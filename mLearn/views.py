from django.shortcuts import render, redirect, get_object_or_404

# message불러올때
from django.contrib import messages

# 외부자료 입력할때
import sys

from .forms import MLearnForm
from .models import MLearn

# decorator 불러들일때
from django.contrib.auth.decorators import login_required

## 데이터 추출
# urllib.request 사용 (데이터 다운로드)
import urllib.request

# requests 패키지 사용(고급)
import requests
# urlencode() 사용하기 위함 : 매개변수 처리
import urllib.parse

# BeautifulSoup4 운용
from bs4 import BeautifulSoup

# 상대경로를 절대경로로 전환위해
from urllib.parse import urljoin

# json 정보 처리위해
import json

# 정규표현식 사용할때
import re

# selenium을 통해 웹브라우저 접근시
from selenium import webdriver

# mysql 연결위해
import pymysql

# path내 파일 존재유무 확인시
import os.path, glob                        ## 차이 :  from django.urls import path

# csv 파일 처리위해
import csv

# excel 파일 처리
import openpyxl

# pandas 분석 처리
import pandas as pd

# numpy(다차원 배열 처리)
import numpy as np

# metplotlib(PLOT처리)
from matplotlib import pyplot as plt

# Pillow를 이용한 이미지 처리
from PIL import Image
# OpenCV를 통한 이미지/영상 처리
import cv2

# scikit Learn 활용위해
from sklearn import svm, metrics
# joblib 모듈 사용위해
# from sklearn.externals import joblib
import joblib

# random 숫자 추출
import random

from sklearn.model_selection import train_test_split

# gzio 압축 해제
import gzip

# cgi 처리 위해
import cgi

# RandonForestClassifier 처리위해
from sklearn.ensemble import RandomForestClassifier
# TensorFlow 사용을 위해
# import tensorflow as tf



# =============================================================
# Create your views here.
def mLearnHome(request):
    mLearnList = MLearn.objects.all()
    item = MLearn.objects.get(id=4)

    data = {
        'mLearnList': mLearnList,
        'item': item,
    }

    return render(request, 'mLearn/mLearnHome.html', data)

# @login_required
def mLearnAdd(request):

    if request.method == 'POST':
        form = MLearnForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "New MLearn was successfully added!")
            return redirect('mLearn:mLearnHome')

    else:
        form = MLearnForm()
        data = {
            'form' : form,
            # 'csrfmiddlewaretoken': '{{ csrf_token }}',
        }
    return render(request, 'mLearn/mLearnForm.html', data)

def mLearnEdit(request, mLearn_id):
    mLearnList = MLearn.objects.all()
    item = get_object_or_404(MLearn, pk=mLearn_id)

    data = {
        'mLearnList' : mLearnList,
        'item' : item,
    }

    return render(request, 'mLearn/mLearnEdit.html', data)

def mLearnReform(request, mLearn_id):

    item = get_object_or_404(MLearn, pk=mLearn_id)

    if request.method == 'POST':
        form = MLearnForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'New mLearn was successfully edited!')
            return redirect('mLearn:mLearnHome')

    else:
        form = MLearnForm(instance=item)
        data ={
            'form' : form,
        }
    return render(request, 'mLearn/mLearnForm.html', data)


# Exercise ========================================================================
def exHome(request):
    return render(request, 'mLearn/exHome.html')

def download(request):

    ##1. urlretrieve() 저장
    savename = "C:/Users/ilee/PycharmProjects/mLearn/test.png"
    url1 = "http://uta.pw/shodou/img/28/214.png"

    urllib.request.urlretrieve(url1, savename)
    print("urlretrieve ()로 파일이 저장되었습니다")

    ##2. urlopen() 함수사용 저장
    mem = urllib.request.urlopen(url1).read()
    with open(savename, mode="wb") as f:
        f.write(mem)
    print("urlopen()로 파일이 저장되었습니다")

    ##  저장하지 않고 오픈한상태에서 문자열로 처리후 보기
    url2 = "http://api.aoikujira.com/ip/ini"
    mem1 = urllib.request.urlopen(url2).read()

    text1 = mem1.decode("utf-8")  ## 바이너리를 text(문자열)로 변환하기 :  decode('utf-8')
    print('텍스트:'+text1)


    ## url로 요청 접근시 매개변수를 추가하여 접근 : urllib.parse 모듈의 urlencode()함수
    url3 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    value = {
        'stnId': '108'
    }
    params = urllib.parse.urlencode(value)    ## 매개변수 값을 dict자료형에서 url 코드로 만듬: urlencode() {a: b} = > a = b
    url3 = url3 + "?" + params               ## 요청 전용 URL을 생성합니다 : get방식으로 매개변수 처리
    print("url?param= :", url3)

    mem3 = urllib.request.urlopen(url3).read()
    text2 = mem3.decode("utf-8")            ##  binary 데이터(대부분의 웹 데이터)를 text 문자열로 전환하기: decode()
    # print('매개변수추가하여 웹 접근:'+text2)


    ##3. requests() 패키지 이용(고급)  : HTTP 요청을 보내는 모듈 사용
    req = requests.get("http://wikibook.co.kr/wikibook.png")
    req1 = requests.post("http://api.aoikujira.com/time/get.php")

    text3= req1.text            # 텍스트 형식으로 추출
    print('requests방식으로 텍스트 데이터 :' +text3)

    mem4 = req1.content                      ##   mem = urllib.request.urlopen(url).read()  바이너리 데이터
    text4 = mem4.decode("utf-8")
    # print('requests방식으로 바이너리 데이터 :' +mem4)
    print('requests방식으로 text 데이터 :' +text4)

    with open(savename, "wb") as f:         ##   바이너리 형식으로 png 데이터 저장(text 이외에는 바이너리 형태로 저장)
        f.write(req1.content)
        print("requests()이용한 saved")

    return render(request, 'mLearn/exHome.html')


