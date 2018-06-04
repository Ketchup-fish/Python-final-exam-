#encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/test?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#db = SQLALchemy(app)
#db.create_all()
@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
