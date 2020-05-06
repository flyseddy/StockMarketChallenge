from listofstocks import stockslist
import requests

def price():
    new_list = stockslist()
    stock_prices = []
    # For each symbol in the list we will append it on the last part of the url to retrieve api for specific company
    for item in new_list:
        url = f'https://financialmodelingprep.com/api/v3/company/profile/{item}'
        r = requests.get(url)
        # Process api page as a json
        stock_dict = r.json()
        # Find the price by indexing the dictionary
        price = stock_dict['profile']['price']
        # Append all the stock prices to the list of all stock prices for all the companies
        stock_prices.append(price)

    return stock_prices

       