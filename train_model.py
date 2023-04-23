import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the dataset
dataset_dir = 'IR-Plag-Dataset'
tasks = os.listdir(dataset_dir)

X = []
y = []

for task in tasks:
    task_dir = os.path.join(dataset_dir, task)
    print(task_dir)
    non_plagiarized_dir = os.path.join(task_dir, 'non-plagiarized')
    plagiarized_dir = os.path.join(task_dir, 'plagiarized')

    # Load non-plagiarized code files
    for subdir in os.listdir(non_plagiarized_dir):
        subdir_path = os.path.join(non_plagiarized_dir, subdir)
        for filename in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, filename)
            with open(file_path, 'r') as f:
                code = f.read()
                X.append(code)
                y.append(0)  # 0: non-plagiarized

    # Load plagiarized code files
    for level in os.listdir(plagiarized_dir):
        level_dir = os.path.join(plagiarized_dir, level)
        for subdir in os.listdir(level_dir):
            subdir_path = os.path.join(level_dir, subdir)
            for filename in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, filename)
                with open(file_path, 'r') as f:
                    code = f.read()
                    X.append(code)
                    y.append(1)  # 1: plagiarized

# Train the machine learning model
vectorizer = TfidfVectorizer()
classifier = LogisticRegression()

model = Pipeline([('vectorizer', vectorizer), ('classifier', classifier)])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'plagiarism_model.pkl')