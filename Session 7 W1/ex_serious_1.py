from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/bmi/<int:w>/<int:h>')
def BMI(w,h):
    hm = h/100
    BMI = w/(hm*hm)

    if BMI < 16:
        return "Serverely underweight"
    else:
            if BMI < 18.5:
                return "Underweight"
            else:
                if BMI < 25:
                    return "Normal"
                else:
                    if BMI < 30:
                        return "Overweight"
                    else:
                        return"Obsese" 

if __name__ == '__main__':
    app.run(debug=True)  
