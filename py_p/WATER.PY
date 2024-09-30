from typing import List

def printDivisors(n: int) -> List[int]:
    # Write your code here
    return [i for i in range(1, n + 1) if n % i == 0]
    
print(printDivisors(n=10))
