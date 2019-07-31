import time, uuid

from app.ext import db

def next_id():
    #返回UUID，%015d表示用15宽度显示，不足15高位补0
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(db.Model):
    id = db.Column(db.String(100), primary_key=True, default = next_id)
    email = db.Column(db.String(120), unique=True, nullable=False) #email作用户名
    passwd = db.Column(db.String(50), nullable = False)
    created_at = db.Column(db.Float, default = time.time)

    #def __repr__(self):
        #return '<User %r>' % self.email

class Blog(db.Model):
    id = db.Column(db.String(100), primary_key=True, default = next_id)
    user_id = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), nullable=False)
    summary = db.Column(db.Text, nullable = True)
    content = db.Column(db.Text, nullable = False)
    created_at = created_at = db.Column(db.Float, default = time.time)