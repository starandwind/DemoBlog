from flask import Flask, url_for, redirect
from .controllers.users import user
from .controllers.passage import passage
from .models import db


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)

    app.register_blueprint(user)
    app.register_blueprint(passage)


    @app.route('/',methods=["GET"])
    def index():
        return redirect(url_for('passage.home'))

    return app

if __name__=='__main__':
    app.run()
