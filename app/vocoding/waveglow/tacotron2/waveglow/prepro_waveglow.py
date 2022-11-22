import pandas as pd
import numpy as np
import os, librosa, re, glob, scipy
from tqdm import tqdm
import pathlib
import json



#train, val 나누기 7:3비율

text_dir = 'C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/data/script/transcript.v.1.4.txt'
data_dir = 'C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/data'
filelists_dir = 'C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/waveglow'
# text_dir = '/data/script/transcript.v.1.4.txt'
# filters = '([.,!?])'

metadata = pd.read_csv(text_dir, dtype='object', sep='|', header=None)

# print(metadata.head())
# print(len(metadata))
# print(len(metadata[0]))
# print(len(metadata[0][0]))
# print(metadata[1][0])
# print(type(metadata))
# print(metadata[0])

# 데이터 총 갯수 세기
# 12854개
myFile = open(text_dir, 'r', encoding='UTF-8')
cnt = 0
while True:
    if myFile.readline()=='':
        break
    cnt += 1
to_data = cnt
myFile.close()
# print(cnt)


# 7대3으로 나눈 갯수
train_num = round(to_data*0.7)
test_num = to_data-train_num
# print(train_num)
# print(test_num)

f = open(filelists_dir+"/train.txt", 'w')
f.close()
for i in range(to_data):
    with open(filelists_dir+"/train.txt", 'a') as f:
            f.write("\n"+data_dir+"/"+metadata[0][i])