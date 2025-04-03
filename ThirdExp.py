import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
data = {'age': [20, 22, 30, 21, 23, 80, 20, 19],  
        'marks': [85, 78, 92, 73, 88, 91, 76, 10]}  

df = pd.DataFrame(data)  
df_cleaned = df[df['marks'] >= 20]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(y=df['marks'], ax=axes[0])
axes[0].set_title("Boxplot of Marks (Original Data)")

sns.boxplot(y=df_cleaned['marks'], ax=axes[1])
axes[1].set_title("Boxplot After Removing Outliers")

plt.show()
