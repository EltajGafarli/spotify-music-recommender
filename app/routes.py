from app import app
from app.musicdata import getMusics
from datetime import datetime

from flask import redirect
from flask import url_for
from flask import flash
from flask import render_template
from flask import request
from werkzeug.exceptions import HTTPException

@app.route('/',methods=["GET","POST"])
def main():
    data = getMusics()
    if request.method == "POST":
        return redirect(url_for('main'))
    return render_template('album.html',songs = data[0],genre = data[1])

@app.errorhandler(404)
def notfound(err):
    return render_template('error.html',error=404),404

@app.errorhandler(HTTPException)
def err304(err):
    return render_template('error.html',error=304),HTTPException

    