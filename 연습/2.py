from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/user')
def user():
    return 'Hello, User!'
if __name__ == '__main__':
    app.run(debug=True)
    
# http://127.0.0.1:5000/ 로 접속할 때 '/' or '/home'으로 끝나면 Hello, World!가 출력되는 것을 확인 가능 
# '/user'로 끝나면 'Hello, User!'가 출력되는 것을 확인할 수 있음.