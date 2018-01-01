from flask import Flask, render_template, request, session
from random import randint
import pickle


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_get():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form['speech']

    # Prepare the vectorizer for prediction
        pkl_file = open('model.pkl', 'rb')
        svm_model = pickle.load(pkl_file, encoding='latin1')

    # Predict using the SVM model
        y = svm_model.predict([data])

        return render_template('result.html', prediction=y, data=data)


if __name__ == '__main__':
    app.run()
