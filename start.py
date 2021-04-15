from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
   password="",
   database="webdemo"
)

mycursor = mydb.cursor()

@app.route('/')
def hello_world():
    return render_template("index.html")
   
   
   
@app.route('/omen')
def exam_resources():
 
   mycursor.execute("SELECT * FROM omen")
   myresult = mycursor.fetchall()
   return render_template("index2.html", myresult=myresult)

@app.route("/sova")
def  bible_resources():
   
   mycursor.execute("SELECT * FROM sova")
   myresult = mycursor.fetchall()
   return render_template("index3.html", myresult=myresult)
if __name__ == '__main__':
   app.run(debug=True)