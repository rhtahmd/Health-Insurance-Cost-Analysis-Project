import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder

# Assuming you have a CSV file of your data
df = pd.read_csv('insurance.csv')

# Convert categorical variables to numerical variables
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex']) # Male:1, Female:0
df['smoker'] = le.fit_transform(df['smoker']) # Yes:1, No:0
df['region'] = le.fit_transform(df['region']) # Each unique region value will be assigned a unique integer

# Define the dependent variable (y) and independent variables (X)
X = df[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = df['charges']

# Add a constant to the independent value
X1 = sm.add_constant(X)

# Make regression model 
model = sm.OLS(y, X1)

# Fit model and print results
results = model.fit()
print(results.summary())
