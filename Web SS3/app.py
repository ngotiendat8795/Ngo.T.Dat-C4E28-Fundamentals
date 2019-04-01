from flask import *
app = Flask(__name__)
from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@c4e28cluster-chzuv.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
bike_database = client.db_bike
bike_model = bike_database["bike_model"]

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('new_bike.html')
    elif request.method == "POST":
        form = request.form 
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]

        infor = {
            "model":model,
            "fee":fee,
            "image":image,
            "year":year
        }
        bike_model.insert_one(infor)
        return redirect('/new_bike')

@app.route('/new_bike')
def newbike():
  return render_template('new_bike.html')

@app.route('/t1')
def t1():
  return render_template('t1.html')

if __name__ == '__main__':
  app.run(debug=True)
 