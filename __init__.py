from flask import Flask

def create_app():
    application = app = Flask(__name__)

    from .smart_tools import smart_tools as smart_tools_blueprint
    app.register_blueprint(smart_tools_blueprint)

    return application

application = create_app()