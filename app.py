from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static') 

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/signup', methods= ['GET','POST'])

def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        return redirect('/thankyou')
    else:
        return render_template('signup.html')

       


if __name__ == '__main__':
    app.run()
