    # ----------------------------------------------------
    # Intuition:
    #
    # 1. Greedy Linear Pass:
    #    - We're allowed to buy and sell multiple times (even on the same day).
    #    - So we just grab profit wherever there's a price increase.
    #    - If prices[i] > prices[i-1], buy at i-1 and sell at i.
    #    - We add up all such gains — this yields the global maximum.
    #    - Time: O(n), Space: O(1)
    #
    # 2. Greedy (Valley-Peak):
    #    - We simulate buy at valleys and sell at peaks.
    #    - This achieves the same result as the greedy pass but mimics real trading logic.
    #    - Time: O(n), Space: O(1)
    #
    # 3. Brute Force (DFS):
    #    - Try all valid (buy, sell) pairs recursively.
    #    - After each sell, recurse to find further profitable moves.
    #    - Time: O(2^n), Space: O(n) stack — not scalable but good for learning.
    # ----------------------------------------------------

    # ----------------------------------------------------
    # 1. Optimal Greedy Approach (Accumulate positive diffs)
    # Time: O(n), Space: O(1)
    # ----------------------------------------------------


from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # ----------------------------------------------------
    # 2. Valley-Peak Greedy Simulation
    # Time: O(n), Space: O(1)
    # ----------------------------------------------------
    # def maxProfit(self, prices: List[int]) -> int:
    #     i = 0
    #     profit = 0
    #     while i < len(prices) - 1:
    #         while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
    #             i += 1
    #         valley = prices[i]
    #         while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
    #             i += 1
    #         peak = prices[i]
    #         profit += peak - valley
    #     return profit

    # ----------------------------------------------------
    # 3. Brute Force Recursive (DFS)
    # Time: O(2^n), Space: O(n) stack
    # ----------------------------------------------------
    # def maxProfit(self, prices: List[int]) -> int:
    #     def dfs(start: int) -> int:
    #         if start >= len(prices):
    #             return 0
    #         max_profit = 0
    #         for buy in range(start, len(prices)):
    #             for sell in range(buy + 1, len(prices)):
    #                 if prices[sell] > prices[buy]:
    #                     profit = prices[sell] - prices[buy] + dfs(sell + 1)
    #                     max_profit = max(max_profit, profit)
    #         return max_profit
    #     return dfs(0)


if __name__ == "__main__":
    sol = Solution()

    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))     # Output: 7
    print(sol.maxProfit([1, 2, 3, 4, 5]))        # Output: 4
    print(sol.maxProfit([7, 6, 4, 3, 1]))        # Output: 0
    print(sol.maxProfit([2, 4, 1, 7]))           # Output: 8 
    print(sol.maxProfit([1]))                   # Output: 0 
    print(sol.maxProfit([]))                    # Output: 0
