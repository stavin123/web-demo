from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html")

@app.route('/exam')
def exam_resources():
   return render_template("index2.html")

@app.route("/bible")
def  bible_resources():
   return render_template("index3.html")
if __name__ == '__main__':
   app.run(debug=True)