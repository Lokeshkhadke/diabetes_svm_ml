# -*- coding: utf-8 -*-
"""BOSTON HOUSE PRICE PREDICTION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A2AmjdDO0Y1ccNIpClxY3ST7Fg1xd2vg

**Boston House Price Prediction**  

In this project, I have built a machine learning model to predict house prices using two different algorithms:  
1. **Linear Regression**  
2. **XGBoost Regression**  

Since this is a **regression problem**, the task involves predicting continuous numerical values (house prices) based on input features like the number of rooms, crime rate, and more. This approach allows us to understand how these features influence house prices and make accurate predictions for unseen data.
"""

#IMPORTING NECESSARY LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor

#IMPORTING DATASET
House_price_dataset = pd.read_csv('/content/BostonHousing.csv')

print(House_price_dataset)

#DISPLAY FIRST FEW ROWS TO VERIFY THE IMPORT
print(House_price_dataset.head())

"""This dataset contains **506 records** and **14 features**, representing various characteristics of homes located in Boston. Each feature provides specific information, such as the number of rooms, crime rate, and property tax, which can help predict house prices in the area.

### Steps of Steps by Step Approch in the Project:

1. **Collecting Data**  
   The first step is gathering the dataset, which contains information about various homes in Boston, such as features like the number of rooms, crime rates, etc., that will help us predict house prices.

2. **Pre-processing Data**  
   The data is not yet ready to be fed into a machine learning model. Pre-processing is required to clean and format the data, handle missing values, and scale the features so the model can process them effectively.

3. **Exploratory Data Analysis (EDA)**  
   In this step, we analyze the dataset to understand the relationships between features. For example, we find correlations between different features (like the number of rooms or crime rates) to see which ones are most closely related to the target variable (house prices).

4. **Splitting Data into Train-Test Split**  
   The data is divided into two sets: one for training the model (training set) and the other for testing the model's performance (test set). This helps ensure the model generalizes well to unseen data.

5. **Feeding the Data to XGBoost Regressor for Prediction**  
   The training data is used to train the **XGBoost Regressor** model, which makes predictions on the test data. This model is known for its efficiency and accuracy in regression tasks.

6. **Evaluation**  
   Finally, the model's performance is evaluated by comparing its predictions with the actual values using metrics like Mean Squared Error (MSE) and R-squared (R²). This step helps us assess how well the model is performing and whether it is a good fit for the problem.
"""

#DISPLAY LAST FEW ROWS
print(House_price_dataset.tail())

House_price_dataset.shape

House_price_dataset.isnull().sum()

House_price_dataset.describe()

correlation = House_price_dataset.corr()

# constructing a heatmap to understand the correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size':8}, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show

"""Splitting the data into train_test_split"""

# Separate features and target variable
X = House_price_dataset.drop(columns=['medv'])  # Replace 'medv' with the correct target column name in your dataset
Y = House_price_dataset['medv']

print(X)

"""**Note:**  
The target variable, which represents house prices, was previously named `'MEDV'` in the dataset. Additionally, the prices are in thousands, meaning that the values in the dataset represent the house prices in thousands of dollars. For example, a predicted price of `25` represents `25,000` dollars. Always remember to multiply by 1,000 when interpreting the actual house price.
"""

print(Y)

"""Splitting the data into train test split"""

X_train , X_test , Y_train , Y_test =train_test_split(X,Y,test_size=0.2,random_state=42)

print(X.shape,X_train.shape,X_test.shape)

"""Standardize the data (optional but recommended for models sensitive to scale)

Standardizing the data is an important step, especially for models like Linear Regression and XGBoost that are sensitive to the scale of the features. Standardization ensures that each feature has a mean of 0 and a standard deviation of 1, which helps the model converge faster and improves performance.

**Why standardizing?**

Some machine learning models (like Linear Regression) are sensitive to the scale of the data. If the features vary widely (e.g., one feature ranges from 1 to 10 and another ranges from 1,000 to 100,000), the model might struggle to learn effectively.
By standardizing the data, all features will contribute equally, allowing the model to learn more efficiently.
"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""now we Train the machine learning model
by using
**1)linear regression** and then by
**2)by xgboost regressor**

**1)By using Linear Regression**
"""

model = LinearRegression()
model.fit(X_train_scaled,Y_train)

# Making predictions
y_pred = model.predict(X_test_scaled)

# Evaluating the model
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(Y_test, y_pred)
r2 = r2_score(Y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2 Score): {r2:.2f}")

#Visualize Predictions
plt.figure(figsize=(8, 6))
plt.scatter(Y_test, y_pred, alpha=0.6, color='blue')
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linestyle='--')
plt.title("Actual vs Predicted Prices")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.show()

"""now we train model by using xgboost regressor"""

# loading the model
model = XGBRegressor()

# training the model with X_train
model.fit(X_train, Y_train)

"""evaluating the model by making prediction on training data"""

# accuracy for prediction on training data
training_data_prediction = model.predict(X_train)

print(training_data_prediction)

