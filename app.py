# app.py - main application

from flask import Flask, render_template, session

#Flask App Setup
app = Flask(__name__)

@app.route('/')
def home():
    #로그인 상태에 따라 index 로딩시 상태변수 전달 / 로그인페이지 => 로그아웃으로 변경
    logged = False
    if "user_id" in session:
        logged = True
    return render_template('main.html', logged = logged)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)