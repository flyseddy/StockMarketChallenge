"""
Author: Sedrick Thomas
Created at: May 7th 2020

This is basically the file that writes all the information that we calculated in the 
other modules to a CSV file to be read and interpreted. There may be a few values that
don't return a value due to the inaccessibilty of those items from scraping those websites
"""


from csv import writer
from price import price
from listofstocks import stockslist
from pe_ratio import p_e_ratio

# Create instances of the imported lists
list_of_stocks = stockslist()
stock_prices = price()
ratio_list = p_e_ratio()


with open('live_stock_more_info.csv', 'w') as f:
    csv_writer = writer(f)
    headers = ['Company', 'Stock Price', 'P/E Ratio']
    csv_writer.writerow(headers)
    # For loop that iterates over the length of this list to write each stock and its price
    for i in range(len(list_of_stocks)):
        try:
            csv_writer.writerow([list_of_stocks[i], stock_prices[i], ratio_list[i]])
        except IndexError:
            csv_writer.writerow([list_of_stocks[i], stock_prices[i], 'null'])
        else:
            continue