def beautifulSoup(request):

    # lessen #1 : links
    html = """
    <html><body>
      <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
      </ul>
    </body></html>
    """

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all("a")

    # 링크 목록 출력하기 ---
    for a in links:
        href = a.attrs['href']
        text = a.string
        print(text, ">", href)

    # lessen #2 : Tag명으로 분류 : 분석하고 싶은 HTML --- (※2)
    html = """
        <html><body>
          <h1>스크레이핑이란?</h1>
          <p>웹 페이지를 분석하는 것</p>
          <p>원하는 부분을 추출하는 것</p>
        </body></html>
    """
    soup = BeautifulSoup(html, 'html.parser')

    h1 = soup.html.body.h1                          # 원하는 부분 추출하기 -- tag 명으로 추출
    p1 = soup.html.body.p
    p2 = p1.next_sibling.next_sibling

    print("h1 = " + h1.string)                      # 요소의 글자 출력하기 --- (※5)
    print("p  = " + p1.string)
    print("p  = " + p2.string)

    # lessen #3 : 선택자 한개 : soup.select_one(<selector>)  /// 선택자로 여러개 리스트 추출 : soup.select(<selector>)
    html = """
        <html><body>
        <div id="meigen">
          <h1>위키북스 도서</h1>
          <ul class="items">
            <li>유니티 게임 이펙트 입문</li>
            <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
            <li>모던 웹사이트 디자인의 정석</li>
          </ul>
        </div>
        </body></html>
    """

    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.select_one("div#meigen > h1").string          # 타이틀 부분 추출하기 --- (※3)
    print("h1 =", h1)
    li_list = soup.select("div#meigen > ul.items > li")     # 목록 부분 추출하기 --- (※4)
    for li in li_list:
        print("li =", li.string)

    # lessen #4 : 환율 데이터 추출
    req = requests.post("https://finance.naver.com/marketindex/")
    mem4 = req.content

    soup1 = BeautifulSoup(mem4, "html.parser")
    price2 = soup1.select_one("div.head_info > span.value").string
    print('requests usd/krw:', price2)


    url = "https://finance.naver.com/marketindex/"
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    price = soup.select_one("div.head_info > span.value").string
    print("urllib.request usd/krw =", price)



    # naver의 주식 사이트 검색
    resp = requests.get('https://finance.naver.com/item/coinfo.nhn?code=005930')
    resp.raise_for_status()

    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.select("#aside ul li a")

    for item in items:
        print(item.string)

    # investing.com의IBM 주식 사이트에서 내용 발췌
    browser = webdriver.Chrome("C:/Users/ilee/PycharmProjects/mLearn/chromedriver/chromedriver.exe")
    browser.implicitly_wait(3)

    url = "https://www.investing.com/equities/ibm-historical-data"

    ## 로그인페이지 접근
    browser.get(url)

    items = browser.find_elements_by_css_selector("#curr_table tbody tr td")

    for item in items:
        print(item.text)

    browser.quit()



    return render(request, 'mLearn/exHome.html')


## CSS 선택자
def select(request):

    # ## lessen #1 : 기본 선택자
    # # fileName = "C:/Users/ilee/PycharmProjects/mLearn/test.html"
    # # html = open(fileName, encoding="utf-8")
    # html = '''
    #     <html>
    #       <body>
    #         <ul id="bible">
    #           <li id="ge">Genesis</li>
    #           <li id="ex">Exodus</li>
    #           <li id="le">Leviticus</li>
    #           <li id="nu">Numbers</li>
    #           <li id="de">Deuteronomy</li>
    #         </ul>
    #           <ul id = "fr-list">
    #             <li class ="red green" data-lo="ko" > 사과 < / li >
    #             < li class ="purple" data-lo="us" > 포도 </ li >
    #             < li class ="yellow" data-lo="us" > 레몬 < / li >
    #             < li class ="yellow" data-lo="ko" > 오렌지 < / li >
    #           < / ul >
    #           < ul id = "ve-list" >
    #             < li class ="white green" data-lo="ko" > 무 < / li >
    #             < li class ="red green" data-lo="us" > 파프리카 < / li >
    #             < li class ="black" data-lo="ko" > 가지 < / li >
    #             < li class ="black" data-lo="us" > 아보카도 < / li >
    #             < li class ="white" data-lo="cn" > 연근 < / li >
    #           < / ul >
    #       </body>
    #     </html>
    #     '''
    #
    # soup = BeautifulSoup(html, "html.parser")
    #
    # # 다양한 선택자 검색
    # sel = lambda q: print(soup.select_one(q).string)
    #
    # sel("#nu")  # id = nu
    # sel("li#nu")  # li가 id=nu인 태그
    # sel("ul > li#nu")  # ul 밑에 li(id=nu)인 태그
    # sel("#bible #nu")  # id=bible 밑에 id=nu인 태그
    # sel("ul#bible > li#nu")  # ul(id=bible) 밑에 li(id=nu)인 태그
    # sel("li[id='nu']")  # li(id=nu)인 태그
    # sel("li:nth-of-type(4)")  # li 4번째 순서  nth-of-types(1,2,3,4,...)
    #
    # print(soup.select("li")[3].string)  # select의 list에 배열[0,1,2,3,4...]
    # print(soup.find_all("li")[3].string)  # find_all list에 배열[0,1,2,3,4..]
    #
    # print(soup.select_one("li:nth-of-type(3)").string)
    # print(soup.select_one("#fr-list > li:nth-of-type(2)").string)
    # print(soup.select("#fr-list > li[data-lo='us']")[0].string)
    # print(soup.select("#fr-list > li.yellow")[1].string)
    #
    # cond = {
    #     "data-lo": "us",
    #     "class": "purple"
    # }
    # print(soup.find("li", cond).string)
    # print(soup.find(id="fr-list").find("li", cond).string)

    ## lessen #2 : 정규표현식 https에서 추출
    # html2 = """
    #     <ul>
    #       <li><a href="hoge.html">hoge</li>
    #       <li><a href="https://example.com/fuga">fuga*</li>
    #       <li><a href="https://example.com/foo">foo*</li>
    #       <li><a href="http://example.com/aaa">aaa</li>
    #     </ul>
    # """
    # soup2 = BeautifulSoup(html2, "html.parser")

    # 정규 표현식으로 href에서 https인 것 추출하기
    # temp = soup2.find_all(href=re.compile(r"^https://"))
    # for e in temp:
    #     print(e.attrs['href'])

    ## lessen #3 : 윤동주 시 발췌
    url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
    res = urllib.request.urlopen(url)
    soup1 = BeautifulSoup(res, "html.parser")

    a_list = soup1.select("#p-views > ul > li a")
    for a in a_list:
        name = a.string
        print("-", name)

    return render(request, 'mLearn/exHome.html')


