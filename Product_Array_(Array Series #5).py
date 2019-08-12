# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

# Test.describe("Basic Tests")
# Test.assert_equals(product_array([12,20]), [20,12])
# Test.assert_equals(product_array([3,27,4,2]), [216,24,162,324])
# Test.assert_equals(product_array([13,10,5,2,9]), [900,1170,2340,5850,1300])
# Test.assert_equals(product_array([16,17,4,3,5,2]), [2040,1920,8160,10880,6528,16320])
# print("<COMPLETEDIN::")

def product_array(numbers):
    product_list = []
    for i in range(len(numbers)):
        num = 1
        for j in numbers:
            num *= j
        
        product_list.append(num // numbers[i])
    
    return product_list

print("Basic Tests")
print(product_array([12,20]))
print(product_array([3,27,4,2]))
print(product_array([13,10,5,2,9]))
print(product_array([16,17,4,3,5,2]))
print("<COMPLETEDIN::")
