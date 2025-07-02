from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    
    # 여기서 문자 API를 호출하는 코드를 넣을 수 있어요.
    # 일단은 그냥 확인용으로 출력해 봅니다.
    print(f"상담 신청 - 이름: {name}, 전화번호: {phone}")
    
    return redirect('/complete')

@app.route('/complete')
def complete():
    return "<h2>상담 신청이 완료되었습니다! 곧 연락드리겠습니다.</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
