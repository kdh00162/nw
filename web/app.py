# -*- coding: utf8 -*- 
from flask import Flask, render_template ,request         #__파일명, app.py의 자체를 의미 import라고 바로써버리면 여러개의 함수를 호출하기 떄문에 from import를 쓰면 flak만 호출
import hashlib

app = Flask(__name__)                                       #render_template = html을 포함한다는 의미 ,리퀘스트는 뭔가를 요청하다 서버가 보낸거면 클라이언트가 나한테 보내는것에대한 처리, 메소드에있는 포스트는 리퀘스트안에 폼은 폼형태를 가진 html데이터가 있다면 그걸 읽어달라고 하는 것 
users = {}

@app.route("/")                                             #/는 주소를 의미      
def hello():
    return render_template("login.html")

@app.route("/name")                       #/이름 하고 주소창에 127.0.0.1:5000(사이트)/name에 들어가면 밑에 입력한 글자가 나옴-
def name():
    return "doheon"

@app.route("/login", methods=['POST'])         #----시작 거절당했을때 밑과 반대가됨 !!!
def login():                                       
        id = request.form['id']
        pw = request.form['pw']
        if id in users:
            if users[id] == hashlib.sha1(pw).hexdigest():
                return "welcome!"
            else: 
                return "login fail!"
        else:
            return "login fail!"        

@app.route("/join", methods=["GET", "POST"])         #로그인 만들고 성공  
def join():                                              #join을 만들어줌 그냥 호출하면 무조건 겟 홈-조인해서해야지 포스트가 되서 로그인됨
    if request.method  == 'POST':                                    # 이프문을 줘서 포스트면 리턴으로 포스트!!를 띄우기
        id = request.form['id']
        pw = request.form['pw']
        if id not in users:
            users[id] = hashlib.sha1(pw).hexdigest()        
        else:
            return "NO! Get out!"
        return "hello!"
    return render_template("join.html")                             #-----여기까지 로그인


@app.route("/add")
@app.route("/add/<int:num1>") 
@app.route("/add/<int:num1>/<int:num2>")           #연산작용하는 사이트를 만들음  # add는 사이트의 이름일뿐,(int)는 함수의 인자를 /를 통해 전달 인트라는뜻이 숫자를 의미 그뒤 넘버 몇이라고 쓰는거 -1179                 
def add(num1=None, num2=None):                     # str 이라는 명령어가 문자열로 묶어서 만들어줌 ""를 넣으면 그냥 문자 그대로만 출력을 해줌
    if num1 is None or num2 is None:                #공통기능을 add로 묶고 나서 하위 2개중 하나라도 인식하면 출력해달라고 표시 if문으로 예외처리
        return "/add/num1/num2"             
    return str(num1 + num2)                         #else등을 사용해서 "아니면" 을 사용             

