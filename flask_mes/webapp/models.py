from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(255))
    passwd = db.Column(db.String(255))
    posts = db.relationship('Post',backref = 'user', lazy = 'dynamic')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "User <{}>".format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'))
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    p_date = db.Column(db.DateTime())
    
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "Post <{}>".format(self.title)
