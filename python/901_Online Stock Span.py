class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        ans = 1

        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]

        self.stack.append([price, ans])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""Test area"""
if __name__ == "__main__":
    x = StockSpanner()
    print(x.next(100))
    print(x.next(80))
    print(x.next(60))
    print(x.next(70))
    print(x.next(60))
    print(x.next(75))
    print(x.next(85))
