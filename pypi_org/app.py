"""First Flask site."""
import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    """Homepage."""
    return "Hello world!"


if __name__ == '__main__':
    app.run()
