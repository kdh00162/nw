# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩 (네트워크)                                      
import socket
import time
# 접속 서버 정보
info = ("127.0.0.1", 9999)      #소켓은 통신을 처리하기위한 라이브러리
# tcp 소켓 생성
s = socket.socket()          
# 서버 접속 
s.connect(info)                 #연결   
# 데이터 전송
s.send("hello sever\n")         #데이터를보냄
# 데이터 수신 및 출력
print s.recv(1024)             
# 접속종료
s.close()