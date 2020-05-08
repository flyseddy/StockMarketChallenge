"""
Author: Sedrick Thomas
Created: May 7th 2020
I developed a method to extract the current P/E ratio (if available) of each stock
and return them as a list

To use this module***

from pe_ratio import p_e_ratio

# Create an instance for the list
pe_ratio_list = p_e_ratio()

Now you are ready use this list
"""



import requests
from bs4 import BeautifulSoup
from listofstocks import stockslist

# List of P/E ratios
pe_list = []
def p_e_ratio():
    # Create an instance of the list
    list_of_stocks = stockslist()
    for symbol in list_of_stocks:
        # For each symbol in the list of stock symbols ex. AAPL
        list_empty = []
        url = f'https://financialmodelingprep.com/financial-summary/{symbol}'
        r = requests.get(url)
        # Request url with the compnay name
        soup = BeautifulSoup(r.text, 'html.parser')
        containers = soup.find_all('tbody')
        # Scrapes the <tbody> tag for the required infromation
        primary = containers[1]
        # Takes the second index [1] of containers
        for item in primary:
            # For each item in this list of items ex. P/E ratio, ROA, Debt/Equity
            list_empty.append(item)
            # Add each item to list

        p_e = list_empty[12].get_text()
        # Get the 13th index [12] which is P/E Ratio
        pe_list.append(p_e)
        # Add the P/E ratio to the list of other P/E ratios
        list_empty.clear()
        # Clear the list so we can do this process over again for each symbol
    
    return pe_list


