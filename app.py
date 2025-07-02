from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

# 쿨SMS API 정보
API_KEY = '당신의_API_KEY_여기에'
API_SECRET = '당신의_API_SECRET_여기에'
TO_NUMBER = '01098330912'       # 당신이 문자 받을 번호
FROM_NUMBER = '01098330912'   # 쿨SMS에 등록한 발신번호

def send_sms(name, phone):
    message = f"📥 보험 상담 신청\n이름: {name}\n전화번호: {phone}"

    url = 'https://api.coolsms.co.kr/messages/v4/send'
    headers = {
        'Authorization': f'HMAC {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json'
    }
    data = {
        'message': {
            'to': TO_NUMBER,
            'from': FROM_NUMBER,
            'text': message
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print("문자 전송 결과:", response.status_code, response.text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    send_sms(name, phone)
    return redirect('/complete')

@app.route('/complete')
def complete():
    return render_template('complete.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
