from flask_mock import app


@app.route('/')
@app.route('/help')
def how_to_use():
    return 'Will be updated help page and request index'
