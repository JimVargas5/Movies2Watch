#Jim Vargas
#This is a little database thing for me to keep track of the movies
#and TV shows that I want to watch

from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
#TODO
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'poop'

class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    release_date = db.Column(db.Integer)
    #TODO watched
    genre = db.Column(db.String(100))
    notes = db.Column(db.String(1000))

    def __init__(self, title, genre, release_date, notes, watched=False):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.notes = notes

    def IsWatched(self):
        print(self.watched)
        return self.watched

    def Watched(self):
        #TODO
        pass


class Movie(db.Model, BaseModel):
    #TODO
    pass


def main():
    pass


if __name__ == '__main__':
    main()