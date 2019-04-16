from flask import Flask, render_template
app = Flask(__name__)

poems = [
    {
        'title': "Tràng Giang",
        'content': "Lớp lớp mây cao đùm núi bạc",
        'author' : "Huy Cận",
        'gender' : "male"
    },
    {
        'title': "Tràng Giang",
        'content': "Chim nghiếng cánh nhỏ bóng chiều sa",
        'author' : "Huy Cận",
        'gender' : "male"
    },
    {
        'title': "Tràng Giang",
        'content': "Lòng quê dờn dợn vời con nước",
        'author' : "Huy Cận",
        'gender' : 'female'
    },
    {
        'title': "Tràng Giang",
        'content': "Không khói hoàng hôn cũng nhớ nhà",
        'author' : "Huy Cận",
        'gender' : "female"
    }

]


@app.route('/')
def index():
    return "Hello World"

@app.route('/say-hi/<name>')
def sayhi(name):
    return "Hi {0}".format(name)


@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return "Sum: {0}".format(a+b )

#all poems

@app.route('/poem')
def testing():   
    # return '<h1> This is heading level 1 </h1>'
    return render_template('poem.html',poems = poems)


#detailed poems

@app.route('/poem/<int:index>')
def detail(index):
    id = index - 1
    poem = poems[id]
    return render_template('index_poem.html',poem = poem,id=index)



if __name__ == '__main__':
  app.run(debug=True)
 
