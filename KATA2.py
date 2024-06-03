def conditionalSum(values, condition):
    if condition == "even":
        return sum(x for x in values if x % 2 == 0)
    else:
        return sum(x for x in values if x % 2 != 0)

print(conditionalSum([1, 2, 3, 4, 5], "even")) 
print(conditionalSum([1, 2, 3, 4, 5], "odd")) 
print(conditionalSum([13, 88, 12, 44, 99], "even"))
print(conditionalSum([], "odd")) 