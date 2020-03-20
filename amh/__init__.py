"""
The flask application package.
"""
from flask import Flask, url_for, Markup, render_template, request, Response
from flask_bootstrap import Bootstrap
from flask_wtf import Form

def create_app():
    """Initialize the core application."""
    app = Flask(__name__,
                instance_relative_config=False,
                template_folder="templates",
                static_folder="static")
    Bootstrap(app)
    Form(app)

    # Initialize Plugins
    # db.init_app(app)
    # r.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import views
        from . import nav
        # from . import forms
        # from . import models

        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        return app
