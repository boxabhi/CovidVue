import click
from flask.cli import with_appcontext

from main import corona_data

@click.command(name="corona_data")
@with_appcontext
def create_tables():
    db.create_all()
    
