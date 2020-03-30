from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/pydb'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://qjuxvlqypxzqoh:28a12e723e0f4bb541828269ba1572c8608c2a7a86c8be528663f8ed9dddd2a6@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d5d140v2mqaj14?sslmode=require'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)   # create table: in terminal -py-then from app import db - then db.create_all()
# app.secret_key = ‘shhhh...iAmASecret!’
class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        # send_email(email,height)
        if db.session.query(Data).filter(Data.email_==email).count()== 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email,height,average_height,count)
            print(average_height) 
            return render_template("success.html")   
    return render_template("index.html",
    text="Seems like we've got something from that email address already!")

if __name__ == '__main__':
    app.debug=True 
    app.run()   