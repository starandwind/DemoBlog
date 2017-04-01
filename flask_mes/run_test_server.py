from webapp.models import db, User
from webapp import create_app

app = create_app('webapp.config.TestConfig')
db.app = app
db.drop_all()
db.create_all()
user=User('testlogin')
user.passwd = 'testpasswd'
db.session.add(user)
db.session.commit()
app.run()


