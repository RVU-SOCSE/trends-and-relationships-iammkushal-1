import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r'C:/Users/RVUW241/Downloads/laptops.csv.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Check columns
print(df.columns)

# Plot
plt.plot(df['YearsExperience'], df['Salary'], marker='o')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.show()
