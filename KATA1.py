def sumLargestNumbers(numbers):
    largest = max(numbers)
    numbers.remove(largest)
    second_largest = max(numbers)
    return largest + second_largest

print(sumLargestNumbers([1, 10])) 
print(sumLargestNumbers([1, 2, 3]))
print(sumLargestNumbers([10, 4, 34, 6, 92, 2]))