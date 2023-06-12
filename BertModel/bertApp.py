# app.py
from flask import Flask, request, render_template
import joblib
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
#model = joblib.load('plagiarism_model.pkl')
bert_model = SentenceTransformer('bert-base-nli-mean-tokens')

def compare_codes(code1, code2):
    embeddings = bert_model.encode([code1, code2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity

def compare_with_folder(code, folder_path):
    similarities = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as f:
            other_code = f.read()
            similarity = compare_codes(code, other_code)
            similarities.append(similarity)
    return max(similarities)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code1 = request.form['code1']
        code2 = request.form['code2']
        
        if code1 and code2:
            similarity = compare_codes(code1, code2)
            result = f"The similarity between the two codes is: {similarity}"
        elif code1:
            folder_path = 'code_folder'
            similarity = compare_with_folder(code1, folder_path)
            result = f"The highest similarity between the code and the codes in the folder is: {similarity}"
        elif code2:
            folder_path = 'code_folder'
            similarity = compare_with_folder(code2, folder_path)
            result = f"The highest similarity between the code and the codes in the folder is: {similarity}"
        else:
            result = "Please provide at least one code to compare."
        
        print(result)
        return render_template('index.html', result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
