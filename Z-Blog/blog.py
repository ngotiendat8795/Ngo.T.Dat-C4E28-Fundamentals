from flask import *
app = Flask(__name__)

from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@c4e28cluster-chzuv.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
mail_database = client.db_secretmail
mail = mail_database["mail"]


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('blog.html')
    elif request.method == "POST":
        form = request.form 
        name = form["name"]
        email = form["email"]
        content = form["content"]

        infor = {
            "name":name,
            "email":email,
            "content":content
        }
        mail.insert_one(infor)
        return redirect('/thanknote')

@app.route('/thanknote')
def thanknote():
    return render_template('thanknote.html')

# @app.route('/')
# def index():
#     a = reading.find_one({"id":"12340"})
#     passage = a["para"]
#     passage.replace('/n',"<br>")
#     return render_template('reading.html',passage=passage)

if __name__ == '__main__':
  app.run(debug=True)
