from flask import Flask
from flask import request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/nameandloc") # GET 방식으로 전달받는 경우
def nameandloc():
    name = request.args.get('name', '배상우') # request.args.get() 함수 활용
    loc = request.args.get('loc', '세종특별자치시')
    return name + " 님 께서는 " + loc + " 에 살고 계십니다."

@app.route("/")
def hello():
    return """
    <p>This is main page</p>
    <p><a href="/url/hello">현재 URL 읽기(@route 기능)</a></p>
    <p><a href="/nameandloc">이름과 사는 곳 출력하기(GET-URI)</a></p>
    <p><a href="/user">유저 이름 입력하기(POST-html + javascript)</a></p>
    """

@app.route("/user", methods=['GET', 'POST']) # POST 메소드만 전달받음, GET의 경우 예외처리
def post():
    if(request.method == 'GET'):
        return render_template('input.html') # GET으로 접근시 input 받는 html 렌더러 내보냄

    elif(request.method == 'POST'):
        value = request.form['myname']
        return render_template('post.html', name=value, score=100) # POST로 접근시 결과를 나타내는 html 렌더러를 내보냄


@app.route('/url/<urlname>') # 라우터에서 현재 주소값을 읽어오기 가능
def get_profile(urlname):
    return 'This URL is ' + urlname

if __name__ == "__main__":
    app.run()