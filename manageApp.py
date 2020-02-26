# encoding=utf8
from app.views import app
from app.models import User

for i in range(10):
    count = i +2
    sum = count + i
    
user = User('清月妖姬', 'qyyj@ai.com')
app.run('0.0.0.0',5000, debug=True)