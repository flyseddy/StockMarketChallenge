from csv import writer
from price import price
from listofstocks import stockslist

list_of_stocks = stockslist()
stock_prices = price()

with open('live_stock_info.csv', 'w') as f:
    csv_writer = writer(f)
    headers = ['Company', 'Stock Price']
    csv_writer.writerow(headers)

    for i in range(len(list_of_stocks)):
        csv_writer.writerow([list_of_stocks[i], stock_prices[i]])
