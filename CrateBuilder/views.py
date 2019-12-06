"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CrateBuilder import app
from flask import request
from CrateBuilder import crate

@app.route('/')
@app.route('/cratebuilder', methods=['GET', 'POST'])
def crateBuilder():
    """Renders the crate builder page."""
    return render_template(
        'cratebuilder.html',
        title='Crate Builder',
        year=datetime.now().year,
        message='Type in the required inside dimensions of a crate in inches.'  
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

    newCrate = crate.Crate(insideWidth, insideLength, insideHeight, sideBraces, endBraces, numRunners)

    # Calculate Outside Crate Dimensions

    outsideLength=newCrate.outsideLength()
    outsideWidth=newCrate.outsideWidth()
    outsideHeight=newCrate.outsideHeight()

    #Calculate Pallet Slat & Runner Dimensions

    slatLength=insideWidth
    runnerLength=insideLength
    palletSlatSpacing=newCrate.palletSlatSpacing()
    numSlats=newCrate.numSlats()
    palletRunnerSpacing=newCrate.palletRunnerSpacing()

    # Calculate Side Board Dimensions

    sideTopRailLength=newCrate.sideTopRailLength()
    sideVertRailLength=newCrate.sideVertRailLength()

    # Calculate End Board Dimensions

    endTopRailLength=newCrate.endTopRailLength()
    endVertRailLength=newCrate.endVertRailLength()

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
        numRunners=numRunners,
        palletSlatSpacing=palletSlatSpacing,
        numSlats=numSlats,
        palletRunnerSpacing=palletRunnerSpacing,
        sideTopRailLength=sideTopRailLength,
        sideVertRailLength=sideVertRailLength,
        endTopRailLength=endTopRailLength,
        endVertRailLength=endVertRailLength
    )

@app.route('/about')
def about():
    """Renders the crate builder page."""
    return render_template(
        'about.html',
        title='About Crate Builder',
        year=datetime.now().year,
        message='Why I created this project.'  
    )