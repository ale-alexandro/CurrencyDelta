from flask import Flask

from app.CRB import CRB

app = Flask(__name__)
crb = CRB()

from app import routes
