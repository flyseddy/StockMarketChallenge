import requests
from csv import writer
from bs4 import BeautifulSoup

def stockslist():
    
    url = 'https://www.slickcharts.com/sp500'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    # Finds all horizontal sections of the website listed above
    list = soup.find_all('tr')
    list_of_symbols = []
    full_list = []
    # For loop finds all elements in list
    for item in list:
        #Finds all elements that contain an <a> tag eg. <a href="/symbol/MSFT">
        links = item.find_all('a')
    # Adds these links to a new list which contains two links in a list that I can't index for no reason
        full_list.append(links)
    # For every element in the 505 companies
    # Retrieve the symbol
    for i in range(len(list)):
        try:
            symbol = (full_list[i][1]).get_text()
            list_of_symbols.append(symbol)
        except IndexError:
            pass
        else:
            continue

    return list_of_symbols





    
