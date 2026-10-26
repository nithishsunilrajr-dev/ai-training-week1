import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

avg_salary = df.groupby('department')['salary'].mean()
print(avg_salary)
avg_salary.plot(kind='bar')
plt.title('Average Salary by Department')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('average_salary_bar.png')
plt.close()
plt.figure()
plt.hist(df['salary'], bins=5, edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.savefig('salary_histogram.png')
plt.close()
plt.figure()


for department, group in df.groupby('department'):
    plt.scatter(group['id'], group['salary'], label=department)


plt.title('Employee ID vs Salary')
plt.xlabel('Employee ID')
plt.ylabel('Salary')
plt.legend()
plt.tight_layout()
plt.savefig('salary_scatter.png')
plt.show()