# -*- coding: utf8 -*-
import time                                   #import로 라이브러리를 불러옴
import threading 
import multiprocessing                              #라이브러리 .쓰레드는 라이브러리안에있는것들중에서쓰겠다
def yes(no):
    while True:
        print "yes - %d\n" % no               #괄호 안에 숫자로 표기해줌
        time.sleep(0.5)
def no(no):
    while True:
        print "no - %d\n" % no
        time.sleep(0.5)

#t1 = threading.Thread(target=yes, args=(1,))
#t2 = threading.Thread(target=yes, args=(2,))  #여기까지는 쓰레드를 만들기만하고 실행은 안한상태

#t1.start()                                    # start를 입력해줌으로써 두개의 일을 동시에 할수있게 해줌 지금 큰 쓰레드 안에 2개의 쓰레드를 실행시킨 것(쓰레드안에서 쓰레드를 쪼갠 것)
#t2.start()                                    # 프로세스에서 실행할수있는 최소단위

if __name__ == '__main__':                     #임폴트로 쓰면 메인이아니기 때문에 메인으로 만들어주기위해 파이썬으로 loop.py를 실행하겠다 이것을 넣어주지않으면 나는 독립실행이다라고 생각함
    p1 = multiprocessing.Process(target=yes, args=(1,))
    p2 = multiprocessing.Process(target=yes, args=(2,))
    p1.start()
    p2.start()
    