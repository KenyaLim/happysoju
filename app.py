from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy username and password
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        return render_template('welcome.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
