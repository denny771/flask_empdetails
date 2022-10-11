from flask import Flask
app = Flask(__name__)
#to avoid cookie data tampering
app.secret_key="secret key"