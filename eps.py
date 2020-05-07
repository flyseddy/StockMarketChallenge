import requests
from listofstocks import stockslist


def eps():
    # Create an instance of the list of the list of company symbols to reference
    list_of_symbols = stockslist()
    list_of_eps = []
    for company in list_of_symbols:
        url = f'https://financialmodelingprep.com/api/v3/financials/income-statement/{company}?period=quarter'
        r = requests.get(url)
        # Process the request as json
        try:
            stock_dict = r.json() 
            eps = stock_dict['financials'][0]['EPS']
        except KeyError:
            pass
        else:
            list_of_eps.append(eps)
    
    return  list_of_eps
    
    
