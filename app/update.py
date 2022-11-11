# from gtts import gTTS

# tts = gTTS(
#     text = '안녕 하시렵니 까마귀',
#     lang = 'ko', slow = False
# )
# tts.save('tts_test.mp3')



# import ftplib
# import os

# # ftp 정보
# host = '192.168.3.46'
# user = 'voco-test1'
# passwd = 'etevers1123!!'
 
# # 파일정보
# uploadFile = r'C:/Users/AI8_KSY/Desktop/Web/data2.txt'
 
# ###############
# # 파일 업로드
# ###############
# try:
#   # ftp 연결
#   with ftplib.FTP() as ftp:
#     ftp.connect(host=host,port=21)
#     ftp.encoding = 'utf-8'
#     ftp.login(user=user,passwd=passwd)
 
#     ftp.cwd('/home')  # 현재 폴더 이동
 
#     # 파일업로드
#     with open(file=uploadFile, mode='rb') as wf:
#       ftp.storbinary('STOR data2.txt', wf)
 
#     print(ftp.dir())
 
# except Exception as e:
#   print(e)


# import speech_recognition as sr
# import pyaudio
import time, os
import pymysql
import ftplib
from playsound import playsound
from datetime import datetime
from gtts import gTTS


#DB ip
#ip_address = '192.168.1.166'
ip_address = '192.168.3.68'
#ftp sever ip,id,passwd
host='192.168.3.46'
user='voco-test1'
passwd='etevers1123!!'
# r=sr.Recognizer()
# mic=sr.Microphone()




def speak(index_num):
    index_num = str(index_num)
    print('test_'+index_num+'.mp3')
    try:
        with ftplib.FTP() as ftp:
            
            
            ftp.connect(host=host,port=21)
            ftp.encoding='utf-8'
            ftp.login(user=user,passwd=passwd)
            ftp.cwd('/home')
            with open('test_' + index_num + '.mp3','wb') as save_f:
                ftp.retrlines("RETR test_" + index_num + ".mp3", save_f.write)
            print(ftp.nlst())
    except Exception as e:
        print(e)
    playsound('test_' + index_num + '.mp3')
    #if os.path.exists('test_' + index_num + '.mp3'):
        #os.remove('test_' + index_num + '.mp3')
        

speak(61)