from logging import exception
from flask import Flask,render_template,url_for,request,redirect,session,send_file

import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import config

app = Flask(__name__)
app.secret_key = 'many random bytes'
# Python Flask app with two routes rendering index.html template.



@app.route("/")
@app.route('/home',methods = ['POST','GET'])
def home():
    return render_template('index.html')

@app.route("/projects",methods = ["post","get"])
def project():
    return render_template("project.html")


@app.route("/download",methods = ["post","get"])
def download():
    path = "jibran_resume.pdf"
    return send_file(path, as_attachment=True)


@app.route("/contact",methods = ["post","get"])
def contact():
    # try:
        name = request.form['name']
        mail_to = request.form['email']
        r_mail = mail_to.lower()
        phone = request.form['phone']
        message = request.form['message']
        
        config.send_mail(name,r_mail,phone,message)
    
        return render_template("index.html")
    
    # except:
    #     return render_template("404.html")
@app.route("/car",methods = ["post","get"])
def car():

    if request.method == "POST":
       year = int(request.form.get("year"))
       price = float(request.form.get("showroom price"))
       km_driven = int(request.form.get("Kms_Driven"))
       owners= int(request.form.get("owner"))
       Fuel_type = int(request.form.get("Fuel_Type"))
       if(Fuel_type==1):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
       else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
       Seller = request.form.get("Seller")
       if(Seller == 1): 
            Seller_Type_Individual=1
       else:
            Seller_Type_Individual=0
       Transmission = request.form.get("Transmission")
       if(Transmission == 1):
            Transmission_Mannual=1
       else:
            Transmission_Mannual=0
       model = pickle.load(open('./models/random_forest_regression_model.pkl', 'rb'))
       
       print(year,km_driven,owners,Fuel_type,Seller,Transmission)
       prediction=model.predict([[price,km_driven,owners,year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
       output=round(prediction[0],2)
       if output<0:
            return render_template('car.html',prediction_texts="Sorry you cannot sell this car")
       else:
            return render_template('car.html',prediction_text="You Can Sell The Car at {}".format(output))
    
    
    return render_template("car.html")
    
    # except:
    #     return render_template("404.html")
    
# if __name__ == '__main__':
#     app.run(port = 5000) 
if __name__ == '__main__':
    app.run(debug=True,host = "0.0.0.0")
    