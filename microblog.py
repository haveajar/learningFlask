import sqlalchemy as sqla
import sqlalchemy.orm as sqlorm
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlorm': sqlorm, 'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    app.run()
