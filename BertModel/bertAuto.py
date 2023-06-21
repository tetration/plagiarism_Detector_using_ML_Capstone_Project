import os
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load the pre-trained BERT model
bert_model = SentenceTransformer('bert-base-nli-mean-tokens')

def compare_codes(code1, code2):
    embeddings = bert_model.encode([code1, code2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity

def compare_with_folder(code, folder_path,original_filename):
    similarities = []
    code_name = os.path.basename(code)
    for level in os.listdir(folder_path):
        level_dir = os.path.join(folder_path, level)
        if os.path.isdir(level_dir):
            print('level_dir',level_dir)
            #foreach folder in 
            if level_dir==original_dir:
                continue
            for folders in os.scandir(level_dir):
                print(folders.path)
                finalFilePath= folders.path
                for codeFile in os.scandir(finalFilePath):
                    print('current location:', codeFile.path)
                    try:
                        if codeFile.is_dir:
                            for codeFilez in os.scandir(codeFile.path):
                                with open(codeFilez.path, 'r') as f:
                                    print('current location:', codeFilez.path)
                                    other_code = f.read()
                                    similarity = compare_codes(code, other_code)
                                    similarities.append((similarity, code_name, codeFilez))
                    except:
                        print("Error", codeFile.path, " is not a directory")
                    try:
                        if codeFile.is_file:
                            print(codeFile,' is a code file')
                            print('code file found:', codeFile.path)
                            with open(codeFile.path, 'r') as f:
                                other_code = f.read()
                                similarity = compare_codes(code, other_code)
                                similarities.append((similarity, code_name, codeFile))
                    except:
                        print("Error", codeFile.path, " is not a file")
    return similarities


def compare_with_folder_Original(code, folder_path,original_dir):
    similarities = []
    code_name = os.path.basename(code)
    for level in os.listdir(folder_path):
        level_dir = os.path.join(folder_path, level)
        if os.path.isdir(level_dir):
            print('level_dir',level_dir)
            for filename in os.listdir(level_dir):
                file_path = os.path.join(level_dir, filename)
                with open(file_path, 'r') as f:
                    other_code = f.read()
                    similarity = compare_codes(code, other_code)
                    similarities.append((similarity, code_name, filename))
    return similarities

def compare_with_folder1(code, folder_path):
    similarities = []
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_file():
                file_path = os.path.join(folder_path, entry.name)
                with open(file_path, 'r') as f:
                    other_code = f.read()
                    similarity = compare_codes(code, other_code)
                    similarities.append(similarity)
    return similarities
# Main code
dataset_dir = 'IR-Plag-Dataset'
results = []

for case in os.listdir(dataset_dir):
    case_dir = os.path.join(dataset_dir, case)
    if os.path.isdir(case_dir):
        original_dir = os.path.join(case_dir, 'original')
        for filename in os.listdir(original_dir):
            file_path = os.path.join(original_dir, filename)
            print('original file', filename)
            with open(file_path, 'r') as f:
                code = f.read()
                similarities = compare_with_folder(code, case_dir, original_dir)
                results.extend(similarities)

# Create a DataFrame from the results
df = pd.DataFrame(results, columns=['Similarity', 'Code 1', 'Code 2'])

# Save the results to an Excel spreadsheet
output_file = 'plagiarism_results.xlsx'
df.to_excel(output_file, index=False)
print(f"Plagiarism results saved to {output_file}")
