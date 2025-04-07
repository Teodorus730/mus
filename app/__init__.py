from flask import Flask

import os
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=1)

from app import routes

