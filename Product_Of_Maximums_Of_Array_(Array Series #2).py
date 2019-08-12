# Given an array/list [] of integers , Find the product of the k maximal numbers.

# Test.it("Basic Tests")
# test.assert_equals(max_product([0]*10, 5), 0)
# test.assert_equals(max_product([4,3,5], 2), 20)
# test.assert_equals(max_product([10,8,7,9], 3), 720)
# test.assert_equals(max_product([8,6,4,6], 3), 288)

# Test.it("Larger arrays")
# test.assert_equals(max_product (list(range(10, -1, -1)), 5), 10*9*8*7*6)
# test.assert_equals(max_product ([10,2,3,8,1,10,4], 5), 9600)
# test.assert_equals(max_product ([13,12,-27,-302,25,37,133,155,-1], 5), 247895375)

# Test.it("Arrays with negative values")
# test.assert_equals(max_product ([-4,-27,-15,-6,-1],2), 4)
# test.assert_equals(max_product ([-17,-8,-102,-309],2), 136)

# Test.it("Arrays with positive and negative values")
# test.assert_equals(max_product ([10,3,-27,-1], 3), -30)
# test.assert_equals(max_product ([14,29,-28,39,-16,-48],4), -253344)

def max_product(lst, n_largest_elements):
    lst.sort()
    lst.reverse()
    sum = 1 
    
    for num in range(0,n_largest_elements):
        sum = sum * lst[num]
    
    return sum

print("Basic Tests")
print(max_product([0]*10, 5))
print(max_product([4,3,5], 2))
print(max_product([10,8,7,9], 3))
print(max_product([8,6,4,6], 3))

print("Larger arrays")
print(max_product (list(range(10, -1, -1)), 5))
print(max_product ([10,2,3,8,1,10,4], 5))
print(max_product ([13,12,-27,-302,25,37,133,155,-1], 5))

print("Arrays with negative values")
print(max_product ([-4,-27,-15,-6,-1],2))
print(max_product ([-17,-8,-102,-309],2))

print("Arrays with positive and negative values")
print(max_product ([10,3,-27,-1], 3))
print(max_product ([14,29,-28,39,-16,-48],4))