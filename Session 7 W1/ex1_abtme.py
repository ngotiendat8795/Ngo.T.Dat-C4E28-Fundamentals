from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def infor():
    inf = {
       'NAME': 'DATNT',
       'WORK' : 'BOND TRADER',
       'SCHOOL': 'NATIONAL ECONOMICS UNIVERSITY',
       'HOBBIES': 'DOING NOTHING',
       'CRUSH' : 'NO ONE'
    }
    return render_template('infor.html',inf=inf)

@app.route('/school')
def change():
    return redirect('https://techkids.vn/')

if __name__ == '__main__':
    app.run(debug=True)  