## 상대경로   urljoin()
def path(request):
    base = "http://example.com/html/a.html"

    print(urljoin(base, "b.html"))
    print(urljoin(base, "sub/c.html"))
    print(urljoin(base, "../index.html"))
    print(urljoin(base, "../img/tiger.png"))
    print(urljoin(base, "http://otherExample.com/wiki"))
    print(urljoin(base, "//anotherExample.com/test"))

    return render(request, 'mLearn/exHome.html')


## 로그인 모듈 추출하기(로그인해서 웹 자료 얻어내기 위함)
def login(request):

    session = requests.session()

    ## 예제1) www.hanbit.co.kr 로그인

    USER = "aaaa"
    PASS = "asdfvcxz!"
    login_info = {
        "m_id": USER,  # 아이디 지정
        "m_passwd": PASS  # 비밀번호 지정
    }

    # post 방식으로 로그인 파일 접근하기
    # http: // www.hanbit.co.kr / member / login.html 파일에서 로그인 처리 파일을 찾아야됨

    url = "http://www.hanbit.co.kr/member/login_proc.php"
    resp = session.post(url, data=login_info)
    resp.raise_for_status()  # 오류가 발생하면 예외가 발생합니다.

    # 마이페이지에 접근하기
    mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
    resp= session.get(mypage)
    resp.raise_for_status()

    # 마일리지와 이코인 가져오기
    soup = BeautifulSoup(resp.text, "html.parser")

    mileage = soup.select_one(".mileage_section1 span").string
    ecoin = soup.select_one(".mileage_section2 span").string
    rank = soup.select_one(".my_rating  p span").string

    print("마일리지: " + mileage)
    print("e코인: " + ecoin)
    print("my rank : "+rank)

    ## 예제2) www.korea.com 로그인

    USER = "ilee"
    PASS = "431#Jaap01"
    login_info = {
        "user": USER,           # 아이디 지정
        "password": PASS        # 비밀번호 지정
    }

    url = "https://id.korea.com/ca.php"
    resp = session.post(url, data=login_info)
    resp.raise_for_status()  # 오류가 발생하면 예외가 발생합니다.

    mypage = "http://mbox04.korea.com/main.crd?count=2"
    resp = session.get(mypage)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, "html.parser")

    links = soup.select(".textN a")
    for a in links:
        name = a.string
        print("-", name)

    link = soup.select_one(".td-title span span")
    print("name:"+link.string)

    return render(request, 'mLearn/exHome.html')


## 날씨 정보 구함(도시, API키를 통해)
def weather(request):
    # API 키를 지정합니다.
    apikey = "7ac07ba17e1c3134df00c2950477ea26"

    # 날씨를 확인할 도시 지정하기 --- (※2)
    cities = ["Seoul, KR", "Tokyo, JP", "New York, US"]

    # API 지정 --- (※3)
    api = "http://api.openweathermap.org/data/2.5/weather?q={cityName}&APPID={key}"

    # 각 도시의 정보 추출하기
    for name in cities:
        # API의 URL 구성하기
        url = api.format(cityName=name, key=apikey)
        print(url)

        # API에 요청을 보내 데이터 추출하기
        req = requests.get(url)

        # 결과를 JSON 형식으로 변환하기: json형식{a:b,} => data[a]=b
        data = json.loads(req.text)
        print(data)

        # lambda식 : lambda 인자 : 식     lam = lambda a,b: a + b  lam(2,3) 5   켈빈 온도를 섭씨 온도로 변환하는 함수
        k2c = lambda k: k - 273.15

        # 출력하기
        print("도시 =", data["name"])
        print("날씨 : ", data["weather"][0]["description"])
        print("기온 :", k2c(data['main']['temp']))
        print("풍향:", data['wind']['deg'])
        print('풍속:', data['wind']['speed'])

    return render(request, 'mLearn/exHome.html')


