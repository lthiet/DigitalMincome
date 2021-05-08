
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
        "initial_number_user": int(request.args.get("initial_number_user")),
        "final_number_user": int(request.args.get("final_number_user")),
        "avg_nb_transactions": int(request.args.get("avg_nb_transactions")),
        "avg_amount_transaction": int(request.args.get("avg_amount_transaction")),
        "time": int(request.args.get("time")),
        "tau": int(request.args.get("tau")),
        "defi_redistrib_period": int(request.args.get("defi_redistrib_period")),
        "fund_period": int(request.args.get("fund_period"))
    }
    print(params)
    return str(plotter.plot(params
                            ))

# Display the plot


@app.route('/plot<id>.html')
def display_plot(id):
    return render_template(f"plot{id}.html")
