# import packages
from flask import Flask, render_template, request
import numpy as np
import sklearn
import pickle
app = Flask('handwritten_digits_recognizer')

# setting up '/' route for home page


@app.route('/')
def show_home():
    return render_template('index.html')

# @app.route('/results', methods=['POST'])


@app.route('/results')
def results():
    form = request.form
    # if request.method == 'POST':
    # function that loads the model
    skl = pickle.load(open('./models/sklearn.pickle', 'rb'))
    test_img = np.array([[0.,  0.,  0., 12., 13.,  5.,  0.,  0.,  0.,  0.,  0., 11., 16.,
                9.,  0.,  0.,  0.,  0.,  3., 15., 16.,  6.,  0.,  0.,  0.,  7.,
                15., 16., 16.,  2.,  0.,  0.,  0.,  0.,  1., 16., 16.,  3.,  0.,
                0.,  0.,  0.,  1., 16., 16.,  6.,  0.,  0.,  0.,  0.,  1., 16.,
                16.,  6.,  0.,  0.,  0.,  0.,  0., 11., 16., 10.,  0.,  0.]])
    result = skl.predict(test_img)
    print(result[0])
    return render_template('index.html', digit=result[0])


if __name__ == '__main__':
    app.run('localhost', '8080', debug=True)
