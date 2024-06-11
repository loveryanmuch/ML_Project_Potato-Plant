def numberOfVowels(data):
    vowels = "aeiou"
    count = 0
    for char in data:
        if char in vowels:
            count += 1
    return count
print(numberOfVowels("orange"))    
print(numberOfVowels("lighthouse labs"))
print(numberOfVowels("aeiou"))       