# Import necessary libraries
import sqlite3
import pandas as pd

# Step 1: Load Data from CSV file into a pandas DataFrame
df = pd.read_csv('C:\\Project 1\\insurance.csv')

# Step 2: Data Cleanup - Trim unnecessary spaces in column names
df.columns = df.columns.str.strip()

# Step 3: Create a connection to SQLite database
connection = sqlite3.connect('insurance.db')

# Step 4: Load data from pandas DataFrame to SQLite database
df.to_sql('insurance', connection, if_exists='replace')

# Create a connection to your SQLite database
conn = sqlite3.connect('insurance.db')

# Step 5: Write SQL query to find average charges of smokers vs non-smokers
query = """
SELECT 
    smoker, 
    AVG(charges) AS avg_charges
FROM 
    insurance
GROUP BY 
    smoker;
"""
# Execute the SQL query and load the result into a DataFrame
df = pd.read_sql_query(query, conn)

# Export the DataFrame to a CSV file
df.to_csv('avg_charges_by_smokers.csv', index=False)

# Step 6: Write SQL query to find average charges by age groups (in 10 years increment)
query_age = """
SELECT 
    CASE
        WHEN age BETWEEN 18 AND 28 THEN '18-28'
        WHEN age BETWEEN 29 AND 39 THEN '29-39'
        WHEN age BETWEEN 40 AND 50 THEN '40-50'
        WHEN age BETWEEN 51 AND 61 THEN '51-61'
        ELSE '62 and above'
    END AS age_group,
    AVG(charges) AS avg_charges
FROM 
    insurance
GROUP BY 
    age_group;
"""
# Execute the SQL query and load the result into a DataFrame
df_age = pd.read_sql_query(query_age, conn)
# Export the DataFrame to a CSV file
df_age.to_csv('average_charges_by_age.csv', index=False)

# Step 7: Write SQL query to find average charges by BMI categories
query_bmi = """
SELECT 
    CASE
        WHEN bmi BETWEEN 18.5 AND 24.9 THEN 'Healthy'
        WHEN bmi BETWEEN 25 AND 29.9 THEN 'Overweight'
        ELSE 'Obese'
    END AS bmi_category,
    AVG(charges) AS avg_charges
FROM 
    insurance
GROUP BY 
    bmi_category;
"""
# Execute the SQL query and load the result into a DataFrame
df_bmi = pd.read_sql_query(query_bmi, conn)
# Export the DataFrame to a CSV file
df_bmi.to_csv('average_charges_by_bmi_category.csv', index=False)

# Step 8: Write SQL query to find average charges by number of children
query_children = """
SELECT 
    children,
    AVG(charges) AS avg_charges
FROM 
    insurance
GROUP BY 
    children;
"""
# Execute the SQL query and load the result into a DataFrame
df_children = pd.read_sql_query(query_children, conn)
# Export the DataFrame to a CSV file
df_children.to_csv('average_charges_by_children.csv', index=False)

# Step 9: Write SQL query to find average charges by region
query_region = """
SELECT 
    region,
    AVG(charges) AS avg_charges
FROM 
    insurance
GROUP BY 
    region;
"""
# Execute the SQL query and load the result into a DataFrame
df_region = pd.read_sql_query(query_region, conn)
# Export the DataFrame to a CSV file
df_region.to_csv('average_charges_by_region.csv', index=False)

# Step 10: Write SQL query to select age and charges for each participant and whether they are a smoker or not
query = """
SELECT 
    age,
    CASE 
        WHEN smoker = 'yes' THEN 1
        ELSE 0
    END AS is_smoker,
    charges
FROM 
    insurance
ORDER BY
    age;
"""
# Execute the SQL query and load the result into a DataFrame
df = pd.read_sql_query(query, conn)
# Export the DataFrame to a CSV file
df.to_csv('charges_by_multiple_factors.csv', index=False)
