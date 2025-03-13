import pandas as pd

#creating a dataset
data=[
    {'student_id': 1, 'name': 'John', 'age': 20, 'marks': 85, 'gender': 'Male'},
    {'student_id': 2, 'name': 'Alice', 'age': 22, 'marks': 78, 'gender': 'Female'},
    {'student_id': 3, 'name': 'Charlie', 'age': None, 'marks': 92, 'gender': 'Male'},
    {'student_id': 4, 'name': 'Rachel', 'age': 21, 'marks': None, 'gender': 'Female'},
    {'student_id': 5, 'name': 'Michael', 'age': 23, 'marks': 88, 'gender': 'Male'},
    {'student_id': 6, 'name': 'Sarah', 'age': None, 'marks': 91, 'gender': 'Female'},
    {'student_id': 7, 'name': 'Jason', 'age': 20, 'marks': 76, 'gender': 'Male'},
    {'student_id': 8, 'name': 'Emma', 'age': 19, 'marks': None, 'gender': 'Female'}
]

#creating a dataframe
df = pd.DataFrame(data)
print(f"Dataframe:\n{df}\n")

#calculating mean,median,mode,variance and standard deviation
mean_age = df['age'].mean()
median_age = df['age'].median()
mode_age = df['age'].mode()[0]
variance_age = df['age'].var()
std_dev_age = df['age'].std()
print("\nStatisitcal Operations:\n")
print(f"Mean: {mean_age}")
print(f"Median: {median_age}")
print(f"Mode: {mode_age}")
print(f"Variance: {variance_age}")
print(f"Standard Deviation: {std_dev_age}\n")

#dropping rows with null values
df_clean = df.dropna(subset=['age', 'marks'])
print(f"After cleaning:\n{df_clean}")
