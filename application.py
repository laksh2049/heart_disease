
import pickle 
from flask import Flask,request,jsonify,render_template
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application 

## import ridge regressor
randomcv_model = pickle.load(open('randomcv.pkl' ,'rb'))



@app.route("/")
def index():

    return render_template('index.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Temperature=float (request. form.get ('Temperature'))

        age = float(request. form.get ('age'))

        sex = float(request. form.get ('sex'))

        cp = float (request. form.get('cp'))

        trestbps = float (request. form.get('trestbps' ))

        chol = float (request. form.get ('chol' ))

        fbs = float (request. form.get ('fbs'))

        restecg = float(request. form.get ('restecg'))

        thalach = float(request. form. get ('thalach' ))

        exang = float(request. form. get ('exang' ))

        oldpeak = float(request. form. get ('oldpeak' ))

        slope = float(request. form. get ('slope' ))

        ca = float(request. form. get ('ca'))

        thal = float(request. form. get ('thal'))

        new_data_scaled= ([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        result = randomcv_model.predict(new_data_scaled)

        return render_template('home.html', results= result[0])
        
    else :
        return render_template('home.html')

if __name__=="__main__" :
    app.run( host="0.0.0.0",port = 5002 )