import click
from flask.cli import with_appcontext
from main import corona_data
from main import db

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    
