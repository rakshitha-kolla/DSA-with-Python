class ProductOfNumbers:

    def __init__(self):
        self.l=[]
        self.prefix=[]

    def add(self, num: int) -> None:
        self.l.append(num)
        if num==0:
            del self.prefix[::]
        elif len(self.prefix)>=1:
            self.prefix.append(self.prefix[-1]*num)
        else:
            self.prefix.append(num)
    def getProduct(self, k: int) -> int:
        if len(self.prefix)==k:
            return self.prefix[-1]
        elif len(self.prefix)>k:
            return self.prefix[-1]//self.prefix[-(k+1)]
        else:
            return 0
if __name__=="__main__":
    s=ProductOfNumbers()
    s.add(3)
    s.add(0)
    s.add(2)
    s.add(5)
    s.add(4)
    print(s.getProduct(2))
    print(s.getProduct(3))
    print(s.getProduct(4))
    s.add(8)
    print(s.getProduct(2))