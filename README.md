# Spam Detector Project

## Table of Contents
1. [Introduction](#introduction)
2. [Notebooks Overview](#notebooks-overview)
3. [Metrics](#metrics)
4. [Model Accuracy](#model-accuracy)
5. [Model Deployment and Integration](#model-deployment-and-integration)
6. [Dockerization](#dockerization)
7. [Simple Interface](#simple-interface)
8. [References and Research Papers](#references-and-research-papers)

---

## Introduction
This project focuses on **text data processing** and techniques to handle **imbalanced datasets**, addressing key machine learning challenges. It emphasizes **model deployment** and **integration** to simulate real-life scenarios, showcasing an end-to-end workflow for building and deploying machine learning applications.

## Notebooks Overview
The `notebooks/` folder contains the following Jupyter notebooks:

1. **EDA.ipynb**: Performs exploratory data analysis to understand the dataset, identify patterns, and uncover features that could improve model performance.
2. **oversampling.ipynb**: Experiments with oversampling techniques (e.g., SMOTE) and undersampling techniques (e.g., TOM Links) to address class imbalance and evaluate their impact on model performance.
3. **spam_notebook.ipynb**: Tests and compares various machine learning models for spam detection, focusing on their accuracy and robustness.
4. **testing.ipynb**: A separate notebook dedicated to testing the final model to ensure no data leakage occurs during evaluation.

## Metrics
Since the dataset is imbalanced, the models were evaluated using **precision**, **recall**, and **F1 score**. These metrics provide a more comprehensive evaluation of model performance compared to accuracy alone.

## Model Accuracy
In this project, the main focus was on **model deployment** and integrating the models with the system. For this purpose, traditional machine learning approaches were used. A **Naive Bayes model** achieved **94% F1 score on cross-validation** and approximately **92.5% F1 score on the test set**, demonstrating strong performance in spam detection.

## Model Deployment and Integration
The model was deployed and integrated into a production environment using **FastAPI**. The classifier and vectorizer were saved using **Pickle** for persistence. To optimize performance, a **Singleton design pattern** was implemented in the server's model class, ensuring that the model is loaded only once during initialization instead of reloading for every prediction. This significantly improved prediction speed and resource efficiency. The model's predictions were served as an **API endpoint** using FastAPI, allowing seamless integration with other systems and applications.

## Dockerization
To ensure consistent deployment across environments, the application was **dockerized** using **Docker**. A `Dockerfile` was created to define the environment, dependencies, and execution steps required to run the application. This allows the application to be easily deployed and scaled in any environment that supports Docker, ensuring reproducibility and simplifying the deployment process.

## Simple Interface
A **simple and user-friendly interface** was developed using **HTML**, **CSS**, and **JavaScript**. This interface allows users to interact with the spam detection model easily. Users can input text, and the interface communicates with the backend API to display the prediction results in real-time. 

<img src="https://github.com/user-attachments/assets/8e401714-c384-48d0-b93d-803b95e55127" alt="Screenshot 2025-02-06 152304" width="60%" />

<img src="https://github.com/user-attachments/assets/e1780cbc-b595-4b3f-bc30-a1905b849f77" alt="Screenshot 2025-02-06 152240" width="60%" />

## References and Research Papers
This project draws some ideas from the following research papers and resources:

1. **Paper 1**: *Content Based Spam Detection In Short Text Messages With Emphasis On Dealing With Imbalanced Datasets*  [Link](https://ieeexplore.ieee.org/abstract/document/8697372)

2. **Paper 2**: *An Integrative Data-Driven Architecture for Online Social Network Spam Detection Using Data Balancing and Machine Learning Methods*[Link](https://www.researchgate.net/profile/Ijeasm-Journal/publication/388174907_An_Integrative_Data-Driven_Architecture_for_Online_Social_Network_Spam_Detection_Using_Data_Balancing_and_Machine_Learning_Methods/links/678d0d9f95e02f182e9fb98b/An-Integrative-Data-Driven-Architecture-for-Online-Social-Network-Spam-Detection-Using-Data-Balancing-and-Machine-Learning-Methods.pdf)

Additionally, summaries and key takeaways from these papers were documented in the paper_notes_and_summary.docs
