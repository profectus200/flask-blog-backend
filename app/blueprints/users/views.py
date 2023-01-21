from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app import menu, db, login_manager
from app.blueprints.profiles.models import Profiles
from app.blueprints.users.forms import LoginForm, RegisterForm
from app.blueprints.users.models import Users

users = Blueprint('users', __name__, template_folder='app/templates', static_folder='app/static')


@login_manager.user_loader
def load_user(user_id):
    return Users().fromDB(user_id, db)


@users.route('/register', methods=('POST', 'GET'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            hashed_psw = generate_password_hash(form.psw.data)
            user = Users(email=form.email.data, psw=hashed_psw)

            db.session.add(user)
            db.session.flush()

            profile = Profiles(name=request.form['name'], age=request.form['age'], city=request.form['city'],
                               user_id=user.id)

            db.session.add(profile)
            db.session.commit()
        except:
            db.session.rollback()

        return redirect(url_for('index'))

    return render_template('register.html', title='Registration', form=form)


@users.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter(Users.email == form.email.data).first()
        if user and check_password_hash(user['psw'], form.psw.data):
            user_login = Users().create(user)
            data = form.remember.data
            login_user(user_login, remember=data)
            return redirect(request.args.get('next') or url_for('profile'))

        flash('Неверная пара логин/пароль', 'error')

    return render_template('login.html', menu=menu, title='Authorization', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logout', 'success')
    return redirect(url_for('login'))
