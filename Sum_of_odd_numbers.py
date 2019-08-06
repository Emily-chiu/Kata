# Given the triangle of consecutive odd numbers

# Test.assert_equals(row_sum_odd_numbers(1), 1)
# Test.assert_equals(row_sum_odd_numbers(2), 8)
# Test.assert_equals(row_sum_odd_numbers(13), 2197)
# Test.assert_equals(row_sum_odd_numbers(19), 6859)
# Test.assert_equals(row_sum_odd_numbers(41), 68921)

def row_sum_odd_numbers(n):
    num = 1
    for ns in range(1, n+1):
        odd_list = []
        for i in range(0,ns):
            odd_list.append(num)
            num += 2
        
    return sum(odd_list)

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))