"""Now we find r squared error and mean absolute error which are evaluation metrics.
In the step below we import performance Evaluation metrics like  **mean_squared_error, r2_score** for Model Evaluation.The two key evaluation metrics used here are mean absolute error and R-squared error.they are important for determinig how well a regression model predicts target variables.In the above Model we predict yield(target variable) based on DOY(day of year).
the Error Metrics are discussed below


1) **Mean_squared_error** : Mean Squared Error (MSE) is a measure used metric to calculate and compute the performance of a regression model. It is the average of the squares of the errors, that are the differences in the actual and predicted values.Smaller the MSE, the better the model's predictions are, because it indicates less deviation from the actual values.

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (\text{Actual}_i - \text{Predicted}_i)^2
$$

MSE indicates how much is the deviation in  model's predictions are from the actual values.If the MSE is low,the model's predictions are more aligned with the true values. If it's high, the model is less accurate.


Why Square the Errors?: **Squaring the errors ensures that the model penalizes larger mistakes** more heavily than smaller ones, which helps the model focus on minimizing large errors and improving overall accuracy.

2) **r2_score** : r2_score is used for regression problems.It is used when we want to know how well the Model fits the overall data and understand relationship between between values of X and Y axis.


$$
R^2 = 1 - \frac{\sum_{i=1}^{n} (y_{\text{true}, i} - y_{\text{pred}, i})^2}{\sum_{i=1}^{n} (y_{\text{true}, i} - \bar{y_{\text{true}}})^2}
$$

   
   **Value of R² lies between 0 to 1** where **0 indicates bad relationship** and values close to **1 indicates perfect fit.** **sklearn** model helps to commute the values.For both linear regression and polyniomial regression values which is higher is preffered.

   For Polynomail regression ,high r2_score value is good but watch MSE/RMSE carefullyfor the sign of overfitting,especailly in highere polynomial degree.


   In **Conclusion** R² provides a relative measure of how well the model captures the variance in the data. By using these two metrics, you can evaluate the performance of each model, compare different regression techniques, and understand whether the model is underfitting or overfitting the data. and Higher the R² ,more acceptable the model and lower the MSE better  model.
"""

# R squared error
score_1 = metrics.r2_score(Y_train, training_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)

"""Visualizing the actual Prices and predicted prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Price vs Preicted Price")
plt.show()

"""Now predicting on test data."""

# accuracy for prediction on test data
test_data_prediction = model.predict(X_test)

# R squared error
score_1 = metrics.r2_score(Y_test, test_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)

"""**Conclusion**

The Boston Housing dataset is used to predict house prices using, first, a baseline of linear regression and, later on, an improved model of XGBoost.

**Linear Regression Model:**
To start with, we used a **Linear Regression** model. It gave us the following results:
• **R-squared value:** 0.8724
• **Mean Absolute Error (MAE):** 2.7099 (on the test set)

These results show that the Linear Regression model generalizes fairly well to the task of house price prediction, with the model explaining about 87% of the variance in the data. The performance was far from perfect, though, with quite a significant room for improvement as evidenced by the relatively high MAE. That implied the model was not able to grasp the complex relationships between the features and the target variable, house prices.

#### XGBoost Model:
To overcome the limitations of Linear Regression, we have moved on to use the **XGBoost Regressor**-one of the power machine learning algorithms that can handle the non-linear relationship between target and predictor variables along with sophisticated patterns in the data. The result for XGBoost was as follows :
Training R-squared value = 0.999997
Training MAE = 0.0112
Test R-squared value = 0.9058
Test MAE = 1.8909

The XGBoost model showed a massive improvement from Linear Regression, with the R-squared perfect in training. The performance on the test was also very strong, at an R-squared of 0.9058, indicating that over 90% of the variance in the test set was explained by the model. The MAE was way lower compared to Linear Regression, which indicated much more accurate predictions.

However, the XGBoost model's performance on the test set was not as perfect as the training set, which is typical of machine learning models. This slight decrease in performance suggests potential **overfitting**, where the model is overly tuned to the training data and may not generalize as well on unseen data.

**Room for Improvement:**

Despite the strong performance of the XGBoost model, there are still areas for improvement:
1. **Overfitting:** The model performed extremely well on the training set, whereas for the test set, performance was slightly lower, which might indicate overfitting. We can try techniques like **cross-validation** to help generalize better on unseen data or tune the hyperparameters.
2. **Hyperparameter Tuning:** The performance of XGBoost can be further enhanced by the use of different **hyperparameter optimization techniques** such as Grid Search or Random Search to find the most suitable set of parameters.

3. **Feature Engineering:** Inclusion of other relevant features or removal of a few irrelevant or redundant ones may further improve the accuracy. Feature interaction and transformation may also yield better results in improving the predictive capability of the model.

4. **Model Comparison:** Although XGBoost outperformed Linear Regression, it would be useful to compare its results with other models such as **Random Forests** or **Gradient Boosting Machines** just to verify that XGBoost is truly the best model for this problem.


**Conclusion** - We can see that we actually improved significantly in predicting house prices by moving from Linear Regression to XGBoost. The XGBoost model gave excellent performance, especially on lower error rates; however, steps for improving its generalization by preventing overfitting can include tuning its hyperparameters, applying regularization, and cross-validation. This project demonstrates the application of a more advanced machine learning model like XGBoost compared to the Linear Regression method; however, there can be a continuous refinement and optimization.
"""