import json
import pandas as pd
#파일명
file_name = 'busan_minwon_10450_2.json'

#데이터 적재를 위한 배열
id = []
title = []
content = []
Class = []

#JSON 파일 읽기
with open(file_name, "r", encoding="UTF-8-sig", newline="\n") as f:
    json_data = json.loads((f.readline()))
    df = pd.DataFrame(columns=['id', 'title', 'content'])
    #민원 분류하기
    for i in range(0, len(json_data)):
        id.append(json_data[i]['id'])
        title.append(str(json_data[i]['title']))
        content.append(json_data[i]['cont'].replace("내용", "").replace("\t", ""))
        if title[i] == "답변입니다":
            Class.append("답변")
        elif ("거부" in title[i]) or ("거부" in content[i]):
            Class.append("불친절")
        elif "칭찬합니다" in title[i]:
            Class.append("친절")
        elif ("신고합니다" in title[i]) or ("조사" in title[i]) or ("신고합니다" in content[i]):
            Class.append("신고")
        elif ("요청" in title[i]) or  ("건의" in title[i]) or ("요청" in content[i]) or ("건의" in content[i]) :
            Class.append("건의")
        elif("?" in title[i]) or ("?" in content[i]):
            Class.append("문의")
        else:
            Class.append("기타")

#CSV 파이로 저장
import csv
with open('Busan_Inquiry.csv', "w", encoding="UTF-8-sig", newline="\n") as csv_f:
    writer = csv.DictWriter(csv_f, fieldnames=["id", "title", "content", "Class"])
    #필드 삽입
    writer.writeheader()
    #데이터 CSV파일 저장
    for i in range(0, 5450):
        writer.writerow({"id": id[i], "title":title[i], "content": content[i], "Class":Class[i]})
