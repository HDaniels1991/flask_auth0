from flask_app import db, login_manager, auth0_blueprint
from flask_login import UserMixin, current_user
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250),unique=True)
    email = db.Column(db.String(250),unique=True)

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
