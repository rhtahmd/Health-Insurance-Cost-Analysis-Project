# Health-Insurance-Cost-Analysis-Project

# Introduction:

In this project, my goal was to analyze a health insurance dataset to understand the factors that influence the charges imposed on individuals. The dataset, sourced from Kaggle, consists of various attributes such as age, gender, body mass index (BMI), number of children, smoking habits, and geographical region.

# Dataset Description:

The dataset obtained from Kaggle consists of 1338 records, with each record representing an individual policyholder. It includes seven features:

Age: The age of the primary beneficiary.
Sex: The policyholder's gender, represented as male or female.
BMI: The body mass index, providing an understanding of body weights that are relatively high or low relative to height.
Children: The number of dependents covered by the insurance plan.
Smoker: Whether the policyholder is a smoker or not.
Region: The beneficiary's residential area in the US, divided into four geographic regions - northeast, southeast, southwest, or northwest.
Charges: Individual medical costs billed by health insurance.
Tools and Packages:

# To accomplish this project, I utilized several tools and libraries:

Python: The primary programming language for this project.
Pandas and Numpy: For data manipulation and analysis.
SQLite: For SQL-based data querying.
Statsmodels: For building a statistical model to analyze relationships between variables.
Matplotlib and Seaborn: For data visualization in Python.
Scikit-learn: For preprocessing and machine learning.
Power BI: For advanced data visualization and analysis.

# Methodology:

I began the project by cleaning and preparing the data using the Pandas library. This included removing any unnecessary spaces from column names and ensuring data consistency.

Once the data was cleaned, I created a SQLite database to store the dataset, which facilitated the process of querying the data using SQL. I ran various SQL queries to understand the average charges by different criteria such as age groups, BMI categories, the number of children, and smoker status. The results of these queries were then exported to separate CSV files for further analysis and visualization.

I then transitioned into more advanced statistical modeling using Statsmodels for an ordinary least squares (OLS) regression. This regression model was useful in analyzing the relationship between the various factors and the insurance charges.

Next, I moved onto visualizing the results using Python libraries initially and later using Power BI. Power BI allowed me to create more interactive and dynamic visualizations that helped in further interpreting and presenting the results.

# Results and Discussion:

The SQL queries returned insightful information regarding the average charges based on various factors. These findings were further substantiated by the results from the regression analysis:

Age: An increase of $257 in charges can be expected for each additional year of age.
BMI: Charges increase by approximately $333 for each unit increase in BMI.
Smoker: Smokers are charged an extra $23,820 on average compared to non-smokers.
Children: Each additional child leads to an expected increase of $479 in charges.
Region: The impact of region on insurance charges, while present, is relatively small.

# Conclusion:

This analysis has allowed me to determine that age, BMI, smoking habits, and the number of children significantly influence the health insurance charges. Interestingly, the model suggests that gender does not have a significant impact on
