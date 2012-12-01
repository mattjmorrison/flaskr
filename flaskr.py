from app import app
from db import close_db_connection, init_db
from controllers import login, logout, add_entry, show_entries

app.config.from_object('settings')

app.route('/')(show_entries)
app.route('/add', methods=['POST'])(add_entry)
app.route('/login', methods=['GET', 'POST'])(login)
app.route('/logout')(logout)


if __name__ == '__main__':
    app.teardown_appcontext(close_db_connection)
    init_db(app)
    app.run()
