import pandas as pd

# Function to calculate volatility percentage
def calculate_volatility(data):
    data['Volatility'] = (data['High'] - data['Low']) / data['Close'] * 100
    return data['Volatility']

# 1. Select two similar financial instruments (e.g., stocks)
instrument1 = 'AAPL'  # Replace with your desired symbol
instrument2 = 'MSFT'  # Replace with your desired symbol

# 2. Download daily data for two years (adjust the start and end dates as needed)
start_date = '2019-06-07'
end_date = '2021-06-07'

# Assuming you have historical stock data files in CSV format, named 'AAPL.csv' and 'MSFT.csv', for example
# You may need to adjust the CSV file names accordingly
data1 = pd.read_csv('AAPL.csv')
data2 = pd.read_csv('MSFT.csv')

# Filter data for the specified date range
data1 = data1[(data1['Date'] >= start_date) & (data1['Date'] <= end_date)]
data2 = data2[(data2['Date'] >= start_date) & (data2['Date'] <= end_date)]

# 3. Calculate volatility for each instrument
volatility1 = calculate_volatility(data1)
volatility2 = calculate_volatility(data2)

# 4. Convert volatility values to percentage with 2 decimal places
volatility1_percentage = volatility1.round(2)
volatility2_percentage = volatility2.round(2)

# 5. Analyze the difference in volatility between the two instruments
volatility_diff = volatility1 - volatility2

# Print the results
print("Volatility of", instrument1, ":", volatility1_percentage)
print("Volatility of", instrument2, ":", volatility2_percentage)
print("Difference in volatility between", instrument1, "and", instrument2, ":", volatility_diff)
