#
import requests
import bs4

# 이 주소로 요청을 보내면 응답으로 html 파일이 도착할것
html = requests.get('https://blog.naver.com/tjseh0091')

print(html.text)

#html text를 내가 보기 좋게 접근할 수 있도록 변경
soup = bs4.BeautifulSoup(html.text, 'html.parser')
todayCnt = soup.select_one('#blog-counter > p.today > span.cnt1')
#totalCnt = 
print(todayCnt.text)