def selenium(request):

    # Ex1) www.hanbit.co.k

    USER = "aaaa"
    PASS = "asdfvcxz!"

    browser = webdriver.Chrome("C:/Users/ilee/PycharmProjects/mLearn/chromedriver/chromedriver.exe")
    # browser = webdriver.PhantomJS("C:/Users/ilee/PycharmProjects/mLearn/phantomjs/bin/phantomjs.exe")

    browser.implicitly_wait(3)

    url_login = "http://www.hanbit.co.kr/member/login.html"

    ## 로그인페이지 접근
    browser.get(url_login)

    elem = browser.find_element_by_id("m_id")
    elem.clear()
    elem.send_keys(USER)
    elem1 = browser.find_element_by_id("m_passwd")
    elem1.clear()
    elem1.send_keys(PASS)

    form = browser.find_element_by_id("login_btn")
    form.click()                                        # form.submit()
    print("로그인 버튼을 클릭합니다.")

    # 마이페이지에 접근하기
    url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
    browser.get(url_mypage)

    mileage = browser.find_element_by_css_selector(".mileage_section1 span").text
    ecoin = browser.find_element_by_css_selector(".mileage_section2 span").text
    print("selenium을 통한 마일리지: " + mileage)
    print("selenium을 통한 e코인: " + ecoin)

    ## BeautifulSoup 적용
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 분석/추출
    mileage = soup.select_one(".mileage_section1 span").get_text()
    ecoin = soup.select_one(".mileage_section2 span").get_text()
    print("BeautifulSoup을 통한 마일리지: " + mileage)
    print("BeautifulSoup을 통한 e코인: " + ecoin)

    # 브라우저 종료하기 ---
    browser.quit()

    # Ex2) kora.com
    USER = "ilee"
    PASS = "431#Jaap01"

    browser = webdriver.Chrome("C:/Users/ilee/PycharmProjects/mLearn/chromedriver/chromedriver.exe")
    browser.implicitly_wait(3)

    url_login = "https://id.korea.com/"

    browser.get(url_login)

    elem = browser.find_element_by_id("user")
    elem.clear()
    elem.send_keys(USER)

    elem = browser.find_element_by_id("password")
    elem.clear()
    elem.send_keys(PASS)

    form = browser.find_element_by_css_selector( "input.btn_login[type=submit]")
    form.submit()

    mypage = "http://mbox04.korea.com/main.crd?count=2"
    browser.get(mypage)

    browser.save_screenshot("C:/Users/ilee/PycharmProjects/mLearn/test3.png")

    name = browser.find_element_by_css_selector(".td-title span span").text
    print("selenium korea의 이름:"+name)


    # Ex3) naver.com (화면보호기 기능 추가로 로그인이 않됨)
    # USER = "idillee01"
    # PASS = "ves941"
    #
    # browser = webdriver.Chrome("C:/Users/ilee/PycharmProjects/mLearn/chromedriver/chromedriver.exe")
    # browser.implicitly_wait(3)
    #
    # # url_login = "https://nid.naver.com/nidlogin.login"
    # url_login = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
    #
    # browser.get(url_login)
    #
    # res = browser.find_element_by_id("id")
    # res.clear()
    # res.send_keys(USER)        ## id=id인 공간에 USER1 값 입력
    #
    # res = browser.find_element_by_id("pw")
    # res.clear()
    # res.send_keys(PASS)       ## id=pw인 공간에 PASS1 값 입력
    #
    # form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
    # form.click()  ## <input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global">
    # print("로그인 버튼을 클릭합니다")
    #
    # ####   현재 화면 보호기 기능 추가로 로그인에 한계가 있음
    #
    # url_mypage = "https://nid.naver.com/user2/help/naverProfile.nhn?m=viewModifyProfile&token_help=j5TgbzfiusMvf3S3"
    #
    # browser.get(url_mypage)
    #
    # html = browser.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # # 분석/추출
    # nic = soup.select_one("#inpNickname").get_text()
    #
    # # nic = browser.find_element_by_css_selector(".nic_desc")
    # # nic = soup.find_element_by_id("inpNickname")
    #
    # print("naver 별명:"+nic)

    ##Ex3)  직접 자바스크립트 실행하기.execute_script()
    browser = webdriver.Chrome("C:/Users/ilee/PycharmProjects/mLearn/chromedriver/chromedriver.exe")
    browser.implicitly_wait(3)

    browser.get("https://google.com")

    resp = browser.execute_script("return 100+150")
    print(resp)


    # 쇼핑 페이지의 데이터 가져오기 --- (※5)
    # browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

    # 메소드 #2 : 화면을 캡처해서 저장하기 .save_screenshot(fileName)
    # browser.save_screenshot("C:/Users/ilee/PycharmProjects/mLearn/test3.png")

    # 브라우저 종료하기 ---
    browser.quit()

    return render(request, 'mLearn/exHome.html')

def mysql(request):

    ## Mysql 연결하기(pymysql로 연결, django와 별도)
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='p23794',
        db='opensky',
        charset='utf8'
    )

    ## cursor 추출하기 : control structure of database
    cursor = conn.cursor()

    ## 같은 db 테이블 이름 지우기
    cursor.execute('DROP TABLE tests')

    ## 테이블 생성하기
    sql = '''
            CREATE TABLE tests (
                item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name TEXT,
                price INTEGER
            )'''
    cursor.execute(sql)
    conn.commit()

    ## 데이터 추가하기
    data = [('banana', 1000), ('사과', 500), ('망고', 800)]
    for i in data:
        sql = "INSERT INTO tests(name, price) VALUES(%s, %s)"
        cursor.execute(sql, i)

    ## 데이커 추출하기
    sql = "SELECT * FROM tests"
    cursor.execute(sql)
    conn.commit()
    for row in cursor.fetchall():
        print(row)

    return render(request, 'mLearn/exHome.html')


def datatype(request):
    return render(request, 'mLearn/datatype.html')

# dictionary, json => json파일에 저장하고 json으로 read
def jsontype(request):
    url = "https://api.github.com/repositories"

    ## 다운로드해서 처리하는것이 효율적
    savename = "C:/Users/ilee/PycharmProjects/mLearn/test.json"

    ## 저장하기(가장 단순한 저장방식)
    if not os.path.exists(url):
        urllib.request.urlretrieve(url, savename)

    ## json 파일 reading

    resp = open(savename, "r", encoding="utf-8").read()
    items = json.loads(resp)

    # items = json.load(open(savename, "r", encoding="utf-8"))

    for item in items:
        name = item['name']
        login = item['owner']['login']
        print(name+"---"+login)

    return render(request, 'mLearn/datatype.html')

# xml => xml저장, xml을 html.parser
def xmltype(request):
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
    savename = "C:/Users/ilee/PycharmProjects/mLearn/test.xml"

    ## 저장하기
    if not os.path.exists(url):
        urllib.request.urlretrieve(url, savename)

    ### BeautifulSoup로 xml 파일 분석 :: html.parser
    xmlfile = open(savename, "r", encoding="utf-8").read()
    soup = BeautifulSoup(xmlfile, 'html.parser')

    ## 데이터 설정하기
    info = {}
    for location in soup.find_all("location"):
        name = location.find("city").string
        weather = location.find("wf").string
        if not (weather in info):
            info[weather] = []
        info[weather].append(name)

    ## 지역날씨 구분해서 출력하기
    for weather in info.keys():
        print("+", weather)
        for name in info[weather]:
            print("| -", name)

    return render(request, 'mLearn/datatype.html')


