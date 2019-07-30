# In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

# Test.it("Basic tests")
# Test.assert_equals(solve([3,4,4,3,6,3]),[4,6,3])
# Test.assert_equals(solve([1,2,1,2,1,2,3]),[1,2,3])
# Test.assert_equals(solve([1,2,3,4]),[1,2,3,4])
# Test.assert_equals(solve([1,1,4,5,1,2,1]),[4,5,2,1])

def solve(arr): 
    num = 0 
    
    while num < len(arr):
        if arr.count(arr[num]) != 1:
            arr.remove(arr[num])
        
        else:
            num += 1
    
    return arr

print("Basic tests")
print(solve([3,4,4,3,6,3]))
print(solve([1,2,1,2,1,2,3]))
print(solve([1,2,3,4]))
print(solve([1,1,4,5,1,2,1]))