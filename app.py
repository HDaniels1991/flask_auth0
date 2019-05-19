import os
import urllib
from flask import url_for, render_template, redirect, session
from flask_login import current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound
from flask_app import app, auth0_blueprint
from flask_app.models import *

#############################################
##############AUTH0 CONFIG###################
#############################################

auth0_blueprint.storage = SQLAlchemyStorage(OAuth, db.session, user=current_user, user_required=False)

@app.route('/auth0')
def auth0_login():
    if not auth0_blueprint.session.authorized:
        return redirect(url_for('auth0.login'))
    account_info = auth0_blueprint.session.get('userinfo')
    account_info_json = account_info.json()
    return '<h1>Your email is: {}</h1>'.format(account_info_json['name'])

@oauth_authorized.connect_via(auth0_blueprint)
def auth0_logged_in(blueprint, token):
    account_info = blueprint.session.get("userinfo")
    if account_info.ok:
        account_info_json = account_info.json()
        print(account_info_json)
        username = account_info_json['name']
        email = account_info_json['email']
        query = User.query.filter_by(username=username)
        try:
            user = query.one()
        except NoResultFound:
            user = User(username=username,email=email)
            db.session.add(user)
            db.session.commit()
        login_user(user)

#############################################

@app.route('/logout')
#@login_required
def logout_auth0():
    # Clear session stored data
    logout_user()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('index', _external=True), 'client_id': os.getenv('auth0_client_id')}
    return redirect(auth0_blueprint.base_url + '/v2/logout?' + urllib.parse.urlencode(params))

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=False)
