from flask_script import Manager, Server
from webapp.models import db, User, Post
from webapp import create_app


app=create_app('webapp.config.DevConfig')
manager = Manager(app)
manager.add_command("server", Server)

@manager.command
def setup_db():#you should first run this
    db.create_all()
    
@manager.shell
def make_shell_context():
    return dict(app = app, db=db, User=User,Post=Post)

if __name__ =='__main__':
    manager.run()

    
