from flask import Blueprint, flash, render_template, abort, request, redirect, url_for
from flask_login import login_required, current_user

from app import menu, db
from app.blueprints.posts.forms import AddPostForm
from app.blueprints.posts.models import Posts

posts = Blueprint('posts', __name__, template_folder='app/templates/posts', static_folder='app/static/posts')


@posts.route('/add_post', methods=['POST', 'GET'])
@login_required
def add_post():
    form = AddPostForm()
    if form.validate_on_submit():
        try:
            post = Posts(title=form.title.data, text=form.text.data, alias=form.alias.data)
            db.session.add(post)
            db.session.commit()

            flash('Pot added successfully', category='success')
        except:
            db.session.rollback()
            flash('Error while post adding', category='error')

    return render_template('add_post.html', menu=menu, title='Post adding')


@posts.route('/posts/<alias>', methods=['GET', 'DELETE'])
def show_post(alias):
    post = Posts.query.filter(alias == Posts.alias).first()
    if not post:
        abort(404)

    if current_user.is_authenticated and current_user.id == post.user_id and request.method == 'DELETE':
        try:
            db.session.remove(post)
            db.session.commit()
        except:
            db.session.rollback()
            return redirect(url_for('show_all_posts'))

    return render_template('post.html', menu=menu, title=post.title, post=post.text, date=post.date)


@posts.route('/')
def show_all_posts():
    post_list = Posts.query.order_by(Posts.date).all()

    return render_template('posts.html', menu=menu, list=post_list)
