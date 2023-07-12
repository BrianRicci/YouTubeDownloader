from app import app
from flask import render_template, url_for, request, redirect
from .video_code import get_video_code
# from .models import *



@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == "POST":
        url_video = request.form['urlInput']
        code = get_video_code(url_video)
        return redirect(f'/{code}')
    else:
        return render_template('index.html')


@app.route('/<video_code>')
def download_page(video_code):
    
    return render_template('download.html')


@app.route('/about')
def about():
    return render_template('about.html')
