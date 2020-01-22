from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404  # second argument is error code

@app.errorhandler(500)
def internal_error(error):
    # rollback database to clean state
    db.session.rollback()
    return render_template('500.html'), 500
