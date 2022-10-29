from flask import Flask

def create_app():
    app = Flask(__name__)
    from .views import test_views
    app.register_blueprint(test_views.bp)

    return app