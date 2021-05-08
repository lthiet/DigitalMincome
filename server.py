
import flask
from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import jsonify
from services import plotter

app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')
app.config['SECRET_KEY'] = 'DigitalMincome'
bootstrap = Bootstrap(app)


@app.route('/')
def root():
    return render_template("index.html")

# Request to make plot
@app.route('/plot')
def plot():
    return str(plotter.some_plot())

# Display the plot
@app.route('/plot.html')
def display_plot():
    return render_template("plot.html")

