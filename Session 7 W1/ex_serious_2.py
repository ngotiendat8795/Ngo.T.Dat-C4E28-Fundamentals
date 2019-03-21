from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<name>')
def user_infor(name):
    users = {
        "yen" : {
            "name": "Nguyen Ha Yen",
            "age" : 24,
            "marital" : "single"
        },
        "quynh" : {
            "name": "Hoang An Diem Quynh",
            "age" : 25,
            "marital" : "Ế"
        },
        "huyen" : {
            "name": "Le Thi Huyen",
            "age" : 24,
            "marital" : "married"
        },
        "trang" : {
            "name": "Trinh Thu Trang",
            "age" : 24,
            "marital" : "single"
        },
        "nga" : {
            "name": "Nguyen Thi Nga",
            "age" : 24,
            "marital" : "single"
        }
        
    }

    infor = users[name]
    return render_template('user_infor.html',infor = infor)

if __name__ == '__main__':
  app.run(debug=True)
 