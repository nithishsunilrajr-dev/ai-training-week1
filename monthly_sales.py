import pandas as pd
import matplotlib.pyplot as plt


# Sample monthly sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [12000, 15000, 13000, 18000, 20000, 25000]
}


df = pd.DataFrame(data)


# Create line chart
plt.plot(df['Month'], df['Sales'], marker='o')


plt.title('Monthly Sales Line Chart')
plt.xlabel('Month')
plt.ylabel('Sales')


plt.grid(True)
plt.tight_layout()


# Save chart
plt.savefig('monthly_sales.png')


# Display chart
plt.show()