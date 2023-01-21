from flask import Blueprint, render_template, make_response, request, flash, redirect, url_for, current_app
from flask_login import login_required, current_user

from app import menu, db
from app.blueprints.profiles.models import Profiles

profiles = Blueprint('profiles', __name__, template_folder='app/templates/profiles', static_folder='app/static/profiles')


@profiles.route('/profile')
@login_required
def profile():
    return render_template('profile.html', menu=menu, title='Profile')


@profiles.route('/user_avatar')
@login_required
def user_avatar():
    img = Profiles.query.filter(Profiles.user_id == current_user.id).first()
    if not img:
        with current_app.open_resource(current_app.root_path + url_for('static', filename='images/default.png'),
                                       'rb') as file:
            img = file.read()

    response = make_response(img)
    response.headers['Content-Type'] = 'image/jpg'
    return response


@profiles.route('/upload_avatar', methods=['POST', 'GET'])
@login_required
def upload_avatar():
    def verify_ext(filename):
        ext = filename.rsplit('.', 1)[1]
        if ext == 'jpg' or ext == 'JPG':
            return True
        return False

    if request.method == 'POST':
        file = request.files['file']
        if file and verify_ext(file.filename):
            try:
                img = file.read()
                current_profile = Profiles.query.filter(Profiles.user_id == current_user.id).first()
                current_profile.avatar = img

                db.session.commit()
                flash('Avatar successfully updated', 'success')
            except:
                db.session.rollback()
                flash('Avatar updating error', 'error')
        else:
            flash('Avatar uploading error', 'error')

    return redirect(url_for('profile'))
