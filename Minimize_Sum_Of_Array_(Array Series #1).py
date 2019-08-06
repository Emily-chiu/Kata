# Given an array of intgers , Find the minimum sum which is obtained from summing each Two integers product .

# Test.describe("Basic Tests")
# Test.it("should return the minimum sum")
# Test.assert_equals(min_sum([5,4,2,3]), 22)
# Test.assert_equals(min_sum([12,6,10,26,3,24]), 342)
# Test.assert_equals(min_sum([9,2,8,7,5,4,0,6]), 74)

def min_sum(arr):
    sum = 0
    arr.sort()
    while len(arr) != 0:
        sum += arr.pop(0)*arr.pop()

    return sum

print("Basic Tests")
print("should return the minimum sum")
print(min_sum([5,4,2,3]))
print(min_sum([12,6,10,26,3,24]))
print(min_sum([9,2,8,7,5,4,0,6]))