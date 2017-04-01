from flask import Blueprint,render_template, url_for,redirect, flash,session,g
from webapp.forms import Regform, Loginform,Length
from . import passage
import math

user = Blueprint('user',__name__,template_folder='../templates')

@user.route('/register/',methods=["GET","POST"])
def reg():
    from webapp.models import User
    from ..models import db
    form = Regform()
    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.passwd = form.passwd.data
        db.session.add(new_user)
        db.session.commit()
        flash('You have been registered',category='success')
        session['username']=form.username.data
        return redirect(url_for('passage.home'))
    return render_template('register.html',form = form)

@user.route('/login/',methods=["GET","POST"])
def login():
    form = Loginform()
    if form.validate_on_submit():
        session['username']=form.username.data
        return redirect(url_for('passage.home'))
    return render_template('login.html',form = form)

@user.route('/logout/',methods=["GET","POST"])
def logout():
    session.pop('username',None)
    return redirect(url_for('passage.home'))

@user.route('/user/<int:uid>/<int:page>',methods=["GET"])
def private(uid,page=1):
    from webapp.models import Post,User
    maxpage =math.ceil(Post.query.filter_by(userid=uid).count()/5)
    posts = Post.query.filter_by(userid=uid).order_by(Post.p_date.desc()).paginate(page,5)
    user = User.query.get(uid).username
    return render_template('people.html',posts = posts,user = user,page = page,maxpage = maxpage)

@user.before_request
def check_user():
    from webapp.models import User
    if 'username' in session:
        g.current_user = User.query.filter_by(username=session['username']).one()
    else:
        g.current_user = None
        
