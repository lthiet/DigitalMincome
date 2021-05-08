
from flask import Flask
from flask import render_template
from flask import request
from services import plotter

app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')

app.config['SECRET_KEY'] = 'DigitalMincome'


@app.route('/')
def root():
    return render_template("index.html")

# Request to make plot


@app.route('/plot')
def plot():
    params = {
        "transaction_fee": int(request.args.get("transaction_fee")),
        "defi_prop": int(request.args.get("defi_prop")),
        "defi_return": int(request.args.get("defi_return")),
        "fund_return": int(request.args.get("fund_return")),
        "growth_model": request.args.get("growth_model")
    }
    return str(plotter.plot(params
                                 ))

# Display the plot


@app.route('/plot.html')
def display_plot():
    return render_template("plot.html")
