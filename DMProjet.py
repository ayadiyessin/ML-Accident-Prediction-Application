from flask import Flask
from flask import render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('data/trainD1.pkl', 'rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result')
def result():
    return render_template("result.html", df_view=df)

@app.route("/predict", methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
#geting data from html form
        YearOfObservation = float(request.form["YearOfObservation"])
        Insured_Period = float(request.form['Insured_Period'])
        Residential = float(request.form['Residential'])
        Building_Painted = request.form['Building_Painted']
        Building_Fenced = request.form['Building_Fenced']

        Garden = request.form["Garden"]
        Settlement = request.form['Settlement']
        Building_Dimension = float(request.form['Building_Dimension'])
        Building_Type = request.form['Building_Type']
        NumberOfWindows = float(request.form['NumberOfWindows'])
# after geting data appending in a list
        lst = list()
        lst.append((YearOfObservation))
        lst.append((Insured_Period))
        lst.append((Residential))
        if Building_Painted == "N":
            BPainted_N = 1
            BPainted_V = 0
        else:
            BPainted_N = 0
            BPainted_V = 1
        lst.append((BPainted_N))
        lst.append((BPainted_V))


        if Building_Fenced == "N":
            BFenced_N = 1
            BFenced_V = 0
        else:
            BFenced_N = 0
            BFenced_V = 1
        lst.append((BFenced_N))
        lst.append((BFenced_V))


        if Garden == "O":
            Garden_O = 1
            Garden_V = 0
        else:
            Garden_O = 0
            Garden_V = 1
        lst.append((Garden_O))
        lst.append((Garden_V))


        if Settlement == "R":
            Settlement_R = 1
            Settlement_U = 0
        else:
            Settlement_R = 0
            Settlement_U = 1
        lst.append((Settlement_R))
        lst.append((Settlement_U))
        lst.append((Building_Dimension))

        if Building_Type == "Fire_resistive":
            Fire_resistive = 1
            Non_combustible = 0
            Ordinary = 0
            Wood_framed = 0
        elif Building_Type == "Non_combustible":
            Fire_resistive = 0
            Non_combustible = 1
            Ordinary = 0
            Wood_framed = 0
        elif Building_Type == "Ordinary":
            Fire_resistive = 0
            Non_combustible = 0
            Ordinary = 1
            Wood_framed = 0
        else:
            Fire_resistive = 0
            Non_combustible = 0
            Ordinary = 0
            Wood_framed = 1
        lst.append((Fire_resistive))
        lst.append((Non_combustible))
        lst.append((Ordinary))
        lst.append((Wood_framed))
        lst.append((NumberOfWindows))


# converting list into 2 D numpy array
        ans = model.predict([np.array(lst,dtype='float64')])
        result=ans[0]
        return render_template("result.html",result=result)

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
