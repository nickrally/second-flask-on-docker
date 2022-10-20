from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField


app = Flask(__name__)
app.config.from_object("project.config.Config")
app.secret_key = 'dessertafterdinner'
db = SQLAlchemy(app)


class NoteForm(FlaskForm):
    english = StringField('english')
    spanish = StringField('spanish')


class Note(db.Model):
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.Text)
    spanish = db.Column(db.Text)

    def __init__(self, english, spanish):
        self.english = english
        self.spanish = spanish


@app.route('/', endpoint='home', methods=['GET', 'POST'])
def index():
    notes = Note.query.order_by(Note.id.asc())
    return render_template('home.html', notes=notes)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    note = Note.query.get(id)
    if request.method == 'POST':
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('delete.html', note=note, id=id)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = NoteForm(request.form)
    if request.method == 'POST':
        note = Note(form['english'].data, form['spanish'].data)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit/<string:id>', methods=['GET', 'POST'], endpoint='edit')
def edit(id):
    note = Note.query.get(id)
    form = NoteForm(obj=note)
    if request.method == 'POST':
        form.populate_obj(note)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', note=note, id=id, form=form)
