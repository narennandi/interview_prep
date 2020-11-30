"""
brute force
Loop through every item in the list and find the difference
and update max profit. This would take too long if the array is huge
"""
# def maxProfit(prices) :
#     maxprofit = 0
#         for i in range(0, len(prices)):
#             for j in range(1, len(prices)):
#                 if j > i and prices[i] < prices[j]:
#                     profit = prices[j] - prices[i]
#                     if profit > maxprofit:
#                         maxprofit = profit
#         return maxprofit

"""
The points of interest are the peaks and valleys in the given graph. 
We need to find the largest peak following the smallest valley. 
We can maintain two variables - minprice and maxprofit corresponding to the smallest valley 
and maximum profit (maximum difference between selling price and minprice) 
obtained so far respectively.
"""
def maxProfit(prices) :
    minSoFar = float('inf')
    maxProfit = 0

    for i in range(len(prices)):
        minSoFar = min(prices[i], minSoFar)
        maxProfit = max(prices[i] - minSoFar, maxProfit)
    
    return maxProfit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))

