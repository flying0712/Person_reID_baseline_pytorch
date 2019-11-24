import os
import shutil
from shutil import copyfile
import re
import numpy as np
import math

# You only need to change this line to your dataset download path
download_path = '../my_data'

Q_MAX_LINE = 1500
LEAST_NUM = 4
MAX_NUM = 100

if not os.path.isdir( download_path ):
    print( 'please change the download_path' )

save_path = download_path + '/pytorch'
if not os.path.isdir( save_path ):
    os.makedirs( save_path )

# -----------------------------------------
# query

query_path_org = download_path + '/query_a'
gallery_path_org = download_path + '/gallery_a'
query_list = download_path + '/query_a_list.txt'

query_save_path = download_path + '/pytorch/query_a'
gallery_save_path = download_path + '/pytorch/gallery_a/g'
if not os.path.isdir( query_save_path ):
    os.mkdir( query_save_path )
#if not os.path.isdir( gallery_save_path ):
 #   os.makedirs( gallery_save_path )

fp = open( query_list, 'r' )
for i in range(Q_MAX_LINE):
    line = fp.readline()
    line = line.strip().replace( '\r', '' ).replace( '\n', '' )
    if(line != ""):
        name, ID = list( re.findall( r"query_a/(.+?) (.*)", line )[0] )
        # name, ID = line.split( ' ' )
        if name != "" and ID != "":
            if not name[-3:] == 'png':
                continue
            if os.path.isfile( query_path_org + '/' + name ):
                src_path = query_path_org + '/' + name
                dst_path = query_save_path + '/' + ID
                #gallery_dst_path = gallery_save_path + '/' + ID
                if not os.path.isdir( dst_path ): #querry
                    os.mkdir( dst_path )
                    copyfile( src_path, dst_path + '/' + name )

                #if not os.path.isdir( gallery_dst_path ):
                 #   os.mkdir( gallery_dst_path )
            else:
                continue
    else:
        break
#
# # ---------------------------------------
# # train_all & val
# train_static = {}
# ID_last = '-1'
# num = 0
# train_path = download_path + '/train_set'
# train_save_path = download_path + '/pytorch/train_all'
# val_save_path = download_path + '/pytorch/val'
# tag_file = download_path + '/train_list.txt'
# if not os.path.isdir( train_save_path ):
#     os.mkdir( train_save_path )
# if not os.path.isdir( val_save_path ):
#     os.mkdir( val_save_path )
#
# fp = open( tag_file, 'r' )
# for i in range(MAX_LINE):
#     line = fp.readline()
#
#     line = line.strip().replace( '\r', '' ).replace( '\n', '' )
#     if (line != ""):
#         name, ID = list( re.findall( r"train/(.+?) (.*)", line )[0] )
#         # name, ID = line.split( ' ' )
#         if name != "" and ID != "":
#             if not name[-3:] == 'png':
#                 continue
#             if os.path.isfile( train_path + '/' + name ):
#                 if ID != ID_last:
#                     if ID_last != '-1': #num with the same id
#                         if num >= LEAST_NUM:
#                             if num > MAX_NUM: #drop some data examples
#                                 num2 = num
#                                 index_i = 1
#                                 index_j = 1
#                                 float_index = list(np.linspace( 1, num2, MAX_NUM ))
#                                 valid_indexs = [int(i) for i in float_index]
#                                 for root, dirs, file_list in os.walk( train_save_path + '/' + ID_last ):
#                                     for file_name in file_list:
#                                         if valid_indexs[index_j - 1] != index_i:
#                                             os.remove( train_save_path + '/' + ID_last+'/' + file_name)
#                                             num -= 1
#                                         else:
#                                             index_j += 1
#                                         index_i += 1
#
#                             train_static.update( {ID_last: num} )
#                         else: #drop all that less than LEAST_NUM
#                             if os.path.isdir(train_save_path + '/' + ID_last):
#                                 shutil.rmtree( train_save_path + '/' + ID_last, True )
#                             if os.path.isdir(val_save_path + '/' + ID_last):
#                                 shutil.rmtree( val_save_path + '/' + ID_last, True )
#
#                     ID_last = ID
#                     num = 1
#                 else:
#                     num += 1
#                 src_path = train_path + '/' + name
#                 dst_path = train_save_path + '/' + ID
#                 val_dst_path = val_save_path + '/' + ID
#                 if not os.path.isdir( dst_path ):
#                     os.mkdir( dst_path )
#
#                 copyfile( src_path, dst_path + '/' + name ) #train set
#
#                 if not os.path.isdir( val_dst_path ): #val set
#                     os.mkdir( val_dst_path )
#                     copyfile( src_path, val_dst_path + '/' + name )
#             else:
#                 continue
#     else:
#         break
#
# print(train_static)