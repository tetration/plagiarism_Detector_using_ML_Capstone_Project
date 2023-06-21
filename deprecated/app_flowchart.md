---
title: Run Plagiarism checker
---

::: mermaid


graph TD
    A[Start] --> B[Import Libraries]
    B --> C[Initialize Flask App]
    C --> D[Load Model]
    D --> E[Define Route '/' with GET and POST methods]
    E --> F[Check Request Method]
    F --> G[Handle POST Request]
    G --> H[Get Code from Form]
    H --> I[Predict using Model]
    I --> J[Check Prediction]
    J --> K[Print Prediction]
    K --> L[Set Result]
    L --> M[Render Template with Result]
    M --> G
    F --> N[Handle GET Request]
    N --> M
    E --> N
    C --> O[Run Flask App]
    O --> P[End]

:::