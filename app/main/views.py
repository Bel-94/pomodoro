from flask import render_template
from . import main 
from ..models import User

@main.route ('/')
def index():

    message = "Hello World" 

    return render_template('index.html', message=message)
