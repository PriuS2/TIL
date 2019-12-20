#
import requests
import bs4

# 이 주소로 요청을 보내면 응답으로 html 파일이 도착할것
html = requests.get('https://m.stock.naver.com/marketindex/item.nhn?marketindexCd=FX_USDKRW&menu=exchange')

#print(html.text)

#html text를 내가 보기 좋게 접근할 수 있도록 변경
soup = bs4.BeautifulSoup(html.text, 'html.parser')
dollor = soup.select_one('#header > div.major_info_wrp.no_chart.no_code > div.major_info > div.stock_wrp > div > strong')
#totalCnt = 
print(dollor.text)
