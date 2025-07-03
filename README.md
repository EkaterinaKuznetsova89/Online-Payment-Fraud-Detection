# Online-Payment-Fraud-Detection

The project focuses on detecting fraudulent payments using machine learning techniques. It involves end-to-end steps from data exploration and preprocessing to model development and evaluation. The final goal is to build a reliable fraud detection model that can distinguish between legitimate and fraudulent transactions.

Source used: https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset/data
It's probably the subset of: https://www.kaggle.com/datasets/vardhansiramdasu/fraudulent-transactions-prediction?sort=published


Details: 
The dataset contains transaction-level information with labelled classes:
- Not fraud(0) for legitimate and  fraud (1) transactions
- covering features such as transaction type
- amount
- balances before and after the transaction
- recipient of the transaction
- balances before and after the transaction

Implementation:
- Data Exploration & Visualisation: Understand data distributions, class imbalances and correlations.
- Model Development - Supervised Learning Technique:
* Logistic Regression 
* Random Forest + using SMOTE and SMOTE-Tomek
* XGBoost + using SMOTE and SMOTE-Tomek
- Model Evaluation 
- The best model used in the app Streamlit
- Conclusions & Insights


Extra materials used:
https://maikpaixao.medium.com/dealing-with-imbalanced-datasets-in-fraud-detection-c8ab5ce4b1f3
https://www.feedzai.com/blog/fraud-data-analytics/
