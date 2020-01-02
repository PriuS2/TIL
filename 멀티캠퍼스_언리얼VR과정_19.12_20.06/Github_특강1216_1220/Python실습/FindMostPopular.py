import requests
import bs4

html = requests.get('https://www.naver.com')
soup = bs4.BeautifulSoup(html.text, 'html.parser')

selector = 'span.ah_k'
keywords = soup.select(selector)

keywords = [i.text for i in keywords[0:20]]

problem = sorted(keywords)

print('아래의 보기 중에서 1위를 고르세요')
print(problem)
answer = input('당신이 입력한 답: ')

if(answer == keywords[0]):
    print("정답")
else:
    print("틀림")