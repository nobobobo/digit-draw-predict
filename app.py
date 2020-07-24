# import packages
from flask import Flask, render_template, request
app = Flask('handwritten_digits_recognizer')

# setting up '/' route for home page
@app.route('/')
def show_home():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run('localhost', '8080', debug=True)