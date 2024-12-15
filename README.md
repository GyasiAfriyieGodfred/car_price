#Car Price Prediction using Machine Learning

This project focuses on building machine learning models to predict car prices based on various features such as the car's model,make, age, torque,MPH_time and more.Accurate 
price prediction is crucial for buyers and sellers and dealerships to make informed decisions. The project demonstrates complete machine learning pipeline, including:
Data preprocessing, Feature engineering, Outlier removal, Feature encoding,Model Training and Evaluation and Creating GUI for easy application of the model.
#Key features
Exploratory Data Analysis (EDA):Visualizations and statistical analysis to understand the relationships between features and target variable(car price).
Outliers Handling: Identification and removal of outliers using percentile based filtering to improve model performance.
Feature Encoding:Conversion of categorical features using Ordinal Enconder.
Model selection: Implementation and comparison of several regression models such as Decision Tree Regressor,Random Forest Regressor and Linear regression
Performance Metrics: Models evaluated using R2SCore , means squared error and mean absolute error
Dataset : The data was derived from Kaggle. it contains details about 'Car Make', 'Car Model', 'Year', 'Engine Size (L)', 'Horsepower',
       'Torque (lb-ft)', '0-60 MPH Time (seconds)' which make up the independent variables whilst 'Price (in USD) is the target variable.
#Result
The best performing model is the Random Forest Regressor with the following metrics:
R square value: 0.946591
Mean squared Error:484681193.3723266
Mean Absolute Error:9089.490288853163
A detailed comparison of the model can be found in the folder.
