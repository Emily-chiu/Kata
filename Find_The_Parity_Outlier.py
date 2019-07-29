# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
# test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
# test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

def find_outlier(integers):
    even_list = []
    odd_list = []
    
    for num in integers:
        if num % 2 == 0 :
            even_list.append(num)
        
        else:
            odd_list.append(num)
    
    if len(even_list) == 1:
        return even_list[0]
    
    else:
        return odd_list[0]

print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))