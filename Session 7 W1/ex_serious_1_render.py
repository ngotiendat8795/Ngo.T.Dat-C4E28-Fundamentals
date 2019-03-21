from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:w>/<int:h>')
def CAL(w,h):
    hm = h/100
    bmi = w/(hm*hm)
    return render_template('bmi.html', BMI=bmi)

if __name__ == '__main__':
    app.run(debug=True)  