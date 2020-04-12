from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgre123@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://nfcxnxovvpepfq:d53a3a57f40002a702a6a9492f3e18a86590c5509d9571bf766129ebb52c8c81@ec2-35-172-85-250.compute-1.amazonaws.com:5432/delc5dflu1elde?sslmode=require '

db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])   
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data_var=Data(email,height)
            db.session.add(data_var)
            db.session.commit()
            avg_height= db.session.query(func.avg(Data.height_)).scalar()
            avg_height=round(avg_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email,height,avg_height,count)
            return render_template("success.html")
            
        else:
            return render_template("index.html",text= " Seems like we have already got something from that email address already")

if __name__== '__main__':
    app.debug=True
    app.run()