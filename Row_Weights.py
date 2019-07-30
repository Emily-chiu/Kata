# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

# Test.describe("Basic tests")
# Test.assert_equals(row_weights([80]), (80,0))
# Test.assert_equals(row_weights([100,50]), (100,50))
# Test.assert_equals(row_weights([50,60,70,80]), (120,140))
# Test.assert_equals(row_weights([13,27,49]), (62,27))
# Test.assert_equals(row_weights([70,58,75,34,91]), (236,92))
# Test.assert_equals(row_weights([29,83,67,53,19,28,96]), (211,164))
# Test.assert_equals(row_weights([0]), (0,0))
# Test.assert_equals(row_weights([100,51,50,100]), (150,151))
# Test.assert_equals(row_weights([39,84,74,18,59,72,35,61]), (207,235))
# Test.assert_equals(row_weights([0,1,0]), (0,1))

def row_weights(array):
    sum = [0,0]
    for num in range(len(array)):
        if num % 2 == 0:
            sum[0] += array[num]
        
        else:
            sum[1] += array[num]
        
    return sum[0],sum[1]

print("Basic tests")
print(row_weights([80]))
print(row_weights([100,50]))
print(row_weights([50,60,70,80]))
print(row_weights([13,27,49]))
print(row_weights([70,58,75,34,91]))
print(row_weights([29,83,67,53,19,28,96]))
print(row_weights([0]))
print(row_weights([100,51,50,100]))
print(row_weights([39,84,74,18,59,72,35,61]))
print(row_weights([0,1,0]))
