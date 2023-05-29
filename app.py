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
        probability = model.predict_proba([code])[0]
        accuracy_percentage = round(max(probability) * 100, 2) 
        if prediction == 1:
            result = f"\n We predicted the possibility of this code being Plagiarized with {accuracy_percentage}% accuracy."
        else:
            result = f"\n We predicted the possibility of this code being Non-plagiarized with {accuracy_percentage}% accuracy."
        print(result)
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)