def csvtype(request):

    # EUC_KR로 저장된 CSV 파일 읽기
    filename = "C:/Users/ilee/PycharmProjects/mLearn/list-euckr.csv"
    csvfile = open(filename, "r", encoding='euc_kr')

    ## csv를 python list로 변환하기
    # data = []
    # rows = csvfile.split("\r\n")        # \r\n : new line
    # for row in rows:
    #     if row == "":
    #         continue
    #     cells = row.split(",")
    #     data.append(cells)

    ## 위 파일을 csv.reader()
    # data = csv.reader(csvfile, delimiter=",", quotechar='"')

    data = csv.reader(csvfile)

    # 결과 출력하기
    for c in data:
        print(c[1] + ":" + c[2])

    for line in data:
        print(line)

    ##  csv 쓰기 새로 생성할때
    # with open(filename, "w", encoding="euc_kr") as fp:
    #     writer = csv.writer(fp, delimiter=",", quotechar='"')
    #     writer.writerow(["ID", "이름", "가격"])
    #     writer.writerow(["1000", "SD 카드 ", 30000])
    #     writer.writerow(["1001", "키보드", 21000])
    #     writer.writerow(["1002", "마우스", 15000])
    #     writer.writerow(["1004", "마우스", 23000])

    return render(request, 'mLearn/datatype.html')

def excel(request):
    xlfile = "C:/Users/ilee/PycharmProjects/mLearn/test.xlsx"
    wb = openpyxl.load_workbook(xlfile)

    # 현재의 active sheet (첫번째 시트) : defautl [0]
    ws = wb.active

    sum = 0
    for r in ws.rows:
        # column_index = r[0]
        id = r[0].value
        name = r[1].value
        price = r[2].value

        sum = sum + price
        print(id, name, price)

    # 합계 쓰기
    ws.cell(row=6, column=3).value = sum

    # 엑셀 파일 저장
    wb.save("C:/Users/ilee/PycharmProjects/mLearn/test2.xls")

    wb.close()



    return render(request, 'mLearn/datatype.html')

def pandas(request):

    #1 Series(1차원 배열)
    data = np.array(['a', 'b', 'c', 'd'])
    s = pd.Series(data, index=[100, 101, 102, 103])
    print(s)

    #2 DataFrame
    data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

    # With two column indices, values same as dictionary keys
    df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
    print(df1)
    # With two column indices with one index with other name
    df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
    print(df2)

    data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
    df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
    print(df)

    data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(data)
    print(df)

    #3 Pannel

    return render(request, 'mLearn/exHome.html')

def plot(request):
    # Matplotlib를 이용한 plot
    plt.plot(["Seoul", "Paris", "Seattle"], [30, 25, 55])
    plt.plot(["Seoul", "Paris", "Seattle"], [-10, 30,20])

    plt.xlabel('City')
    plt.ylabel('Response')
    plt.title('Experiment Result')
    plt.legend(['Mouse', 'Cat'])

    plt.show()

    return render(request, 'mLearn/exHome')

