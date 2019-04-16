#fapp

from flask import *
app = Flask(__name__)
from services import Services
from bson.objectid import ObjectId
app.config["SECRET_KEY"] = "everytime you walk out the less i love you ahihi 12345#@@@#"


@app.route('/')
def index():
  session["logged"]=False
  return render_template('homepage.html')

@app.route('/all-service')
def get_service():
  if session["logged"] == True:

    all_services = Services.find()
    return render_template('services.html', Services=all_services)
  else:
    return redirect('/login')

@app.route('/all-service/<gender>')
def male(gender):
  male_services = Services.find({"gender": gender})
  return render_template('services.html', Services=male_services)

@app.route('/all-service/details/<id>')
def details(id):
  detail_service = Services.find_one({"_id": ObjectId(id)})
  return render_template('detail_service.html',detail_service = detail_service)


@app.route('/delete/<id>')
def delete(id):
  del_servce = Services.find_one({"_id": ObjectId(id)})
  if del_servce is not None:
    Services.delete_one(del_servce)
    return redirect('/all-service')
  else:
    print("Not found")



@app.route('/update/<id>', methods=["GET","POST"])
def update(id):

  edit_service = Services.find_one({"_id": ObjectId(id)})
  if request.method == "GET": 
    return render_template("update_service.html", edit_service=edit_service)
  elif request.method == "POST":
    form = request.form
    name = form["name"]
    age = form["age"]
    gender = form["gender"]
    address = form["address"]
    new_value = {"$set":{
      "name": name,
      "age": age,
      "Address": address,
      "gender":gender
    }}
    Services.update_one(edit_service,new_value)
    return redirect('/all-service/details/{0}'.format(id))


@app.route('/login', methods=["GET","POST"])
def login():
  if not session["logged"]:
    if request.method == "GET":
      return render_template('login.html')
    elif request.method == "POST":
      form = request.form
      username = form["username"]
      password = form["password"]

      if username == "admin" and password == "admin":
        session["logged"]=True
        return redirect('/all-service')
      else:
        return redirect('/login')
  else:
    return redirect('/all-service')

@app.route('/logout')
def logout():
  # del session['logged'] #cach 1
  session["logged"] = False #cach 2
  return redirect('/login')



if __name__ == '__main__':
  app.run(debug=True)
 
