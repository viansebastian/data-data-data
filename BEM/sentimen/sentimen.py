import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
data = pd.read_excel('sentimen_bersih.xlsx')

# Extract the desired column
column = data['Sentiment']

# Create a pie chart
plt.pie(column, labels=column.index, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures a circular pie chart

# Display the chart
plt.show()
