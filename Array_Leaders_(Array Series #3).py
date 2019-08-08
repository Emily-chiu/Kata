# Given an array/list [] of integers , Find all the LEADERS in the array.

# Test.describe("Sample Tests")
# Test.it("Positive Values")
# test.assert_equals(array_leaders([1,2,3,4,0]), [4])
# test.assert_equals(array_leaders([16,17,4,3,5,2]), [17,5,2])

# Test.it("Negative Values")
# test.assert_equals(array_leaders([-1,-29,-26,-2]), [-1])
# test.assert_equals(array_leaders([-36,-12,-27]), [-36,-12])

# Test.it("Mixed Values")
# test.assert_equals(array_leaders([5,2]), [5,2])
# test.assert_equals(array_leaders([0,-1,-29,3,2]), [0,-1,3,2])

def array_leaders(numbers):
    numbers.append(0)
    numbers_list = []

    for ns in range(len(numbers)-1):
        if numbers[ns] > sum(numbers[ns+1:]):
            numbers_list.append(numbers[ns])  

    return numbers_list

print("Sample Tests")
print("Positive Values")
print(array_leaders([1,2,3,4,0]), [4])
print(array_leaders([16,17,4,3,5,2]), [17,5,2])

print("Negative Values")
print(array_leaders([-1,-29,-26,-2]), [-1])
print(array_leaders([-36,-12,-27]), [-36,-12])

print("Mixed Values")
print(array_leaders([5,2]), [5,2])
print(array_leaders([0,-1,-29,3,2]), [0,-1,3,2])

