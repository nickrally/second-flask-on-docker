from flask.cli import FlaskGroup

from project import app, db, Note


cli = FlaskGroup(app)


@cli.command("say_hi")
def say_hi():
    print("HEY")


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Note(english="A man who wishes to seem simple cannot possibly be a simpleton.",
                   spanish="El hombre que desea parecer simple no puede ser un simplón."))
    db.session.commit()


if __name__ == "__main__":
    cli()
