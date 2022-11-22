import pandas as pd
import numpy as np
import os, librosa, re, glob, scipy
from tqdm import tqdm
import pathlib
import json

# # train, test, val 비율확인
# # 결과 : 
# # ljs_audio_text_test_filelist.txt : 3.816793893129771
# # ljs_audio_text_train_filelist.txt : 95.41984732824427
# # ljs_audio_text_val_filelist.txt : 0.7633587786259541

# file_list =  os.listdir('C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/filelists')
# dict_cnt = {}
# to_cnt=0
# for i in file_list:
#     myFile = open('C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/filelists/' + i, 'r', encoding='UTF-8')
#     cnt = 0
#     while True:
#         if myFile.readline()=='':
#             break
#         cnt += 1
#     print("{} : {}".format(i, cnt))
#     to_cnt += cnt
#     dict_cnt[i] = cnt
#     myFile.close()
# a=0
# for key, value in dict_cnt.items():
#     print("{} : {}".format(key, (value/to_cnt)*100))



#train, val 나누기 7:3비율

text_dir = 'C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/data/script/transcript.v.1.4.txt'
data_dir = 'C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/data'
filelists_dir = 'C:/Users/YGL/Desktop/Team1_Project_Fold/Tacotron2_With_Waveglow_kjh/tacotron2/filelists'
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

f = open(filelists_dir+"/ljs_audio_text_train_filelist.txt", 'w')
f.close()
for i in range(train_num):
    with open(filelists_dir+"/ljs_audio_text_train_filelist.txt", 'a') as f:
            f.write("\n"+data_dir+"/"+metadata[0][i]+"|"+metadata[2][i])

f = open(filelists_dir+"/ljs_audio_text_val_filelist.txt", 'w')
f.close()
for i in range(test_num):
    with open(filelists_dir+"/ljs_audio_text_val_filelist.txt", 'a') as f:
            f.write("\n"+data_dir+"/"+metadata[0][train_num+i]+"|"+metadata[2][train_num+i])


