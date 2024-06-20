def sumLargestNumbers(numbers):
    largest = max(numbers)
    numbers.remove(largest)
    second_largest = max(numbers)
    return largest + second_largest

