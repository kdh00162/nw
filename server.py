# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩 (네트워크)
import socket                         # 서버.바인드 서버.바인드   바인드를 해야 항구(9999)를 만들고 문을 열어놓는거 = 바인드 한다       
import threading

def handler(conn, address):
     while True:
        try:
            # 클라이언트가 전송한 데이터 수신
            data = conn.recv(1024)                            
        except:                                          
            print "Exception!!!"                               #쓰레드 한 프로세스안에서 여러개가 실행가능하게하는거 하지않으면 동시에 한명밖에 쓰지 못함 쓰레드를 완성하면 여러명이 들어와서 대화가 가능함
            break                                             # tcp는 할일을 다햇거나 예측할수없는상황(인터넷끊김) 외에는 항상 서버와 연결(세션)유지 - 연결되면 하나의 세션이 생겼다. (세션을 보는 명령어 -anop tcp | findstr 9999(파일 이름))
        if not data:                                          #accept배가 항구로들어왔을때 해적선이면 돌려보내는것처럼 (필요한지 아닌지 확인) 받아들이면 소켓이됨  # 어드레스가 소켓을 보관  
            # 데이터를 보내지 않은 클라이언트 연결 종료
            conn.close()                                      # if not 데이터가 없으면 여기로 와라
            break                                             
        # 수신 데이터를 클라이언트에 전송                        
        print "address %s send data: %s" % (address[0], data) #확인법 :cmd에서 cd 파일 있는 경로(desktop) (cd desktop)cd->nw-> python server.py-> 다른 하나더 틀어서 python client.py
        # 수신한 데이터를 클라이언트에 전송  
        conn.send(data)                                       #브레이크를 하면 while을 끝낼수있음
     
     
#서버정보                              # * 은 와일드카드
info = ("0.0.0.0", 9999)            #(127.0.0.1은 나 자신을 의미(거울, 진짜 아이피는 따로있지만 보여줄수있게 설정해줌), 0.0.0.0으로 바꾸면 모두 들어올수있음)
# 소켓 생성
s = socket.socket()                   #프로그래밍을통해서 네트워크를하기위해 통신할때 소켓으로 함 
#9999번 포트 파인딩                    #서버와 클라이언트의 차이점은 서버(제공하다라는 의미클라이언트에게 제공해기위함 아무의미없는 서버는 클라이언트가 필요로하지않음)는 나에게 접속하기를 항상 기다림 바인딩을 해야지 클라이언트가 서버를 찾을수있음    
s.bind(info)                          # 포트 (바닷가 만) 포트는 항구-무수히 많을수있음 항구를 열어놔야(바인드) 배(클라이언트)가 들어옴
# 바인딩 포트 바인딩                   #listen은 열기만하고 보고있는거 (자동문, 뚫려있는거 나갔다 들어옴에 관심이 없음-쳐다만봄)
s.listen(5)                           
while True:                           #listen뒤의 숫자는 그뒤에 5개가오면 5개를 본다는말임 1이면 1개만 봄 더 크게줘도 상관없음
    # 접속요청 승인
    conn, address = s.accept()        # accaept 받아들임
    print "[+] new connection from %s(%d)" % (address[0], address[1]) 
    th =threading.Thread(target=handler, args=(conn,address))
    th.start()




    #while True:
        #try:
            # 클라이언트가 전송한 데이터 수신
            #data = conn.recv(1024)                            
        #except:                                          
           # print "Exception!!"                               #쓰레드 한 프로세스안에서 여러개가 실행가능하게하는거 하지않으면 동시에 한명밖에 쓰지 못함 쓰레드를 완성하면 여러명이 들어와서 대화가 가능함
           # break                                             # tcp는 할일을 다햇거나 예측할수없는상황(인터넷끊김) 외에는 항상 서버와 연결(세션)유지 - 연결되면 하나의 세션이 생겼다. (세션을 보는 명령어 -anop tcp | findstr 9999(파일 이름))
        #if not data:                                          #accept배가 항구로들어왔을때 해적선이면 돌려보내는것처럼 (필요한지 아닌지 확인) 받아들이면 소켓이됨  # 어드레스가 소켓을 보관  
            # 데이터를 보내지 않은 클라이언트 연결 종료
            #conn.close()                                      # if not 데이터가 없으면 여기로 와라
            #break                                             
        # 수신 데이터를 클라이언트에 전송                        
        #print "address %s send data: %s" % (address[0], data) #확인법 :cmd에서 cd 파일 있는 경로(desktop) (cd desktop)cd->nw-> python server.py-> 다른 하나더 틀어서 python client.py
        # 수신한 데이터를 클라이언트에 전송  
        #conn.send(data)                                       #브레이크를 하면 while을 끝낼수있음