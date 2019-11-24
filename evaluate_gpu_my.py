import scipy.io
import torch
import numpy as np
#import time
import os

#######################################################################
# Evaluate
def evaluate(qf,ql,gf,gl):
    query = qf.view(-1,1)
    score = torch.mm(gf,query)
    score = score.squeeze(1).cpu()
    score = score.numpy()
    index = np.argsort(score)  #from small to large
    index = index[::-1]
    return index[0:200]

######################################################################
result = scipy.io.loadmat('pytorch_result.mat')
query_feature = torch.FloatTensor(result['query_f'])
query_cam = result['query_cam'][0]
query_label = result['query_label'][0]
gallery_feature = torch.FloatTensor(result['gallery_f'])
gallery_cam = result['gallery_cam'][0]
gallery_label = result['gallery_label'][0]

max_index_200 = []
#print(query_label)
for i in range(len(query_label)):
    max_index_200[i] = evaluate(query_feature[i],query_label[i],gallery_feature,gallery_label)
