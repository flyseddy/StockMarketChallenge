from csv import writer
from price import price
from listofstocks import stockslist

# Create instances of the imported lists
list_of_stocks = stockslist()
stock_prices = price()

with open('live_stock_info.csv', 'w') as f:
    csv_writer = writer(f)
    headers = ['Company', 'Stock Price']
    csv_writer.writerow(headers)
    # For loop that iterates over the length of this list to write each stock and its price
    for i in range(len(list_of_stocks)):
        csv_writer.writerow([list_of_stocks[i], stock_prices[i]])
