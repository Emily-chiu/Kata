# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# test.assert_equals(duplicate_count("abcde"), 0)
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)

def duplicate_count(text):
    sum = 0
    text = text.lower()
    for i in set(text):
        if text.count(i) != 1:
            sum += 1
    
    return sum
    

# print(duplicate_count("abcde"), 0)
# print(duplicate_count("abcdea"), 1)
print(duplicate_count("abcdeaB"))