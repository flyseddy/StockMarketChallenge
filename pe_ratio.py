from price import price
from eps import eps

def pe_ratio():
    list_of_stock_prices = price()
    list_of_eps = eps()
    list_of_ratios = []
    
    # Iterates through the length of this list(505 items)
    # Calculates the estimated P/E ratio of each stock based on the quarterly eps
    for i in range(len(list_of_stock_prices)):
        try:
            ratio = float(list_of_stock_prices[i]) // float(list_of_eps[i])
        except (ZeroDivisionError, IndexError):
            pass
        else:
            list_of_ratios.append(ratio)
    
    return list_of_ratios        
