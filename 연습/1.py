from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True)
    

#http://127.0.0.1:5000/ 로 들어 가면 Hello, World!가 나오는 것을 확인할 수 있음.