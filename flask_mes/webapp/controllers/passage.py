from flask import Blueprint,render_template,session,g
from os import path
from flask import redirect,url_for
import datetime,math

passage = Blueprint('passage',__name__,template_folder=path.join(path.pardir,'templates'))

@passage.route('/',methods=["GET"])
@passage.route('/<int:page>/',methods=["GET"])
def home(page=1):
    from ..models import Post, User
    users = []
    maxpage =math.ceil(Post.query.count()/5)
    posts =Post.query.order_by(Post.p_date.desc()).paginate(page,5)
    for post in posts.items:
        users.append(User.query.get(post.userid).username)
    return render_template('index.html',posts = posts,users = users,page = page,maxpage = maxpage)



@passage.route('/publish/',methods=["GET","POST"])
def publish():
    from ..forms import Publish
    from ..models import Post,db
    if not g.current_user:
        return render_template('publish.home')
    form = Publish()
    if form.validate_on_submit():
        new_post = Post(form.title.data)
        new_post.userid = g.current_user.id
        new_post.text = form.text.data
        new_post.p_date = datetime.datetime.now()
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('user.private',uid= g.current_user.id, page=1))
    return render_template('publish.html',form=form)

@passage.route('/delete/<int:id>/',methods=["GET"])
def delete(id):
    from ..models import Post,db
    post=Post.query.get(id)
    if g.current_user.id != post.userid:
        abort(403)
    else:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('passage.home'))


@passage.before_request
def check_user():
    from ..models import User
    if 'username' in session:
        g.current_user = User.query.filter_by(username=session['username']).one()
    else:
        g.current_user = None
