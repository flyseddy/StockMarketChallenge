from csv import writer
from price import price
from listofstocks import stockslist
from eps import eps
from pe_ratio import pe_ratio

# Create instances of the imported lists
list_of_stocks = stockslist()
stock_prices = price()
eps_list = eps()
ratio_list = pe_ratio()


with open('live_stock_info2.csv', 'w') as f:
    csv_writer = writer(f)
    headers = ['Company', 'Stock Price', 'EPS', 'P/E Ratio']
    csv_writer.writerow(headers)
    # For loop that iterates over the length of this list to write each stock and its price
    for i in range(len(list_of_stocks)):
        try:
            csv_writer.writerow([list_of_stocks[i], stock_prices[i], eps_list[i], ratio_list[i]])
        except IndexError:
            csv_writer.writerow([list_of_stocks[i], stock_prices[i]])
        else:
            continue
