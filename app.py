from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# 쿨SMS API 정보 (발신번호는 반드시 쿨SMS에 등록된 번호로 바꿔주세요)
API_KEY = 'NCSNJWYSDPSBJDY2'
API_SECRET = 'JNDC10JIYQXEKHW1PBTHDWNBLQ3MU8NM'
FROM_NUMBER = '01000000000'  # 쿨SMS 발신번호 등록된 번호
TO_NUMBER = '01098330912'    # 수신자 번호 (본인 번호)


def send_sms(name, phone):
    url = 'https://api.coolsms.co.kr/messages/v4/send'
    headers = {
        'Authorization': f'HMAC {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        'messages': [{
            'to': TO_NUMBER,
            'from': FROM_NUMBER,
            'text': f'[보험상담신청]\n이름: {name}\n전화번호: {phone}'
        }]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print('문자 전송 성공:', response.json())
    except Exception as e:
        print('문자 전송 실패:', e)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    print(f'상담 신청 - 이름: {name}, 전화번호: {phone}')
    send_sms(name, phone)
    return redirect(url_for('complete'))


@app.route('/complete')
def complete():
    return render_template('complete.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
