# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# Test.it("Basic tests")
# Test.assert_equals(persistence(39), 3)
# Test.assert_equals(persistence(4), 0)
# Test.assert_equals(persistence(25), 2)
# Test.assert_equals(persistence(999), 4)

def persistence(n):
    time = 0
    
    while len(str(n)) != 1:
        sum = 1 
        for ns in str(n):
            sum *= int(ns)
        time += 1
        n = sum    
    
    return time

print("Basic tests")
print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
print(persistence(999), 4)
