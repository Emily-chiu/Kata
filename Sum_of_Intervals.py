# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

# Test.assert_equals(sum_of_intervals([(1, 5)]), 4)
# Test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
# Test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
# Test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

def sum_of_intervals(intervals):
    range_list = []
    for i in intervals:
        for j in range(i[0],i[1]):
            range_list.append(j)
    return len(set(range_list))


print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (6, 10)]), 8)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)