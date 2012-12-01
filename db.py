from flask import _app_ctx_stack
from sqlite3 import dbapi2 as sqlite3


def init_db(app):
    """Creates the database tables."""
    with app.app_context():
        db = get_db(app)
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db(app):
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return top.sqlite_db


def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()
