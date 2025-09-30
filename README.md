# ANN-Classification-Churn-Prediction

# ANN Classification with Hyperparameter Tuning

This project implements an **Artificial Neural Network (ANN)** for **binary classification** using **TensorFlow/Keras** and **Scikit-Learn**.  
In addition to building the ANN, the project also applies **Hyperparameter Tuning** using **GridSearchCV** with the **SciKeras wrapper** to find the best model configuration.

---

## 🚀 Project Overview
- **Dataset**: Preprocessed dataset with both categorical (e.g., `Geography`) and numerical features.
- **Task**: Binary classification (predicting a target class: 0 or 1).
- **Goal**: Build an ANN and optimize its performance by tuning hyperparameters such as:
  - Number of neurons in hidden layers
  - Number of hidden layers
  - Batch size
  - Number of epochs

---

## 🛠 Features
- **Data Preprocessing**:
  - One-Hot Encoding of categorical features.
  - Feature Scaling using `StandardScaler`.
- **Model Creation**:
  - Function `create_models(neurons, layers)` builds a flexible ANN.
  - Architecture:  
    - Input Layer: Features from dataset.  
    - Hidden Layers: ReLU activation, tunable neurons and depth.  
    - Output Layer: Sigmoid activation (binary classification).  
- **Hyperparameter Tuning**:
  - GridSearchCV tested combinations of:
    - `neurons` = [16, 32, 64]
    - `layers` = [1, 2, 3]
    - `fit__batch_size` = [10, 32]
    - `fit__epochs` = [20, 50]
  - Best configuration is selected based on cross-validation accuracy.
- **Evaluation**:
  - Reports best accuracy and corresponding hyperparameters.

---

## 📂 Project Structure
📦 ANN_Classification_Project1
┣ 📜 data/ # Dataset files
┣ 📜 notebooks/ # Jupyter notebooks (EDA, preprocessing, model building)
┣ 📜 models/ # Saved ANN models
┣ 📜 requirements.txt # Project dependencies
┣ 📜 README.md # Project documentation
┗ 📜 main.py / notebook.ipynb # Main training script/notebook