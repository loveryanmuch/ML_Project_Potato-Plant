from typing import List

def conditional_sum(values: List[int], condition: str) -> int:
    """
    Calculate the sum of numbers in the list based on the given condition.
    
    Parameters:
    values (List[int]): A list of integers.
    condition (str): The condition to sum by, either "even" or "odd".
    
    Returns:
    int: The sum of numbers that meet the condition.
    """
    if condition not in {"even", "odd"}:
        raise ValueError("Condition must be either 'even' or 'odd'")
    
    parity = 0 if condition == "even" else 1
    return sum(x for x in values if x % 2 == parity)

print(conditional_sum([1, 2, 3, 4, 5], "even")) 
print(conditional_sum([1, 2, 3, 4, 5], "odd")) 
print(conditional_sum([13, 88, 12, 44, 99], "even"))
print(conditional_sum([], "odd"))
