from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(db.Model,UserMixin):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    reviews = db.relationship('Review',backref = 'users',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_passwords(self, password):
        return check_password_hash(self.pass_secure, password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User {self.username}'
        
class Role(db.Model):
    __tablename__ ='roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user = db.relationship('User',backref='roles',lazy="dynamic")
    
    def __repr__(self):
        return f'User {self.name}'


class Movie:
    '''
    Movie class to define Movie Objects
    '''
    
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        
class Review(db.Model):
    __tablename__='reviews'
        
    all_reviews = []
    
    def __init__(self, movie_id, movie_title, image_path, review, user_id):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.image_path = image_path
        self.movie_review = review
        self.user_id=user_id
        
    def save_reviews(self):
        db.session.add(self)
        db.session.commit()
                
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
        
    @classmethod
    def get_reviews(cls,id):
        reviews=Review.query.filter_by(movie_id=id).all()
        return reviews

    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

