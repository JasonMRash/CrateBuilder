"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from JasonRashWebsite import app
from flask import request
from JasonRashWebsite import crate

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
    )

@app.route('/projects')
def projects():
    """Renders the projects page."""
    return render_template(
        'projects.html',
        title='Projects',
        year=datetime.now().year,
        message=''
    )

@app.route('/resume')
def resume():
    """Renders the resume page."""
    return render_template(
        'resume.html',
        title='Resume',
        year=datetime.now().year,
        message=''
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/cratebuilder', methods=['GET', 'POST'])
def crateBuilder():
    """Renders the crate builder page."""
    return render_template(
        'cratebuilder.html',
        title='Crate Builder',
        year=datetime.now().year,
        message='Type in the inside dimensions of a crate in the form below.'  
    )

@app.route('/cratecalc', methods=['GET', 'POST'])
def crateCalc():
    """Renders the crate calculation page."""
    if request.method == "POST":
        insideHeight=request.form.get('inside_height')
        insideWidth=request.form.get('inside_width')
        insideLength=request.form.get('inside_length')
        sideBraces=request.form.get('side_braces')
        endBraces=request.form.get('end_braces')
        numRunners=request.form.get('num_runners')

    newCrate = crate.Crate(insideWidth, insideLength, insideHeight, sideBraces, endBraces)

    # Calculate Outside Crate Dimensions

    outsideLength=newCrate.outsideLength()
    outsideWidth=newCrate.outsideWidth()
    outsideHeight=newCrate.outsideHeight()

    #Calculate Pallet Slat & Runner Dimensions

    slatLength=insideWidth
    runnerLength=insideLength

    # Calculate Side Board Dimensions

    # Calculate End Board Dimensions

    # Calculate Top Board Dimensions

    return render_template(
        'cratecalc.html',
        title='Crate Builder Calculations',
        year=datetime.now().year,
        message='Here are the dimensions to make the crate drawings.',
        insideLength=insideLength,
        insideWidth=insideWidth,
        insideHeight=insideHeight,
        outsideLength=outsideLength,
        outsideWidth=outsideWidth,
        outsideHeight=outsideHeight,
        slatLength=slatLength,
        runnerLength=runnerLength,
        numRunners=numRunners
    )