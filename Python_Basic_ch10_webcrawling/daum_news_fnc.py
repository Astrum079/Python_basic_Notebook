#함수
#input:url
#output:제목 본문

#기존 : 제목함수, 본문함수
# -> 이유 : 함수 만들때 함수 하나에 여러 기능 넣기 X

import requests
from bs4 import BeautifulSoup

def get_news_title_and_content(url):


    result=requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")

    content = ""  #전체 본문을 담을 변수
#    contents.pop(-2)
#    contents.pop(-1)
    for tag in contents:
        content += tag.get_text()
    print(f"뉴스 본문 : {content}")

    return title,content