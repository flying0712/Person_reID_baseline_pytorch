import os
import shutil
from shutil import copyfile
import re
import numpy as np
import math

download_path = '../my_data'

train_path = download_path + '/train_set'
tag_file = download_path + '/train_list.txt'
query_path_org = download_path + '/query_a'
gallery_path_org = download_path + '/gallery_a'
query_list = download_path + '/query_a_list.txt'

pytorch_path = download_path + '/pytorch'

train_save_path = download_path + '/pytorch/train_all'
val_save_path = download_path + '/pytorch/val'

query_save_path = download_path + '/pytorch/query'
gallery_save_path = download_path + '/pytorch/gallery'

if not os.path.isdir( pytorch_path ):
    os.mkdir( pytorch_path )

if not os.path.isdir( train_save_path ):
    os.mkdir( train_save_path )
if not os.path.isdir( val_save_path ):
    os.mkdir( val_save_path )

if not os.path.isdir( query_save_path ):
    os.mkdir( query_save_path )
if not os.path.isdir( gallery_save_path ):
    os.mkdir( gallery_save_path )

MAX_LINE =1000
N1 = 200
# train_all & val & query & gallery
train_stat = {}
img_list = []
ID_last = '-1'
num = 0

tag_file = download_path + '/train_list.txt'
fp = open( tag_file, 'r' )
for i in range(MAX_LINE):
    line = fp.readline()
    line = line.strip().replace( '\r', '' ).replace( '\n', '' )
    if (line != ""):
        name, ID = list( re.findall( r"train/(.+?) (.*)", line )[0] )
        # name, ID = line.split( ' ' )
        if name == "" or ID == "" or not name[-3:] == 'png':
            continue

        if ID != ID_last:
            if ID_last!= '-1':
                train_stat.update( {ID_last: [num, img_list]} )
            num = 1
            ID_last = ID
            img_list=[]
            img_list.append( name )
        else:
            num += 1
            img_list.append( name )
train_stat.update({ ID: [num, img_list]} )
print(train_stat)

for ID in  train_stat:
    i += 0
    c_num = train_stat[ID][0]
    if c_num > 1 and c_num <= N1:
        for  name in  train_stat[ID][1]:
            src_path = train_path + '/' + name
            dst_path = train_save_path + '/' + ID
            val_dst_path = val_save_path + '/' + ID
            if not os.path.isdir(dst_path):
                os.mkdir(dst_path)
            copyfile(src_path, dst_path + '/' + name)  # train set
            if not os.path.isdir(val_dst_path):  # val set, only one image
                os.mkdir(val_dst_path)
                copyfile(src_path, val_dst_path + '/' + name)
    elif c_num > N1:
        for  name in  train_stat[ID][1]:
            src_path = train_path + '/' + name
            gallery_dst_path = gallery_save_path + '/' + ID
            query_dst_path = query_save_path + '/' + ID
            if not os.path.isdir(gallery_dst_path):
                os.mkdir(gallery_dst_path)
            copyfile(src_path, gallery_dst_path + '/' + name)  # gallery set
            if not os.path.isdir(query_dst_path):  # query set, only one image
                os.mkdir(query_dst_path)
                copyfile(src_path, query_dst_path + '/' + name)
