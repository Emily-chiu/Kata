# Given an array of N integers, you have to find how many times you have to add up the smallest numbers in the array until their Sum becomes greater or equal to K.

# Test.describe("Basic tests")
# Test.assert_equals(minimum_steps([4,6,3], 7), 1)
# Test.assert_equals(minimum_steps([10,9,9,8], 17), 1)
# Test.assert_equals(minimum_steps([8,9,10,4,2], 23), 3)
# Test.assert_equals(minimum_steps([19,98,69,28,75,45,17,98,67], 464), 8)
# Test.assert_equals(minimum_steps([4,6,3], 2), 0)
# print("<COMPLETEDIN::>")

def minimum_steps(numbers, value):
    numbers.sort()
    time = 0
    calculation = numbers[time]
    if numbers[0] >= value:
        return time

    else:
        while calculation < value:
            calculation += numbers[time+1]
            time += 1

    return time

print("Basic tests")
print(minimum_steps([4,6,3], 7), 1)
print(minimum_steps([10,9,9,8], 17), 1)
print(minimum_steps([8,9,10,4,2], 23), 3)
print(minimum_steps([19,98,69,28,75,45,17,98,67], 464), 8)
print(minimum_steps([4,6,3], 2), 0)
print("<COMPLETEDIN::>")