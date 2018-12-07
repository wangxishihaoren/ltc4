

def maxProfit(prices):

    def findMax(arr, k):
        temp = arr[k - 1]
        for i in range(k, len(arr)):
            if temp < arr[i]:
                temp = arr[i]
        return temp

    profitMax = 0
    for i in range(0,len(prices)):
        temp = prices[i]
        maxNum = findMax(prices,i+1)
        if temp < maxNum:
            profit = maxNum - temp
            if profit > profitMax:
                profitMax = profit
    return profitMax

print(maxProfit([7,6,4,3,1]))

