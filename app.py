from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(subject, body, to_email):
    from_email = "01098330912a@gmail.com"       # 보내는 이메일 (당신 이메일)
    password = "Qnals112!!@"       # Gmail 앱 비밀번호 입력

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

@app.route('/')
def index():
    return render_template('index.html')  # 인덱스 페이지

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')

    subject = "보험 상담 신청 알림"
    body = f"상담 신청이 접수되었습니다.\n\n이름: {name}\n전화번호: {phone}"

    send_email(subject, body, "a76567368@gmail.com")  # 상담 내용을 받을 이메일

    return redirect('/complete')

@app.route('/complete')
def complete():
    return render_template('complete.html')  # 완료 페이지

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
