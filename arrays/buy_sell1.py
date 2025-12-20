
def buysell(stock):
    min_price=float('inf')
    max_profit=0
    for i in range(len(stock)):
        if stock[i]<min_price:
            min_price=stock[i]
        max_profit=max(max_profit,stock[i]-min_price)
    return max_profit
stock=[7,1,5,3,6,4]
print(buysell(stock))