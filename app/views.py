from app import app
from flask import render_template, url_for, request, redirect
# from .models import *


@app.route('/')
def index():
    return render_template('index.html')


