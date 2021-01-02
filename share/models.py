from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    lists = relationship("MovieList")
    profile = relationship("Profile")


class Profile(db.Model):
    __tablename__ = "api_profile"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("auth_user.id"))
    user = relationship("User", uselist=False, back_populates="profile")


class Movie(db.Model):
    __tablename__ = "api_movie"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    about = Column(Text)
    poster = Column(String)

    def __repr__(self):
        return "<Movie %r>" % self.title


class MovieList(db.Model):
    __tablename__ = "api_movielist"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    liked_by = Column(Integer)
    owner_id = Column(Integer, ForeignKey("auth_user.id"))

    def __repr__(self):
        return "<MovieList %r>" % self.name