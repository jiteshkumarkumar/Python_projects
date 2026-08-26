# importing
from flask import Flask, render_template, request

#interaction
web = Flask(__name__)  # constractor

# mapping
@web.route('/')
@web.route('/register')

#input
def homepage():
    return render_template('register.html')

#roots
@web.route('/confirmation', methods= ['POST','GET'])

#inputs
def register():
    if request.method == 'POST':
        n= request.form.get('name')
        c=request.form.get('city')
        p=request.form.get('phonenumber')
        return render_template('confirm.html',name=n,city=c,phonenumber=p)


if __name__ == '__main__':
    web.run(debug=True)  # debug=True, it will reload automatically and users does not require to load