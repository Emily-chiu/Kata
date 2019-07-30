# Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

# Test.assert_equals(min_value([1, 3, 1]), 13)
# Test.assert_equals(min_value([4, 7, 5, 7]), 457)
# Test.assert_equals(min_value([4, 8, 1, 4]), 148)

def min_value(digits):
    sort = sorted(list(set(digits)))
    a = ''
    for i in sort:
        a += str(i)
    return int(a)

print(min_value([1, 3, 1]))
print(min_value([4, 7, 5, 7]))
print(min_value([4, 8, 1, 4]))
