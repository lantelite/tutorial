from flask import Blueprint, render_template, flash, redirect, url_for

frontend = Blueprint('frontend', __name__)

@app.route('/')
def index():
    return render_template('bootstrap_index.html')