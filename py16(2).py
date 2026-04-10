import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/RVUW241/Downloads/laptops.csv.csv')

plt.scatter(df['YearsExperience'], df['Salary'])
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Scatter Plot (Matplotlib)")
plt.show()

sns.scatterplot(x=df['YearsExperience'], y=df['Salary'])
plt.title("Scatter Plot (Seaborn)")
plt.show()