def image(request):

    #EX1) Pillow를 이용한 image
    im = Image.open('C:/Users/ilee/PycharmProjects/mLearn/test.png')
    im.show()
    im.save('C:/Users/ilee/PycharmProjects/mLearn/test1.png')

    #Ex2) Open CV를 이용한 이미지처리
    img = cv2.imread('C:/Users/ilee/PycharmProjects/mLearn/animal_3.jpg', 1)
    cv2.imshow('Test Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite('C:/Users/ilee/PycharmProjects/mLearn/test2.jpg', img)

    #Ex3) Open CV를 이용한 영상 처리
    cap = cv2.VideoCapture('C:/Users/ilee/PycharmProjects/mLearn/05 I Look To You.mp3')

    while cap.isOpened():
        success, frame = cap.read()
        if success:
            cv2.imshow(' 동영상 윈도우', frame)

            # ESC를 누르면 종료
            key = cv2.waitKey(1) & 0xFF
            if (key == 27):
                break

    cap.release()
    cv2.destroyAllWindows()

    # Ex4)  Image(JPG) to CSV conversion

    fileList = createFileList('C:/Users/ilee/PycharmProjects/mLearn/mnist/')
    for file in fileList:
        print(file)
        img_file = Image.open(file)
        img_file.show()

        # get original image parameters...
        # width, height = img_file.size
        # format = img_file.format
        # mode = img_file.mode

        value = np.array(img_file)    # np 배열 생성
        img_list = value.tolist()     # list로 리턴
        print(img_list)

        # with open(fil_name + '.csv', 'w', newline='') as csvfile:
        with open("C:/Users/ilee/PycharmProjects/mLearn/mnist/img_pixels.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(img_list)

        # option#! Make image Greyscale
        # img_grey = img_file.convert('L')
        # value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
        # # img_grey.save('result.png')
        # img_grey.show()
        #
        # value = value.flatten()
        # print(value)
        # with open("C:/Users/ilee/PycharmProjects/mLearn/mnist/img_pixels.csv", 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(value)

    return render(request, 'mLearn/exHome')

def scikit(request):

    ##EX1. XOR
    xor_data = [
        # P, Q, Results
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    # 옵션1 : Basic (데이터와 레이블 분리)
    # data = []
    # label = []
    # for row in xor_data:
    #     p = row[0]
    #     q = row[1]
    #     r = row[2]
    #
    #     data.append([p, q])
    #     label.append(r)

    #옵션2: pandas DataFrame 이용 : 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기
    df = pd.DataFrame(xor_data)
    data = df.ix[:, 0:1]  # 데이터
    label = df.ix[:, 2]  # 레이블

    ## 데이터 학습시키기 : fit(data, lebel)함수 활용위해 위 데이터 레블 분리
    clf = svm.SVC()
    clf.fit(data, label)

    ## 데이터 예측하기
    pred = clf.predict(data)
    print('예측 결과 :', pred)

    ## 옵션1. 결과 확인하기
    ok = 0
    total = 0

    for idx, answer in enumerate(label):
        p = pred[idx]
        if p == answer:
            ok += 1
        total += 1
    print('정답율 : ', ok, '//', total, ok/total)

    ## 옵션2  scikit.metrics() 메소드 이용 정답률 구하기
    ac_score = metrics.accuracy_score(label, pred)
    print("metrics의 정답율 : ", ac_score)

    #####################################################################################
    ###EX2. 붓꼿 CSV 데이터 읽어 들이기
    csv = []
    iris_file = "C:/Users/ilee/Documents/ref_linked/iris.csv"

    # # 옵션1. 기본형
    # with open(iris_file, 'r', encoding='utf-8') as fp:
    #     # 한줄씩 읽어 들이기
    #     for line in fp:
    #         line = line.strip()         # 줄바꿈 제거
    #         cols = line.split(',')      # 쉼표로 자르기
    #
    #         # 문자열 데이터를 숫자로 변환하기
    #         fn = lambda n: float(n) if re.match(r'^[0-9\.]+$', n) else n   # raw string 숫자로 시작\.
    #         cols = list(map(fn, cols))
    #         csv.append(cols)
    # print('irs:', csv)
    #
    # # 가장 앞 줄의 헤더 제거
    # del csv[0]
    #
    # # 데이터 셔플하기(섞기)
    # random.shuffle(csv)
    #
    # # 학습전용데이터 / 테스트전용데이터 분할(2:1비율)
    # total_len = len(csv)
    # train_len = int(total_len * 2 / 3)
    # train_data = []
    # train_label = []
    # test_data = []
    # test_label = []
    #
    # for i in range(total_len):
    #     data = csv[i][0:4]
    #     label = csv[i][4]
    #     if i < train_len:
    #         train_data.append(data)
    #         train_label.append(label)
    #     else:
    #         test_data.append(data)
    #         test_label.append(label)

    ### 옵션2. pandas 사용
    csv = pd.read_csv(iris_file)
    # 필요한 열 추출하기
    csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
    csv_label = csv["Name"]
    # 학습전용 // 테스트전용 데이터 나누기
    train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)


    # 데이터를 학습시키고 예측하기
    clf = svm.SVC()
    clf.fit(train_data, train_label)
    pred = clf.predict(test_data)

    # 정답률 구하기
    ac_score = metrics.accuracy_score(test_label, pred)
    print("정답율 : ", ac_score)

    return render(request, 'mLearn/exHome.html')


def mnist(request):
    savepath = "../mnist"  # 부모폴더(현재 mLeran의 부모 Tutorial급)
    baseurl = "http://yann.lecun.com/exdb/mnist"
    files = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz"]

    # 다운로드
    if not os.path.exists(savepath):
        os.mkdir(savepath)

    for f in files:
        url = baseurl + "/" + f
        loc = savepath + "/" + f
        print("download:", url)
        if not os.path.exists(loc):
            urllib.request.urlretrieve(url, loc)

    # GZip 압축 해제
    for f in files:
        gz_file = savepath + "/" + f
        raw_file = savepath + "/" + f.replace(".gz", "")

        with gzip.open(gz_file, "rb") as fp:
            body = fp.read()
            with open(raw_file, "wb") as w:
                w.write(body)

    print("ok")

    # binary to CSV 전환: to_csv() 호출 => ../mnist/train.csv  ../mnist/t10k,csv에 저장
    to_csv("train", 1000)
    to_csv("t10k", 500)

    # load csv : load_csv() 호출  => ../mnist/train.cav  ../mnist/t10k.csv를 불러 내여 처리
    data = load_csv("../mnist/train.csv")
    test = load_csv("../mnist/t10k.csv")

    # 학습하기
    clf = svm.SVC()
    clf.fit(data["images"], data["labels"])

    # 예측하기
    predict = clf.predict(test["images"])

    # 결과 확인하기 --- (※4)
    ac_score = metrics.accuracy_score(test["labels"], predict)
    cl_report = metrics.classification_report(test["labels"], predict)
    print("정답률 =", ac_score)
    print("리포트 =")
    print(cl_report)

    return render(request, 'mLearn/exHome.html')

def conversion(request):

    # Ex1)  Image(JPG) to CSV conversion

    fileList = createFileList('C:/Users/ilee/PycharmProjects/mLearn/mnist/')
    for file in fileList:
        print(file)
        img_file = Image.open(file)
        img_file.show()

        # get original image parameters...
        # width, height = img_file.size
        # format = img_file.format
        # mode = img_file.mode

        value = np.array(img_file)   # np 배열 생성
        img_list = value.tolist()    # list로 리턴
        print(img_list)

        # with open(fil_name + '.csv', 'w', newline='') as csvfile:
        with open("C:/Users/ilee/PycharmProjects/mLearn/mnist/img_pixels.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(img_list)


        # option#! Make image Greyscale
        # img_grey = img_file.convert('L')
        # value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
        # # img_grey.save('result.png')
        # img_grey.show()
        #
        # value = value.flatten()
        # print(value)
        # with open("C:/Users/ilee/PycharmProjects/mLearn/mnist/img_pixels.csv", 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(value)



    ##EX2) Binary to CSV

    # import urllib.request as req
    # import gzip, os, os.path

    savepath = "../mnist"   # 부모폴더(현재 mLeran의 부모 Tutorial급 ..pycharmProjects/mnist)
    baseurl = "http://yann.lecun.com/exdb/mnist"
    files = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz"]

    # 다운로드
    if not os.path.exists(savepath):
        os.mkdir(savepath)

    for f in files:
        url = baseurl + "/" + f
        loc = savepath + "/" + f

        if not os.path.exists(loc):
            urllib.request.urlretrieve(url, loc)

    # GZip 압축 해제
    for f in files:
        gz_file = savepath + "/" + f
        raw_file = savepath + "/" + f.replace(".gz", "")

        with gzip.open(gz_file, "rb") as fp:
            body = fp.read()
            with open(raw_file, "wb") as w:
                w.write(body)

    # binary to CSV 전환: to_csv() 호출 => ../mnist/train.csv  ../mnist/t10k,csv에 저장
    to_csv("train", 100)
    to_csv("t10k", 50)

    # load csv : load_csv() 호출  => ../mnist/train.cav  ../mnist/t10k.csv를 불러 내여 처리
    data = load_csv("../mnist/train.csv")
    test = load_csv("../mnist/t10k.csv")

    print('label:', data["labels"])
    print('image:', data["images"])

    # 학습하기
    clf = svm.SVC()
    clf.fit(data["images"], data["labels"])

    # 예측하기
    predict = clf.predict(test["images"])

    # 결과 확인하기 --- (※4)
    ac_score = metrics.accuracy_score(test["labels"], predict)
    cl_report = metrics.classification_report(test["labels"], predict)
    print("정답률 =", ac_score)
    print("리포트 =")
    print(cl_report)

    return render(request, 'mLearn/exHome.html')

def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

def to_csv(name, maxdata):
    import struct

    # 레이블 파일과 이미지 파일 열기
    lbl_f = open("../mnist/"+name+"-labels-idx1-ubyte", "rb")
    img_f = open("../mnist/"+name+"-images-idx3-ubyte", "rb")
    csv_f = open("../mnist/"+name+".csv", "w", encoding="utf-8")

    # 헤더 정보 읽기 --- (※1)
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols

    # 이미지 데이터를 읽고 CSV로 저장하기 --- (※2)
    res = []
    for idx in range(lbl_count):
        if idx > maxdata:
            break
        label = struct.unpack("B", lbl_f.read(1))[0]   # label의 binary to text 처리

        bdata = img_f.read(pixels)                      # binary 데이터 타입
        sdata = list(map(lambda n: str(n), bdata))     # image의 문자열 처리하여 리스트에 저장

        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")            # 문자열(",")에 조인함수(label, [image1. image2..])) \r\n 한줄 뛰움움

       # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기 -- (※3)
        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "../mnist/{0}-{1}-{2}.pgm".format(name,idx,label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)

    csv_f.close()
    lbl_f.close()
    img_f.close()

    return csv_f

def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2:
                continue

            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}




def lang(request):

    # 데이터 불러 들이기
    train = load_files("../mLearn/lang/train/*.txt")
    test = load_files("../mLearn/lang/test/*.txt")

    # txt파일을 json 파일로 전환후 저장
    with open("../mLearn/lang/freq.json", "w", encoding="utf-8") as fp:
        json.dump([train, test], fp)

    # 학습하기
    clf = svm.SVC()
    clf.fit(train["freqs"], train["labels"])

    # #check   # 학습 데이터 저장하기
    # joblib.dump(clf, "../mLearn/lang/freq.pkl")
    # print("학습 데이터 저장 ok")

    ## Ex1. test 데이터로 예측하기
    predict = clf.predict(test["freqs"])

    # 결과 확인하기 --- (※4)
    ac_score = metrics.accuracy_score(test["labels"], predict)
    cl_report = metrics.classification_report(test["labels"], predict)
    print("정답률 =", ac_score)
    print("리포트 =")
    print(cl_report)

    ##Ec2.  학습 데이터(preq 결과(dictionary)) PLOT 하기
    with open("../mLearn/lang/freq.json", "r", encoding="utf-8") as fp:
        freq = json.load(fp)

    lang_dic = {}
    for idx, lbl in enumerate(freq[0]["labels"]):
        freq_list = freq[0]["freqs"][idx]

        if not (lbl in lang_dic):
            lang_dic[lbl] = freq_list
            continue

        for i, item in enumerate(freq_list):
            # lang_dic[lbl][i] = fq
            lang_dic[lbl][i] = (lang_dic[lbl][i] + item) / 2

    indexlist = [chr(n) for n in range(97, 97+26)]
    df = pd.DataFrame(lang_dic, index=indexlist)

    df.plot(kind='bar')
    # plt.show()

    # # ggplot방식 적용
    # plt.style.use('ggplot')
    # df.plot(kind="bar", subplots=True, ylim=(0, 0.15))

    plt.savefig("../mLearn/lang/lang_plot.png")

    ##Ex3.  실제 데이터를 이용한 예측(언어 선별)

    # 텍스트 데이터 입력 양식

    form = cgi.FieldStorage()

    text = form.getvalue("text", default="")
    msg = ""

    if text != "":
        lang = detect_lang(text)
        msg = "판정결과=" + lang

    show_form(text,msg)

    return render(request, 'mLearn/exHome.html')


def show_form(text, msg=""):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
        <html><body><form>
        <textarea name="text" rows="8" cols="40">{0}</textarea>
        <p><input type="submit" value="판정"></p>
        <p>{1}</p>
        </form></body></html>
    """.format(cgi.escape(text), msg))

def detect_lang(text):
    # 알파벳 출현 빈도 구하기
    text = text.lower()

    # 숫자 세기 변수(cnt) 초기화하기
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a")
    code_z = ord("z")

    # 알파벳 출현 횟수 구하기 -
    for ch in text:
        n = ord(ch)

        if code_a <= n <= code_z:  # a~z 사이에 있을 때
            cnt[n - code_a] += 1

    # 정규화하기
    total = sum(cnt)
    if total == 0: return "입력이 없습니다"
    freq = list(map(lambda n: n / total, cnt))

    # 학습 데이터 읽어 들이기
    # pklfile = os.path.dirname(__file__) + "/freq.pkl"

    pklfile = "../mLearn/lang/freq.pkl"
    clf = joblib.load(pklfile)

    pred = clf.predict([freq])
    print(pred)

    lang_dic = {
        "en": "영어",
        "fr":"프랑스어",
        "id": "인도네시아어", 
        "tl": "타갈로그어"
    }
    
    return lang_dic[pred[0]]

def load_files(path):
    labels = []
    freqs = []

    file_list = glob.glob(path)              # 지정한 디렉토리에서의 파일 리스트(dir)
    for fname in file_list:
        # print('fname:'+fname)
        resp = check_freq(fname)
        # print('resp:'+str(resp))

        freqs.append(resp[0])
        labels.append(resp[1])

    return {"labels": labels, "freqs": freqs }

def check_freq(fname):

    name = os.path.basename(fname)
    # print('name:'+name)
    lang = re.match(r"^[a-z]{2,}", name).group()     #  raw String으로 영어 소문자로 시작하고, 적어도 2개 글짜(영어소문자) 매칭이 되는 것으로 문자열 리턴
    # print(lang)

    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()                               # 전체를 읽어 나감
    text = text.lower()                                 # 소문자 변환

    # 숫자 세기 변수(cnt) 초기화하기
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a")
    code_z = ord("z")

    # 알파벳 출현 횟수 구하기 -
    for ch in text:
        n = ord(ch)

        if code_a <= n <= code_z:                # a~z 사이에 있을 때
            cnt[n - code_a] += 1

    # 정규화하기
    total = sum(cnt)
    # print('total:'+str(total))
    freq = list(map(lambda n: n / total, cnt))
    # print('freq:'+str(freq))
    return (freq, lang)

def langTest(request):

    if request.method == 'POST':

        text = request.POST['text']
        lang = detect_lang(text)

        data = {
            'text': text,
            'lang': lang,
        }
    else:
        data = {
            'lang': "lang",
        }

    return render(request, 'mLearn/langTestForm.html', data)

def bmi_check(h, w):
    bmi = w/(h/100)**2
    if bmi<18.5:
        return "thin"
    if bmi<25:
        return "normal"
    return "fat"

def fat(request):

    #1 bmi 데이터 창출 및 저장(csv)
    # fp = open("../mLearn/bmi.csv", "w", encoding="utf-8")
    # fp.write("height,weight,label\r\n")
    #
    # cnt = { "thin": 0, "normal": 0, "fat": 0 }
    #
    # for i in range(20000):
    #     h = random.randint(120, 200)
    #     w = random.randint(45, 100)
    #     label = bmi_check(h, w)
    #     cnt[label] += 1
    #
    #     fp.write("{0},{1},{2}\r\n".format(h, w, label))
    #
    # fp.close()

    with open("../mLearn/bmi.csv", "w", encoding="utf-8") as fp:
        fp.write("height,weight,label\r\n")

        cnt = {"thin": 0, "normal": 0, "fat": 0}

        for i in range(20000):
            h = random.randint(120, 200)
            w = random.randint(45, 100)
            label = bmi_check(h, w)
            cnt[label] += 1

            fp.write("{0},{1},{2}\r\n".format(h, w, label))


    print('cnt:', cnt)

    #2 bmi csv 데이터를 pandas로 읽어들이고(pd.read_csv) dataframe 형태로 -> label, data 데이터로 정규화해서 구하기
    pdData = pd.read_csv("../mLearn/bmi.csv")

    w = pdData["weight"]/100   # 몸무게는 최대 100kg 가정
    h = pdData["height"]/200  # 키는 최고 200cm 가정
    label = pdData["label"]
    wh = pd.concat([w, h], axis=1)
    # print('wh:', wh)

    data_train,  data_test, label_train, label_test = train_test_split(wh, label)

    #3 데이터 학습
    clf = svm.SVC()
    clf.fit(data_train, label_train)

    #4 데이터 예측하기
    predict = clf.predict(data_test)

    #5 결과 테스트
    ac_score = metrics.accuracy_score(label_test, predict)
    cl_report = metrics.classification_report(label_test, predict)
    print("정답률 =", ac_score)
    print("리포트 =")
    print(cl_report)

    #6 데이터 분포 PLOT 그리기
    # pdData = pd.read_csv("../mLearn/bmi.csv")
    # pdData.plot()
    # pdData["label"]

    # Pandas로 CSV 파일 읽어 들이기
    tbl = pd.read_csv("../mLearn/bmi.csv", index_col=2)
    # 그래프 그리기 시작(하나의 sub plot - axes)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
    def scatter(lbl, color):
        b = tbl.loc[lbl]
        ax.scatter(b["weight"], b["height"], c=color, label=lbl)

    scatter("fat", "red")
    scatter("normal", "yellow")
    scatter("thin", "purple")
    ax.legend()

    plt.savefig("../mLearn/bmi.png")
    # plt.show()

    return render(request, "mLearn/exHome.html")

def mushroom(request):

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
    savename = "../mLearn/mushroom.csv"
    urllib.request.urlretrieve(url, savename)

    mushroom = pd.read_csv("../mLearn/mushroom.csv")

    # 내부의 기호를 숫자로 변환
    label = []
    data = []

    for idx, row in mushroom.iterrows():
        label.append(row.ix[0])

        row_data = []
        for v in row.ix[1:]:
            row_data.append(ord(v))
        data.append(row_data)

    data_train, data_test, label_train, label_test = train_test_split(data, label)

    # 3 데이터 학습
    clf = RandomForestClassifier()
    clf.fit(data_train, label_train)

    # 4 데이터 예측하기
    predict = clf.predict(data_test)

    # 5 결과 테스트
    ac_score = metrics.accuracy_score(label_test, predict)
    cl_report = metrics.classification_report(label_test, predict)
    print("정답률 =", ac_score)
    print("리포트 =")
    print(cl_report)

    return render(request, "mLearn/exHome.html")

def tensor(request):

    # # 상수 정의
    # a = tf.constant(1234)
    # b = tf.constant(45)
    # add_op = a + b
    #
    # # session 설정
    # sess = tf.session()
    # resp = sess.run(add_op)
    # print(resp)

    return render(request, "mLearn/exHome.html")

##For TEST ##############################################################

def mLearnTest(request):
    ###############################

    print('home:', os.path.expanduser('~'))




    ####################################
    return render(request, 'mLearn/exHome.html')

###End TEST#########################################################################