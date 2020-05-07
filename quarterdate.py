import requests
from listofstocks import stockslist

def quarterdate():
    new_list = stockslist()
    quarter_date_list = []
    # Cycles through each company symbol to access api to retireve information
    for company in new_list:
        url = f'https://financialmodelingprep.com/api/v3/financial-statement-growth/{company}?period=quarter'
        r = requests.get(url)

        quarter_date = r.json()
        try:
            date = quarter_date['growth'][0]['date']
            quarter_date_list.append(date)
        except KeyError:
            pass
        else:
            continue
        
    return quarter_date_list 