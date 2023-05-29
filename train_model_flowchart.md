---
title: train_model flowchart
---

::: mermaid

graph TD
    A[Start] --> B[Load Dataset]
    B --> C[Initialize X and y]
    C --> D[Loop through tasks]
    D --> E[Set task_dir]
    E --> F[Set non_plagiarized_dir]
    F --> G[Loop through non-plagiarized code files]
    G --> H[Read code file]
    H --> I[Append code to X and label to y]
    I --> G
    F --> J[Set plagiarized_dir]
    J --> K[Loop through plagiarized code files]
    K --> L[Read code file]
    L --> M[Append code to X and label to y]
    M --> K
    D --> E
    D --> N[Train the ML model]
    N --> O[Initialize vectorizer and classifier]
    O --> P[Create model pipeline]
    P --> Q[Split data into training and testing sets]
    Q --> R[Train the model]
    R --> S[Predict on test data]
    S --> T[Print classification report]
    T --> U[Save the model]
    U --> V[End]

:::