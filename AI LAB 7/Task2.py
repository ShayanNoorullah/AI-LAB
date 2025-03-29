import sys

def alphaBetaPruning(coins, left, right, alpha, beta, isMaxTurn):
    if left > right:
        return 0
    if isMaxTurn:
        best = -sys.maxsize
        best = max(best, coins[left] + alphaBetaPruning(coins, left + 1, right, alpha, beta, False))
        alpha = max(alpha, best)
        if beta <= alpha:
            return best
        best = max(best, coins[right] + alphaBetaPruning(coins, left, right - 1, alpha, beta, False))
        return best
    else:
        best = sys.maxsize
        best = min(best, alphaBetaPruning(coins, left + 1, right, alpha, beta, True))
        beta = min(beta, best)
        if beta <= alpha:
            return best
        best = min(best, alphaBetaPruning(coins, left, right - 1, alpha, beta, True))
        return best
def maxPick(coins, left, right):
    pickLeft = coins[left] + alphaBetaPruning(coins, left + 1, right, -sys.maxsize, sys.maxsize, False)
    pickRight = coins[right] + alphaBetaPruning(coins, left, right - 1, -sys.maxsize, sys.maxsize, False)
    return left if pickLeft >= pickRight else right









def playGame(coins):
    left, right = 0, len(coins) - 1
    maxScore, minScore = 0, 0
    print(f"Initial Coins: {coins}")
    while left <= right:
        maxIndex = maxPick(coins, left, right)
        maxScore += coins[maxIndex]
        print(f"Max picks {coins[maxIndex]}, Remaining Coins: {coins[left:right+1]}")
        if maxIndex == left:
            left += 1
        else:
            right -= 1
        if left > right:
            break
        if coins[left] < coins[right]:
            minIndex = left
        else:
            minIndex = right
        minScore += coins[minIndex]
        print(f"Min picks {coins[minIndex]}, Remaining Coins: {coins[left:right+1]}")
        if minIndex == left:
            left += 1
        else:
            right -= 1
    print(f"\nFinal Scores - Max: {maxScore}, Min: {minScore}")
    print("Winner:", "Max" if maxScore > minScore else "Min")




coins = [3, 9, 1, 2, 7, 5]
playGame(coins)
