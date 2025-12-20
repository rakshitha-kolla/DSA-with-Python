def buysell(stock):
    buy1=float('inf')
    buy2=float('inf')
    profit1=0
    profit2=0
    for price in stock:
        buy1=min(buy1,price)
        profit1=max(profit1,price-buy1)

        buy2=min(buy2,price-profit1)
        profit2=max(profit2,price-buy2)
    return profit2
if __name__ == "__main__":
    stock=[3,3,5,0,0,3,1,4]
    print(buysell(stock))