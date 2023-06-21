
Detailed explanation of how the model detects plagiarism in source codes submitted by the user
---

::: mermaid

flowchart LR
    A[Importing Required Libraries]
    B[Loading the Model]
    C[Defining the Flask Application]
    D[Route Definition]
    E{Is the request method POST?}
    F[Handling GET and POST Requests]
    G[Machine learning Model Makes The Prediction]
    H[Is the source code plagiarized?]
    I[Returns the binary classification of 1]
    J[Returns the binary classification of 0]
    K[Displays the Result to the User]


    A --> B
    B --> C
    C --> D
    D --> E
    E -->|Yes| F
    E -->|No| K
    F --> G
    G --> H
    H -->|Yes| I
    H -->|No| J
    I --> K
    J --> K