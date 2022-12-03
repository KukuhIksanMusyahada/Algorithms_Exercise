'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
'''

class BuySellStock:

    def sol1(self,prices: list[int]):
        profits = []
        for i,price in enumerate(prices):
            for j in range(i+1,len(prices)):
                profits.append(prices[j]-price)
        max_profit = max(profits)
        if max_profit<= 0:
            return 0
        return max_profit

    def sol2(self,prices: list[int]):
        pass


if __name__=='__main__':
    prices = [7,1,5,3,6,4]
    solution = BuySellStock()
    max_profit = solution.sol1(prices)
    print(max_profit)
    # solution.sol2(prices)