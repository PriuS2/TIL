from flask import Flask, escape, request, render_template
import random
import requests
import json

#app = Flask(__name__, static_folder='static',  static_url_path='')
app = Flask(__name__, static_folder='templates', static_url_path='')

#1
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

#2
@app.route('/myname')
def myname():
    return '박선도입니다'

#3
@app.route('/lunch')
def lunch():
    menus = ['111', '222', '333', '444']
    lunch = random.choice(menus)
    return lunch

#4
@app.route('/idol')
def Idol():
    idol = {
        'AAA' : {
            '111' : 1,
            '222' : 2,
        },
        'BBB' : {
            '333' : 333,
            '444' : 444
        },
        'CCC' : ['111', '222', '333']
    }
    return idol

#5
@app.route('/post/<int:num>')
def post(num):
    posts = ['0번 포스트', '1번 포스트', '2번 포스트']
    return posts[num]

#6
# 실습 cube뒤에 전달된 수의 세제곱 수를 화면에 보여주세요
@app.route('/cube/<int:num>')
def cube(num):
    return str(num**3)

#7
# 클라이언트에게 html 파일을 주고싶어요
@app.route('/html')
def html():
    return render_template('index.html')

#8
@app.route('/ping')
def pint():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html=age)

#로또 번호를 가져와서 보여주는 서버
@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    result = requests.get(url).json()

    winner = []
    for i in range(1,7):
        winner.append(result.get(f'drwtNo{i}')) #없는거 찾으면 null로 나옴
        # winner.append(result[f'drwtNo{i}']) //없는거 찾으면 에러남
    winner.append(result.get('bnusNo'))

    
    return json.dumps(winner)


app.run(debug=True)