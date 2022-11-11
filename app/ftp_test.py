import ftplib
import os

host = '192.168.3.46'
user = 'voco-test1'
passwd = 'etevers1123!!'

###############
# 파일 다운로드
###############
try:
  # ftp 연결
  with ftplib.FTP() as ftp:
    ftp.connect(host=host,port=21)
    ftp.encoding = 'utf-8'
    ftp.login(user=user,passwd=passwd)
  # 파일다운로드

    with open('data.txt', 'w') as save_f:
        ftp.retrlines("RETR data.txt", save_f.write)
    print(ftp.nlst())
except Exception as e:
  print(e)