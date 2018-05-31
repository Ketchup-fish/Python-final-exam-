#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    comments = [
        {
            'user':u'知了课堂',
            'content':'XXXX'
        },
        {
            'user':u'黄勇',
            'content':'XXXX'
        }
    ]
    return render_template('index.html',comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
