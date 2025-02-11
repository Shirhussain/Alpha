# when I saw this code then immediately I thought of coin change problem

from typing import List
from collections import deque

def fill_tank(tank_size: int, bucket_sizes: List[int]) -> List[int]:
    
    def fill_tank_recursive(amount: int, memo={}) -> tuple[int, List[int]]:
        if amount == 0:
            return 0, []
        if amount < 0:
            return float('inf'), []
        if amount in memo:
            return memo[amount]
            
        min_scoops = float('inf')
        best_path = []
        
        for bucket in bucket_sizes:
            scoops, path = fill_tank_recursive(amount - bucket, memo)
            if scoops != float('inf') and scoops + 1 < min_scoops:
                min_scoops = scoops + 1
                best_path = [bucket] + path
                
        memo[amount] = (min_scoops, best_path)
        return memo[amount]
    
    scoops, path = fill_tank_recursive(tank_size)
    return path if scoops != float('inf') else None

def fill_tank_dfs(tank_size: int, bucket_sizes: List[int]) -> List[int]:
    """DFS approach using queue, similar to my coin_change."""
    if tank_size == 0:
        return []
        
    queue = deque([(0, [])])  # (current_amount, path)
    seen = {0}
    
    while queue:
        amount, path = queue.popleft()
        
        for bucket in bucket_sizes:
            new_amount = amount + bucket
            if new_amount == tank_size:
                return path + [bucket]
            if new_amount < tank_size and new_amount not in seen:
                seen.add(new_amount)
                queue.append((new_amount, path + [bucket]))
    
    return None

def fill_tank_tabulation(tank_size: int, bucket_sizes: List[int]) -> List[int]:
    """Bottom up approach like my coin change."""
    dp = [float('inf')] * (tank_size + 1)
    prev = [-1] * (tank_size + 1)
    dp[0] = 0
    
    for amount in range(tank_size + 1):
        for bucket in bucket_sizes:
            if amount >= bucket and dp[amount - bucket] != float('inf'):
                if dp[amount - bucket] + 1 < dp[amount]:
                    dp[amount] = dp[amount - bucket] + 1
                    prev[amount] = bucket
    
    if dp[tank_size] == float('inf'):
        return None
        
    path = []
    remaining = tank_size
    while remaining > 0:
        path.append(prev[remaining])
        remaining -= prev[remaining]
    return path


test_cases = [
    (20, [6, 4, 3, 2]),
    (6, [5, 4, 2]),
    (3, [2])
]

for size, buckets in test_cases:
    print(f"\nTank size: {size}, Buckets: {buckets}")
    print(f"Recursive: {fill_tank(size, buckets)}")
    print(f"DFS: {fill_tank_dfs(size, buckets)}")
    print(f"Tabulation: {fill_tank_tabulation(size, buckets)}")
