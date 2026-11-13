
# Research Document Mining

## 1. Project Overview

This project focuses on applying data science and machine learning techniques to research document analysis. It explores text preprocessing, classification, text summarisation, and topic modelling to extract useful information from research documents.

The project was completed as part of the ITNP assignment.

## 2. Project Objectives

The main objectives are:

- To preprocess and prepare research abstracts for machine learning.
- To develop and evaluate machine learning models for research paper classification.
- To improve predictive performance through an additional machine learning technique.
- To implement a web-based research paper classification application.
- To apply TextRank and Latent Semantic Analysis (LSA) for text summarisation.
- To use Latent Dirichlet Allocation (LDA) to identify topics and explore topic distributions.

## 3. Repository Structure

- `documentation/` - Completed assignment documentation.
- `datasets/` - Datasets used throughout the project.
- `notebooks/` - Jupyter notebooks containing the code and outputs for Questions 1–4.
- `deployment/` - Streamlit application, trained model, dependencies and deployment instructions.
- `outputs/` - Generated visualisations and topic-modelling outputs.

## 4. Questions and Methodologies

### Question 1: Research Paper Classification

The research abstracts dataset was cleaned and preprocessed. TF-IDF was used to convert the text into numerical features. A Logistic Regression baseline model was trained and evaluated.

### Question 2: Machine Learning Models and Deployment

Four machine learning models were trained and evaluated. An additional technique was applied to address class imbalance. The selected model was saved and used in a Streamlit web application for research paper classification.

### Question 3: Research Document Summarisation

TextRank and Latent Semantic Analysis (LSA) were applied to the research corpus to identify important sentences and terms. Visualisations were generated to present the summarisation results.

### Question 4: Topic Modelling

Latent Dirichlet Allocation (LDA) was used to identify topics within the research corpus. Topic-word distributions and document-topic distributions were generated. An interactive topic visualisation was created using pyLDAvis.

## 5. Technologies and Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Matplotlib
- NetworkX
- Streamlit
- Joblib
- pyLDAvis
- Jupyter Notebook

## 6. Datasets

The project uses the following datasets:

- `research_abstracts.json` - Research abstracts used for classification.
- `research_corpus.zip` - Collection of research documents used for summarisation and topic modelling.

## 7. Running the Notebooks

Open the notebooks using Jupyter Notebook or JupyterLab.

Run each notebook from top to bottom to reproduce the relevant preprocessing, modelling, evaluation and visualisation steps.

Ensure that the required Python libraries are installed and that the datasets are available in the `datasets/` directory.

## 8. Deployment

The research paper classification application is located in the `deployment/` folder.

Refer to `deployment/README.md` for installation instructions and details on running the Streamlit application.
