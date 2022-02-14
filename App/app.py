from flask import Flask, render_template
import datetime
import pandas as pd
import dataFrame

app = Flask(__name__)

df = pd.read_csv ('./static/assets/windows.csv', on_bad_lines='skip')



labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/')
# def hello():
#     bar_labels = labels
#     bar_values = values
#     return render_template('home.html', utc_dt=datetime.datetime.utcnow(), title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)
def hello():
    bar_labels = list(dataFrame.allUniqEventIDsFreq.keys())
    bar_labels.pop(0)
    bar_values = list(dataFrame.allUniqEventIDsFreq.values())
    #print(bar_values)
    bar_values.pop(0)
    return render_template('home.html', utc_dt=datetime.datetime.utcnow(), title='Bitcoin Monthly Price in USD', max=400, labels=bar_labels, values=bar_values)

@app.route('/about/')
def about():
    return render_template('about.html')

app.run(host='0.0.0.0', port=5000)
