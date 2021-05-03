from myapp import app
import numpy as np
import pandas as pd
import json
from flask import render_template, request
#from scripts.graphs import return_figures

print("Defining pages")

@app.route('/')
@app.route('/index')
def jumbotron():
    """Render the main portfolio page

    Args:
        None

    Returns:
        index.html page
    """
    return render_template('index.html')

#@app.route('/capstone/eda')
#def eda():
#    """Render the page for exploratory data analysis
#
#    Args:
#        None
#
#    Returns:
#        eda.html page
#    """
#    figures = return_figures()
#
#    # plot ids for the html id tag
#    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
#
#    # Convert the plotly figures to JSON for javascript in html template
#    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
#
#    return render_template('eda.html',
#                           ids=ids,
#                           figuresJSON=figuresJSON)
#