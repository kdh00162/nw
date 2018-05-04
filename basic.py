# -*- coding: utf8 -*-
# 문자열 출력
print "python"

# 변수 선언
msg = "hello python"
print msg
# 문자열 슬라이싱
print msg[1:3]
print msg[-3:]
print msg[:-2]
print msg[::-1]

# 리스트
data =[]
# 리스트 자료 입력
data.append("hi")
data.append(123)
data.append(1.2)
# 리스트 출력
print data
# 리스트 데이터 제거
data.pop()
print data
data.pop()
print data
# 리스트 요소 인덱스 검색
print data.index("hi")

# index 메소드 실패 시 에러 발생
#print data.index("hi222")

# 사전(딕셔너리)
# { 키 : 값 }
user = {}
user["me"] = {'age' : 30, 'address': 'deajeon'}
user['you'] = {'age':22, 'address': 'seoul'}
# 사전 출력
print user
# 사전 데이터 검색 키 활용
print user['me']
print "uesr keys", user.keys()
print "me" in user.keys() 
# 제어
# if, if else, if elif else
num = 4
if num > 0:
    print "num > 0"

if num > 5:
    print "num > 5"
else:
    print "num < 5" 

if num % 2 == 0:
    print "even"
elif num % 2 == 1:
    print "odd"
else:
    print "????"   

# 함수 
def addition(numbers):         #함수는 def로 만들 수 있음 : 함수 안에 속해있다라고 표시 스코프를 가진다. 함수는 스코프 안에서만 활용가능 
    result = 0                  #하고 쓰는건 주석을 단다고 함 
    for number in numbers:      # 모든 함수가 인자를 필요로 하진 않지만 number가 인자
        result += number 
    return result
 
data = [1, 2, 3] 
print addition(data)       


def help():
    print "id ------- print uesr id"
    print "pwd -------print current path"
    print "quit -------- exit program"
    print "ip ----- print ip address" 

help()
# 라이브러리 불러오기
import os
import platform
import subprocess
# 무한루프 

def shell():
    while True:
        cmd = raw_input('>>> ')                 # pass는 문제가 생겼을때 넘어갈수있게 해준것 브레이크해서 나갈수있게 "bye~"나오게 설정
        if cmd == 'id':
            if platform.system() == 'Windows':
                print os.environ.get('USERNAME')    #파이썬은 윈도우 리눅스 둘다동작 윈도우즈에는 있는값이 리눅스에는 없을수있음 동일하지만 다른방식이기 때문(86,87줄)
            else:                                     #윈도우는 첫번째 글자를 대문자로 해야 인식
                print os.getenv('USER')
        elif cmd == 'pwd': 
            print os.getcwd() 
        elif cmd == 'quit':
            print "bye~"
            break
        elif cmd == 'ip':
            if platform.system() == 'Windows':
                buf = subprocess.check_output('ipconfig')     #윈도우에서는 ip 리눅스에서는 if로 표시
                index = buf.find("IPv4")
                newline = buf[index:].find("\n")               #ipv4를 인덱스로 커서처럼 표시 이네덱스로부터 다음줄newline까지 몇칸이나 가야하나를 newline 그래서 인덱스 플러스 뉴라인를 플러스
                # print index, newline
                ipline = buf[index:index+newline]              #nw폴더에 들어가서 cmd를 주소창에 치면 폴더에서 커멘드를 칠수있음
                ip = ipline.split(':')
                print (ip[1].strip())                          #strip은 필요없는걸 벗겨내는것 (':')는 :기준으로 나타내는것 -ex) ipv4주소 ...... : 192.168.40.128 니까 0:1 로 1을 표시해달라고 표시 하지만 ipv4앞에 띄어쓰기가있어서 스트립으로 벗겨냄
            else:
                buf = subprocess.check_output('ifconfig')
                target = 'addr:'
                index = buf.find(target) + len(target)
                space = buf[index:].find(' ')
                print index, space
                print buf[index:index+space]                   #html 은 홈페이지만들때 읽을수있게 한 방식
                
        else:
            help() 
    
# urllib2 사용
import urllib2
import re
ur1 = 'https://box.cdpython.com/ezen/'        # 주소에 리퀘스트를 해서 리스판을 받고 html을 읽어달라고하고 프린트로 출력해달라고 함
req = urllib2.Request(ur1)
res = urllib2.urlopen(req)
html = res.read() 
# print html
# re 모듈 (정규표현식)을 이용한 패턴매칭  [정규표현식 - 많은데이터중에 내가 원하는것을 찾기위함 ex)127.0.0.1/31337 \d+\.\d+\.\d+\.\d+\/\d+ 여기에 플러스를 붙이면 하나또는 그이상 d가 숫자를 의미]
ipaddress, port = re.findall(r"\d+\.\d+\.\d+\.\d+\/\d+", html)[0].split('/')       #패턴데이터 앞에는 r을 붙여줌을 권장
print "ip", ipaddress, "port:", port    
# 파이썬 도움말 이용
