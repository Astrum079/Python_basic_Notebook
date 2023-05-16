#다음뉴스 목록 페이지에서 여러건의 뉴스(제목+본문) 수집
import requests
from bs4 import BeautifulSoup
from daum_news_fnc import get_news_title_and_content
for i in range(1,11):
    print(f"{i} page ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    url=f"https://news.daum.net/breakingnews/digital?page={i}"  #뉴스 목록 url

    #뉴스 목록 url에서 1건의 뉴스 url 추출
    result = requests.get(url)  #해당 url의 전체 소스코드 get
    soup = BeautifulSoup(result.text,"html.parser")  #전체 소스코드 BS4 읽기
    title_list = soup.select("ul.list_news2 a.link_txt")  #BS4로 뉴스제목 목록 추출

    for j, tag in enumerate(title_list):
        new_url = tag["href"]
        title,content=get_news_title_and_content(new_url)
        print("=" * 100)
        print(f"{(i-1)*15+j+1} 뉴스 제목 : {title}")  # 나는 바로 계산때리긴 했는데
                                                     # 기사 하나 긁어올때마다 변수값 1씩 증가시키는 방법도 있다고 한다
        print("=" * 100)
        print(f"뉴스 본문 : {content}")