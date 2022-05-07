from selenium import webdriver
import time
import random
# 웹브라우저 작동을 기다리기 위한 라이브러리
# 처리속도가 너무 빠른 경우 정보가 호출되기 전에 프로그램이 실행되어 오류가 발생할 수도 있음
# 아래 라이브러리 대신 Selenium 라이브러리의 "WebDriverWait, By, expected_conditions" 모듈을 써도 됨


# HTML Pasrsing을 위한 라이브러리
# 동적 페이지에서 HTML 정보를 가져온 후 BeautifulSoup 모듈로 해석
from bs4 import BeautifulSoup

# csv 파일 저장을 위한 라이브러리
import pandas as pd

# 시간 관련 라이브러리
# 최종 파일에 오늘의 날짜를 입력하기 위함
from datetime import datetime, timedelta  # 현재 시간
from pytz import timezone  # 한국 기준 시간


# 웹브라우저 작동
browser = webdriver.Chrome()  # 이 명령어가 작동하기 위해선 컴퓨터에 설치된 Chrome의 버전에 맞는 ChromeDriver의 설치가 필요
# https://chromedriver.chromium.org/downloads 에서 다운 가능

# url변수에 5분 순삭 유튜브 링크 입력
url = "https://www.youtube.com/c/%EC%98%A4%EB%B6%84%EC%88%9C%EC%82%AD5minstealer/videos"

# URL 열기
browser.get(url)
# Chrome 창 최대화
browser.maximize_window()

while True:
    # 현재 scrollHeight 값 가져오기
    init_height = browser.execute_script("return document.documentElement.scrollHeight")
    # 평소 사용하던 documnet.body.scrollHeight는 값이 반환되지 않음.
    # 유튜브 페이지에는 스크롤을 내릴 수 있는 곳이 두 개여서 그런듯..?!

    # 현재 scrollHeight 값 만큼 스크롤 아래로 내리기
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")

    # 웹드라이버 동작 기다리기
    # 소수를 쓰는 이유는 로봇 처럼 안보여야 차단 안될것 같아서
    time.sleep(random.uniform(1, 2))

    # 변경된 scrollHeight 값 가져오기
    curr_height = browser.execute_script("return document.documentElement.scrollHeight")  # 변경된 scrollHeight 값 가져오기
    # 이전과 현재 scrollHeight 값 비교하여 같은 경우는 스크롤의 끝이란 뜻이기 때문에 반복문 탈출하기
    if init_height == curr_height:
        break
soup = BeautifulSoup(browser.page_source, "lxml") #HTML을 "lxml"로 파싱(해석)

# 영상 제목에 해당하는 태그'들' 모두 가져오기
title_all = soup.find_all("a", attrs={"id": "video-title"})

list_all_row = []  # 전체 내용을 넣을 리스트

for index, title in enumerate(title_all):
    list_row = []  # for문 안에서 가져와지는 내용을 넣을 리스트
    if "무도" in title.get_text():  # 텍스트 안에 "무도"라는 낱말이 있을 때 list_row에 넣기
        list_row.append(index + 1)  # 영상 순서
        list_row.append(title.get_text())  # 영상 제목
        list_row.append("https://www.youtube.com" + title["href"])  # 영상 링크
    else:  # 텍스트 안에 "무도"가 없는 경우 다음 태그 값 for문으로 돌리기
        continue
    list_all_row.append(list_row)  # 영상 순서, 제목, 링크 list_all_row에 넣기

# CSV파일 만들기
dataframe = pd.DataFrame(list_all_row)  # 데이터 프레임으로 변환
# date_today = datetime.now().strftime("%Y%m%d")  # 오늘 날짜 구하기. 파일 제목 설정을 위함
# dataframe.to_csv(f"{date_today}MuDoList.csv", header=["영상순서", "제목", "링크"], encoding="utf-8-sig")  # csv 파일로 저장

# 웹브라우저 종료
browser.quit()