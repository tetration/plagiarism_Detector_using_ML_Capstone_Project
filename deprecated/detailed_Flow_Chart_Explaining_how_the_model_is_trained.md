


Detailed explanation of how the model is trained to detect plagiarism in source codes
---

::: mermaid

flowchart LR
    A[Import Libraries] --> B[Load Dataset]
    B --> C[Load Non-Plagiarized Code Files]
    B --> D[Load Plagiarized Code Files]
    C --> E[Append Code to X and Assign Label 0]
    D --> F[Append Code to X and Assign Label 1]
    B --> G[Train ML Model]
    G --> H[Create TfidfVectorizer]
    G --> I[Create LogisticRegression Classifier]
    G --> J[Create Pipeline]
    B --> K[Split Data into Train/Test Sets]
    J --> K[The TfidfVectorizer converts text data into numerical feature vectors, while LogisticRegression predicts one of two outcomes in binary classification tasks.]
    K --> L[Train Model]
    L --> M[Predict on Test Data]
    M --> N[Generate Classification Report]
    L --> O[Save Model]