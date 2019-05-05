from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
from service.model import selectLogin, insertUser

# 플라스크 앱 생성
def createApp():
    app = Flask(__name__)
    # 1. 세션 키 생성 => 통상 값은 해쉬값(중복되지 않는 임의값) 사용
    app.secret_key = 'adfad2321fa34dfasdfadfafdff13131kjjlk12'  # 사용자가 많지 않으므로 임의로 사용
    initRoute(app)
    return app

# 라우트 초기화 담당
def initRoute(app):
    # 라우트 설정
    @app.route('/', methods=['GET', 'POST'])
    def home():
        # 세션이 없어도 처음 접근할 수 있는 로그인페이지. 뒤/앞으로가기 버튼 안먹음.
        # if not 'user_id' in session:
        #     return redirect(url_for('login'))
        # 로그인 성공 => 쿠키 설정.
        # 세션은 모든곳에서 사용가능 id 정보 들어있음.!!
        resp = make_response(render_template('index.html'))
        # 쿠키 세팅
        # resp.set_cookie('user_id', session['user_id'])  # 쿠키도 자료구조 딕셔너리!
        

        return resp  # 응답을 가로채서 던짐.
    #2 login
    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            # 쿠키를 읽어와서 아이디창에 채운다.
            user_email = request.cookies.get('email')
            if not user_email:  # 쿠키 없으면
                user_email = ''  # 쿠키는 아이디를 들고 있거나 없거나.
            return render_template('login.html')
        else:
            # 잘 넘어오는지 체크
            user_email = request.form.get('email')
            user_pw = request.form.get('pw')
            row = selectLogin(user_email, user_pw)
            return redirect(url_for('home'))

    #3 about us
    @app.route('/about')
    def about():
        return render_template('about-us.html')
    
    #SIGNUP 라우트 설정
    @app.route('/signup', methods=['GET'])
    def signup():
        resp = make_response(render_template('signup.html'))
        return resp
       
    # 채용공고 화면 라우트 설정
    @app.route('/category', methods=['GET'])
    def category():
        resp = make_response(render_template('category.html'))
        return resp


