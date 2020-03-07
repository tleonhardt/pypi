"""First Flask site."""
import os

import flask

import pypi_org.data.db_session as db_session

app = flask.Flask(__name__)


def initialize_stuff():
    register_blueprints()
    setup_db()


def main():
    initialize_stuff()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(os.path.dirname(__file__), 'db', 'pypi.sqlite')
    db_session.global_init(db_file)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views
    from pypi_org.views import account_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    # Run from Python
    main()
elif __name__ == 'app':
    # Run from the flask command line executable
    initialize_stuff()
