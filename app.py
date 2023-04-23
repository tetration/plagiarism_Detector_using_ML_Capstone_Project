# app.py
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('plagiarism_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        prediction = model.predict([code])[0]
        print(prediction)
        result = "Plagiarized" if prediction == 1 else "Non-plagiarized"
        print(result)
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)