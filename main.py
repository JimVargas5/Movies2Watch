#Jim Vargas
#This is a little database thing for me to keep track of the movies
#and TV shows that I want to watch

from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
#TODO
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Movies2Watch:Movies2Watch@localhost:8889/Movies2Watch'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'poop'

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    type = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    release_date = db.Column(db.Integer)
    notes = db.Column(db.String(1000))
    consumed = db.Column(db.Boolean)

    def __init__(self, title, type, genre, release_date, notes, consumed=False):
        self.title = title
        self.type = type
        self.genre = genre
        self.release_date = release_date
        self.notes = notes
        self.consumed = consumed

    def Consumed(self):
        self.consumed = True


@app.route("/")
def index():
    return redirect("/home")

@app.route("/home", methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
        add_title = request.form["add_title"]
        add_type = request.form["add_type"]
        add_genre = request.form["add_genre"]
        add_release_date = request.form["add_release_date"]
        add_notes = request.form["add_notes"]

        NewMedia = Media(add_title, add_type, add_genre, add_release_date, add_notes)
        db.session.add(NewMedia)
        db.session.commit()
        return redirect("/")

    Medias2Consume = Media.query.filter_by(consumed= False).all()
    return render_template("home.html", Medias2Consume= Medias2Consume)

@app.route("/consume", methods= ['POST', 'GET'])
def consume():
    id = request.args.get('media')
    existing_media = Media.query.filter_by(id= id).first()
    if request.method == 'POST':
        existing_media.Consumed()
        db.session.add(existing_media)
        db.session.commit()
        return redirect("/")

    return render_template("consume.html", existing_media= existing_media)


if __name__ == '__main__':
    app.run()