
# 0x08-making_change

## Overview

This document provides an explanation of two different approaches for solving the coin change problem: **Greedy Algorithm** and **Dynamic Programming**. Both approaches aim to determine the fewest number of coins needed to make up a given total from a set of coins with different denominations. However, each approach has its own methodology and optimality characteristics.

## Greedy Algorithm

### Approach
- The **Greedy Algorithm** solves the coin change problem by making a series of choices, each of which appears to be locally optimal. It focuses on choosing the highest denomination coin available at each step in an attempt to reach the target total quickly.
- The algorithm continues to choose the largest possible coin that does not exceed the remaining amount until it reaches the total or cannot use any more coins.

### Pros
- **Efficiency**: The greedy algorithm is fast and easy to implement.
- **Simplicity**: The approach is straightforward, making it easy to understand and apply.

### Cons
- **Suboptimal Solutions**: The greedy algorithm does not always guarantee the optimal solution. For certain coin systems, it may lead to suboptimal results because it does not consider all possible combinations.
- **Example**: Given a total of 6 and coin denominations [1, 3, 4], the greedy approach might use coins 4 and then 1, resulting in a total of 3 coins. However, the optimal solution (2 coins of 3) is not found.

## Dynamic Programming

### Approach
- **Dynamic Programming (DP)** builds solutions incrementally by solving subproblems and combining their solutions to address larger problems. It uses a table to store the minimum number of coins required for each intermediate amount, eventually building up to the total amount.
- The algorithm evaluates all possible combinations of coins to find the minimum number of coins needed for each amount from 0 to the target total.

### Steps
1. **Initialization**: Start with a table where each entry represents the minimum number of coins needed for each amount, initialized to infinity (or a large number) except for the base case (0 coins for a total of 0).
2. **Table Update**: For each coin and for each amount, update the table to reflect the fewest number of coins needed by either including or excluding the current coin.
3. **Solution Retrieval**: The final entry in the table represents the minimum number of coins needed for the target total. If it remains infinity, the total cannot be made with the given coins.

### Pros
- **Optimal Solution**: Guarantees an optimal solution by evaluating all combinations, ensuring the fewest number of coins are used.
- **Versatility**: Effective for a wide range of coin systems and problems where the greedy approach might fail.

### Cons
- **Complexity**: May require more memory and processing time compared to greedy algorithms due to the comprehensive exploration of possibilities.

## Comparison

- **Greedy Algorithm**: Prioritizes immediate benefits by choosing the highest denomination coins, which can lead to non-optimal solutions for certain coin systems.
- **Dynamic Programming**: Provides a thorough exploration of possibilities, ensuring the optimal solution by minimizing the number of coins required, even when the greedy approach would fail.

## Conclusion

Both algorithms have their strengths and weaknesses. The **Greedy Algorithm** is simple and efficient but might not always find the optimal solution. **Dynamic Programming** guarantees an optimal solution by considering all possible combinations, though it may be more resource-intensive. Understanding these approaches helps in selecting the right method based on the problem requirements.
