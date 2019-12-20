from flask import Flask, request
import requests

#pip install python-decouple
from decouple import config

app = Flask(__name__)


#token = '1023745417:AAFId8WOdNs08DuaCx073rQURCLtuKfVZbQ'
# https://api.telegram.org/bot<token>/METHOD_NAME

token = config('TOKEN')
chat_id = config('CHAT_ID')
apiUrl = f'https://api.telegram.org/bot{token}/'
#chat_id = '906918498'

#파파고
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')



# my id : 906918498
# getUpdates


@app.route('/')
def hello():
    return 'hello world'

#METHOD_NAME : sendMessage
@app.route('/send/<text>')
def send(text):
    req = f'{apiUrl}sendMessage?chat_id={chat_id}&text={text}'
    res = requests.get(req)
    return req + "\n\n" + res.text 

@app.route('/chatbot', methods=['POST'])
def chatbot():
    from_telegram = request.get_json()
    chat_id = from_telegram.get('message').get('from').get('id')
    chat_text = from_telegram.get('message').get('text')
    
    #req = f'{apiUrl}sendMessage?chat_id={chat_id}&text={chat_text}'
    #res = requests.get(req)
    

    if chat_text[0:3]=='@번역':
        



    return 'ok', 200
    # status code 200 ->  ok 잘 접수했다. (내서버 -> 텔레그램 서버)




app.run(debug=True)

