from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# 메일 발송 함수
def send_email(subject, body, to_email):
    from_email = "01098330912a@gmail.com"   # 보내는 이메일
    password = "xqwrpvghbqjggzgz"            # 앱 비밀번호 (공백 없이!)

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        print("이메일 전송 성공!")
    except Exception as e:
        print("이메일 전송 실패:", e)

# 라우팅
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    phone = request.form["phone"]
    subject = "보험 상담 신청"
    body = f"상담 신청 - 이름: {name}, 전화번호: {phone}"
    
    # 이메일로 전송
    send_email(subject, body, "a76567368@gmail.com")

    return redirect("/complete")

@app.route("/complete")
def complete():
    return render_template("complete.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
