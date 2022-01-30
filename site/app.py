from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/introduce')
def introduce():
    return render_template('introduce.html')

@app.route('/subject_wiki')
def subject_wiki():
    return render_template('subject_wiki.html')

@app.route('/notice_board')
def notice_board():
    return render_template('notice_board.html')

@app.route('/event_wiki')
def event_wiki():
    return render_template('event_wiki.html')

if __name__ == '__main__':
    app.run(debug=True)