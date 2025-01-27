# Telecom Churn Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\Omantel_Aspire\My Learning\Data Scientist\Git Hub\Telecom Churn.csv'  # Path to the dataset
telecom_churn_data = pd.read_csv(file_path)

# Data Cleaning
# Convert 'TotalCharges' to numeric and handle missing values
telecom_churn_data['TotalCharges'] = pd.to_numeric(telecom_churn_data['TotalCharges'], errors='coerce')
telecom_churn_data.dropna(subset=['TotalCharges'], inplace=True)
telecom_churn_data['Churn'] = telecom_churn_data['Churn'].map({'Yes': 1, 'No': 0})

# EDA
sns.set(style="whitegrid")

# Churn Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Churn', hue='Churn', data=telecom_churn_data, palette='coolwarm', dodge=False)
plt.title("Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# Correlation Heatmap (numeric columns only)
plt.figure(figsize=(10, 8))
correlation = telecom_churn_data.select_dtypes(include=['number']).corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Tenure vs. Churn
plt.figure(figsize=(8, 6))
sns.histplot(data=telecom_churn_data, x="tenure", hue="Churn", multiple="stack", bins=30, palette="coolwarm")
plt.title("Tenure vs. Churn")
plt.xlabel("Tenure (months)")
plt.ylabel("Count")
plt.show()

# Monthly Charges by Churn
plt.figure(figsize=(8, 6))
sns.boxplot(x="Churn", y="MonthlyCharges", data=telecom_churn_data, palette="coolwarm")
plt.title("Monthly Charges by Churn")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Monthly Charges ($)")
plt.show()

# Save cleaned dataset for further analysis
telecom_churn_data.to_csv('Cleaned_Telecom_Churn.csv', index=False)

# End of script




