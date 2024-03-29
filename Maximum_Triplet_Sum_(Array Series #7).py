# Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .

# Test.describe("Basic tests")
# Test.assert_equals(max_tri_sum([3,2,6,8,2,3]),17)
# Test.assert_equals(max_tri_sum([2,9,13,10,5,2,9,5]),32)
# Test.assert_equals(max_tri_sum([2,1,8,0,6,4,8,6,2,4]),18)
# Test.assert_equals(max_tri_sum([-3,-27,-4,-2,-27,-2]),-9)
# Test.assert_equals(max_tri_sum([-14,-12,-7,-42,-809,-14,-12]),-33)
# Test.assert_equals(max_tri_sum([-13,-50,57,13,67,-13,57,108,67]),232)
# Test.assert_equals(max_tri_sum([-7,12,-7,29,-5,0,-7,0,0,29]),41)
# Test.assert_equals(max_tri_sum([-2,0,2]),0)
# Test.assert_equals(max_tri_sum([-2,-4,0,-9,2]),0)
# Test.assert_equals(max_tri_sum([-5,-1,-9,0,2]),1)
# print("<COMPLETEDIN::>")

def max_tri_sum(numbers):
    numbers = sorted(set(numbers), reverse = True)
    sum = 0

    for i in range(3):
        sum += numbers[i]
    return sum
    

print("Basic tests")
print(max_tri_sum([3,2,6,8,2,3]),17)
print(max_tri_sum([2,9,13,10,5,2,9,5]),32)
print(max_tri_sum([2,1,8,0,6,4,8,6,2,4]),18)
print(max_tri_sum([-3,-27,-4,-2,-27,-2]),-9)
print(max_tri_sum([-14,-12,-7,-42,-809,-14,-12]),-33)
print(max_tri_sum([-13,-50,57,13,67,-13,57,108,67]),232)
print(max_tri_sum([-7,12,-7,29,-5,0,-7,0,0,29]),41)
print(max_tri_sum([-2,0,2]),0)
print(max_tri_sum([-2,-4,0,-9,2]),0)
print(max_tri_sum([-5,-1,-9,0,2]),1)
print("<COMPLETEDIN::>")