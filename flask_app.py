from flask import Flask,render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

from joblib import load
model = load('fintech.joblib')

@app.route("/probdefaultfixed")
def probdefaultfixed():
    """ Probability of Default Harded Coded """
    # dictionary with list object in values
    data = {
        'time_on_books' : [36],
        'total_paid_last_12_months' : [2000],
        'total_debt_in_arrears' : [4000]
    }

    # creating a Dataframe object
    data_df = pd.DataFrame(data)
    X = data_df[['time_on_books', 'total_paid_last_12_months', 'total_debt_in_arrears']]

    # predict
    prob_default = model.predict_proba(X)[:,1]

    return "Probability of default: {}".format(prob_default)


@app.route("/probdefault")
def probdefault():
    """ Probability of receiving parameters from HTML using GET """

    data = {
        'time_on_books' : [request.args['time_on_books']],
        'total_paid_last_12_months' : [request.args['total_paid_last_12_months']],
        'total_debt_in_arrears' : [request.args['total_debt_in_arrears']]
    }

    # creating a Dataframe object
    data_df = pd.DataFrame(data)
    X = data_df[['time_on_books', 'total_paid_last_12_months', 'total_debt_in_arrears']]

    # predict
    prob_default = model.predict_proba(X)[:,1]

    return "Probability of default: {}".format(prob_default)
