# -*- coding: utf8 -*- 
from flask import Flask, render_template ,request, g , redirect, session, escape     #__파일명, app.py의 자체를 의미 import라고 바로써버리면 여러개의 함수를 호출하기 떄문에 from import를 쓰면 flak만 호출, 플라스크라는 걸 사용해서 기능(라이브러리)을 넣어 만듦, *request : 어떤객체를 보냈는지 알수있게해줌 *g : 별도의 작업없이 어디서는 사용할수있게해줌 *redirect : 로그인에 성공한사람이 또한번 로그인을 하려고 접근했을때 로그인이되었다로 돌려보내는 역할 session : 로그인유지 (사용자의 정보를 고유한 성질로 보관해줌-쿠키) escape : 화면에 출력할때 id를 생성시 코드등 이상한 것으로 만들때 그것을 미연에 방지, render_template = html을 포함한다는 의미 ,리퀘스트는 뭔가를 요청하다 서버가 보낸거면 클라이언트가 나한테 보내는것에대한 처리, 메소드에있는 포스트는 리퀘스트안에 폼은 폼형태를 가진 html데이터가 있다면 그걸 읽어달라고 하는 것 
import hashlib                                                                       #  hashlib a라는 값이 들어가면 똑같이 a를 출력 (패스워드를 검증할때 사용) 무결성 - 데이터가 위변조 되지 않았는가를 검열, 정상인지 아닌지 판단(해쉬값은 고유번호로 데이터마다 다른 키를 제공 하기때문에 해쉬를 서로비교하면 가능)                                                   
import sqlite3                                                                       # 프로그램 실행 
DATABASE = 'database.db'                                                             #database.db 라는 파일을 염

app = Flask(__name__)                                                                
app.secret_key = 'wkssk13'                                                           #세션만들때 비밀번호 만드는거 아무거나 상관없지만 해킹당하면 곤란

                                                                                     #인코딩과 디코딩 : 인코딩 정보의 특정한 규칙에 맞게 형태와 형식을 변환하다(기존 데이터가 변경수될수있음, 암호화 하기위해서는 키가 필요한데 키가 있음)  디코딩
def get_db():                                                                        #데이터베이스를 가져오는 기능                                  
    db = getattr(g, '_database', None)                       
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):                                                     # 연결을 끊어주는 역할 사용자가많아지면 신경써야됨
    db = getattr(g, '_database', None)                                                      
    if db is not None:                                                                  
        db.close()                                                                              

def query_db(quert, args=(), one=False, modify=False):                               # 실제 데이터를 받아서 처리하는 기능   
    cur = get_db().execute(quert, args)                                              # commit 저장    
    if modify:                                                                       # 
        try:                                                                         #   
            get_db().commit()                                                        # 
            cur.close()                                                              #
        except:                                                                         
            return False                                                                
        return True                                                                         
    rv = cur.fetchall()                                                                     
    cur.close()                                                                         
    return (rv[0] if rv else None) if one else rv       #if를 기준으로 바깟쪽부터                                  


@app.route("/logout")                                                  
def logout():
        session.pop('id', None )#세션을 pop빼겠다 id를 그리고 로그인으로 보내겠다
        return redirect('/login')

@app.route("/")                                                   
def hello():
    if 'id' in session: # 세션에 id라는 애가 잇으면 로그인을 하겠다 
        return u'로그인 완료. %s<a href="/logout">로그아웃</a>' % escape(session['id'])#한글을 쓰고싶다면 소문자 u를 입력
    return render_template("login.html")

@app.route("/name")                       #/이름 하고 주소창에 127.0.0.1:5000(사이트)/name에 들어가면 밑에 입력한 글자가 나옴-
def name():
    return "doheon"

@app.route("/login", methods=['POST','GET'])         # 
def login():                                       
        if request.method == 'POST':
            id = request.form['id'].strip()
            pw = hashlib.sha1(request.form ["pw"].strip()).hexdigest()
            sql = "select * from user where id='%s' and password='%s'"% (id, pw)         
            if query_db(sql, one=True):
                #로그인이 성공한경우
                session['id'] = id
                return redirect("/")
            else:
                #로그인이 실패한경우 
                return "<script>alert('아이디 또는 비밀번호를 다시 확인하세요. 등록되지 않은 아이디이거나, 아이디 또는 비밀번호를 잘못 입력하셨습니다.');history.back(-1);</script>"
        if 'id' in session:
            return redirect("/")
        return render_template("login.html")       

@app.route("/join", methods=["GET", "POST"])                             #로그인 만들고 성공  
def join():                                                              #join을 만들어줌 그냥 호출하면 무조건 겟 홈-조인해서해야지 포스트가 되서 로그인됨
    if request.method  == 'POST':                                        # 이프문을 줘서 포스트면 리턴으로 포스트!!를 띄우기
        id = request.form["id"]
        pw = hashlib.sha1(request.form["pw"].strip()).hexdigest()
        sql = "select * from user where id='%s'"% id
        if query_db(sql,one=True):
            return "<script>alert('이미 가입한 아이디가 있습니다.');history.back(-1);</script>"
        sql = "insert into user(id, password) values('%s', '%s')"% (id, pw)
        print sql
        query_db(sql, modify=True)
        return redirect("/login")
    if 'id' in session:
        return redirect("/")
    return render_template("join.html")                             #-----여기까지 로그인


@app.route("/add")
@app.route("/add/<int:num1>") 
@app.route("/add/<int:num1>/<int:num2>")           #연산작용하는 사이트를 만들음  # add는 사이트의 이름일뿐,(int)는 함수의 인자를 /를 통해 전달 인트라는뜻이 숫자를 의미 그뒤 넘버 몇이라고 쓰는거 -1179                 
def add(num1=None, num2=None):                     # str 이라는 명령어가 문자열로 묶어서 만들어줌 ""를 넣으면 그냥 문자 그대로만 출력을 해줌
    if num1 is None or num2 is None:                #공통기능을 add로 묶고 나서 하위 2개중 하나라도 인식하면 출력해달라고 표시 if문으로 예외처리
        return "/add/num1/num2"             
    return str(num1 + num2)                         #else등을 사용해서 "아니면" 을 사용             

