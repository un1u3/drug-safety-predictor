# Drug-Safety-Predictor

This project builds and evaluates a machine learning model to predict whether a patient will be hospitalized based on clinical and drug-related data.

---

## Project Overview

- **Goal:** Predict hospitalization status (0 = not hospitalized, 1 = hospitalized) from patient features.
- **Data:** Includes features like age, sex, drug exposure, reaction types, and other clinical indicators.
- **Model:** Random Forest classifier (can be changed to other models).
- **Challenge:** Imbalanced dataset with more non-hospitalized cases.

---

## Important Note About Model Performance

The current model has **limited ability to correctly identify hospitalized patients** (minority class).  
- It achieves good accuracy overall but has **low recall (~32%) for hospitalized cases**, meaning it misses many true positives.  
- This model **should not be used as a sole decision-maker in clinical settings** without further improvement.  
- Use it only as a supportive tool and continue working on improving recall, collecting more data, or using advanced modeling techniques.

---

## How to Use

### 1. Data Preparation

- Clean and preprocess raw data.
- Handle missing values.
- Encode categorical variables and generate binary columns for drugs and reactions.
- Split data into train and test sets.

### 2. Training the Model

- Train the Random Forest classifier with class imbalance handling (`class_weight='balanced'` or using SMOTE).
- Save the trained model and feature columns list.

### 3. Testing the Model

- Load the saved model and feature columns.
- Prepare the test dataset with the same preprocessing.
- Align test data columns to training columns.
- Predict hospitalization on test data.
- Evaluate performance using accuracy, precision, recall, and F1-score.

---

## Running the Code

1. **Tr**
