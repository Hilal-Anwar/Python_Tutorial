def bin_fruits(fruit_prices):
    '''
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    '''
    D = {'cheap': set(), 'affordable': set(), 'costly': set()}
    #fruit_prices = dict(sorted(fruit_prices.items(), key=lambda item: item[1], reverse=True))
    for fruit in fruit_prices:
        if fruit_prices[fruit] < 3:
            D['cheap'].add(fruit)
        elif 3 <= fruit_prices[fruit] <= 6:
            D['affordable'].add(fruit)
            #D['affordable'].sort()
        else:
            D['costly'].add(fruit)
    return D


print(bin_fruits({'Apple': 7, 'Banana': 3, 'Orange': 4,
                  'Grapes': 6, 'Papaya': 5, 'Mango': 2, 'Amla': 1, 'Jackfruit': 10}))
