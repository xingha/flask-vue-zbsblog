#encoding=utf8
from app import app


@app.route('/', methods=['POST','GET'])
def index():
    return '<h1/>Hi Grils</h1>'

