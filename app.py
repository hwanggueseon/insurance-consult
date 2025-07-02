from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 쿨SMS API 정보 입력
API_KEY = 'NCSNJWYSDPSBJDY2'
API_SECRET = 'JNDC10JIYQXEKHW1PBTHDWNBLQ3MU8NM'
TO_PHONE = '01098330912'  # 당신의 수신번호

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')

    # 문자 보내기
    message = f"[상담신청] 이름: {name}, 연락처: {phone}"
    send_sms(TO_PHONE, message)

    return render_template('complete.html')

def send_sms(to, text):
    url = 'https://api.coolsms.co.kr/messages/v4/send'
    headers = {
        'Authorization': f'Basic {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json'
    }
    data = {
        'message': {
            'to': to,
            'from': '01000000000',  # 쿨SMS에 등록된 발신번호로 바꿔야 함
            'text': text
        }
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        print(response.status_code, response.json())
    except Exception as e:
        print("문자 전송 실패:", e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
