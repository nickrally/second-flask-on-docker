from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)


@cli.command("say_hi")
def say_hi():
    print("HEY")


if __name__ == "__main__":
    cli()
