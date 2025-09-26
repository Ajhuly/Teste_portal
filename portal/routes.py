# rotas de links
from flask import render_template, url_for
from portal import app

@app.route('/')
def home():
    return render_template('index.html')
