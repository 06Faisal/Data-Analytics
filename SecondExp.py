import pandas as pd

data = [
    {'student_id': 1, 'name': 'John', 'age': 20, 'marks': 85, 'gender': 'Male'},
    {'student_id': 2, 'name': 'Alice', 'age': 22, 'marks': 78, 'gender': 'Female'},
    {'student_id': 3, 'name': 'Charlie', 'age': None, 'marks': 92, 'gender': 'Male'},
    {'student_id': 4, 'name': 'Rachel', 'age': 21, 'marks': None, 'gender': 'Female'},
    {'student_id': 5, 'name': 'Michael', 'age': 23, 'marks': 88, 'gender': 'Male'},
    {'student_id': 6, 'name': 'Sarah', 'age': None, 'marks': 91, 'gender': 'Female'},
    {'student_id': 7, 'name': 'Jason', 'age': 20, 'marks': 76, 'gender': 'Male'},
    {'student_id': 8, 'name': 'Emma', 'age': 19, 'marks': None, 'gender': 'Female'}
]

df = pd.DataFrame(data)

subset_labels = df[['name', 'age', 'marks']]  
subset_positional = df.iloc[2:6] 

# Aggregation
aggregation_results = df.agg({
    'age': ['mean', 'min', 'max'],
    'marks': ['mean', 'sum', 'count']
})

# Grouping by gender and applying aggregation
grouped_results = df.groupby('gender').agg({
    'age': ['mean', 'count'],
    'marks': ['mean', 'count']
})

print("Subset based on labels:")
print(subset_labels)
print("\nSubset based on positional indexing:")
print(subset_positional)
print("\nAggregation Results:")
print(aggregation_results)
print("\nGrouped Results:")
print(grouped_results)
