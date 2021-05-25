from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
from webdriver_manager.chrome import ChromeDriverManager


# 페이지 진입 > 제목별 진입 > 제목 & 내용 크롤링

navercld_list = []
title_list = []
cnt_list = []

# 페이지를 for문으로 돌림
# 페이지 for 문으로 돌리기, 27 페이지


driver = webdriver.Chrome('./chromedriver')
# 크롬 드라이버 설치
# driver = webdriver.Chrome(ChromeDriverManager().install())


# 제목별 진입 > 제목 & 내용 크롤링 > 다음 페이지로 넘어가기

driver.get('https://www.ncloud.com/support/notice/all2')
time.sleep(1)

# 원랜 27페이지, 5버튼 클릭위해서 임시로

for page in range(1, 27):
    url = driver.current_url
    print(url)
    driver.get(str(url))
    time.sleep(1)

# 5페이지 단위마다 페이지 목록 갱신(> 버튼 클릭)
    if page % 5 != 0:

        # 현재 페이지의 url 받아오기

# 공지문 제목별로 클릭
        for i in range(1, 10):

        # articleClass =
        # driver.find_element_by_xpath('//*[@id="notice_tab1"]/div/table/tbody/tr['+str(i)+"]/td[3]/a").text
        # print(articleClass)
        # driver.get('https://gov.toast.com/kr/support/notice')
        # time.sleep(0.7)

        # 기사글 클릭
            articleBtn = driver.find_element_by_css_selector(
                '#app > article > div.center-wrap > div:nth-child(3) > section > div:nth-child(1) > div:nth-child(' + str(i) + ') > a')
            articleBtn.click()
            time.sleep(0.8)

    # 제목
            title = driver.find_element_by_css_selector(
                '#app > article > div.center-wrap > div:nth-child(3) > section > div.basic > div > p.search_title').text
            print(title)

    # 내용
            cnt = driver.find_element_by_css_selector(
                '#app > article > div.center-wrap > div:nth-child(3) > section > div.content.search_content').text

    # 내용이 잘 담겼는지 확인
            print(cnt)

    # 닥셔너리에 제목, 내용 key-value로 담기
    # Class.append(articleClass)
            title_list.append(title)
            cnt_list.append(cnt)

    # driver.back()
    # 목록페이지로 이동(이전 페이지로 이동)
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
    # 다음페이지로 이동
        driver.find_element_by_css_selector(
            '#app > article > div.center-wrap > div:nth-child(3) > section > div:nth-child(2) > a:nth-child(' + str(page + 2)).click()
        time.sleep(0.8)


    else:
    # 현재 페이지의 url 받아오기

        driver.find_element_by_css_selector('#app > article > div.center-wrap > div:nth-child(3) > section > div:nth-child(2) > a:nth-child(8)')
# 공지문 제목별로 클릭
        for i in range(1, 10):

        # articleClass =
        # driver.find_element_by_xpath('//*[@id="notice_tab1"]/div/table/tbody/tr['+str(i)+"]/td[3]/a").text
        # print(articleClass)
        # driver.get('https://gov.toast.com/kr/support/notice')
        # time.sleep(0.7)

        # 기사글 클릭
            articleBtn = driver.find_element_by_css_selector(
            '#app > article > div.center-wrap > div:nth-child(3) > section > div:nth-child(1) > div:nth-child(' + str(i) + ') > a')
            articleBtn.click()
            time.sleep(0.8)

    # 제목
            title = driver.find_element_by_css_selector(
            '#app > article > div.center-wrap > div:nth-child(3) > section > div.basic > div > p.search_title').text
            print(title)

    # 내용
            cnt = driver.find_element_by_css_selector(
            '#app > article > div.center-wrap > div:nth-child(3) > section > div.content.search_content').text

    # 내용이 잘 담겼는지 확인
            print(cnt)

    # 닥셔너리에 제목, 내용 key-value로 담기
    # Class.append(articleClass)
            title_list.append(title)
            cnt_list.append(cnt)

    # driver.back()
    # 목록페이지로 이동(이전 페이지로 이동)
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
    # 다음페이지로 이동
        driver.find_element_by_css_selector(
        '#app > article > div.center-wrap > div:nth-child(3) > section > div:nth-child(2) > a:nth-child(' + str(page + 2)).click()
        time.sleep(0.8)

#####

print(title_list)
print(cnt_list)

import csv
# csv 파일로 만들기
with open("./navercld_data.csv", "w", encoding="UTF-8-sig", newline="\n") as f:
    writer = csv.DictWriter(f, fieldnames={"No", "Title", "Content"})
    writer.writeheader()
    for i in range(0, len(title_list)):
        navercld_list = {"No": len(title_list) - i,
                      "Title": title_list[i], "Content": cnt_list[i]}
        writer.writerow(navercld_list)
#
