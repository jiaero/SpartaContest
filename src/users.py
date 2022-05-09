# users.py - 회원가입 및 로그인 application

from flask import Blueprint, request, render_template, session, jsonify
# from pymongo import MongoClient

#users_bp Setup
users = Blueprint('login', __name__)

#MongoDB Setup - 배포할 때 연결
# client = MongoClient('localhost', 27017)
# db = client.S2lide

@users.route('/')
def login():
    '''
    메인페이지 등에서 로그인 버튼 클릭시 라우터 함수 실행
    로그인 페이지 렌더링 -> 프론트에서 처리?
    '''

# 로그인 페이지에서 로그인 버튼 클릭시 라우터 함수 실행
'''
username, password 모두 입력됐을 경우만 라우터 함수 실행 -> 프론트 처리?

username, password 변수에 저장
비밀번호 암호화

DB에서 username 찾기(함수)
    -> 없으면 return "사용자 정보가 없습니다."
찾은 데이터의 password와 입력받은 password가 같은지 확인
    -> 같다면 세션에 username 저장 후 return 메인 페이지로 이동
    -> 다르다면 return "비밀번호가 틀렸습니다."
'''

# 로그인 페이지에서 회원가입 버튼 클릭시 라우터 함수 실행
'''
회원가입 페이지 렌더링 -> 프론트?
'''

# 회원가입 페이지에서 회원가입 버튼 클릭시 라우터 함수 실행
@users.route('/register', method='POST')
def register():
    '''
    모든 항목이 입력됐을 경우만 라우터 함수 실행 -> 프론트 처리?

    username, email, password, confirm_password 변수에 저장
    password와 confirm_password가 같은지 확인 -> 프론트 처리?
        -> 다르면 return "비밀번호를 다시 확인해 주세요"

    비밀번호 암호화
    username, email, password 객체 생성
    DB에 객체 삽입
    return 로그인 페이지로 이동
    '''
    userName = request.form['user_id']
    return

# username 확인하는 함수 - 중복체크 버튼 클릭 or focus 옮겨질 때 실행
# 회원가입 시 아이디 중복 체크 / 로그인 시 유저 찾기에 사용
'''
username 변수에 저장
DB에서 username 찾기
    -> 있다면 return true
    -> 없다면 return false
'''