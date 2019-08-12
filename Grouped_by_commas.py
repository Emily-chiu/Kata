# Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.
# Assume: 0 <= n < 2147483647

# test.assert_equals(group_by_commas(1), '1')
# test.assert_equals(group_by_commas(10), '10')
# test.assert_equals(group_by_commas(100), '100')
# test.assert_equals(group_by_commas(1000), '1,000')
# test.assert_equals(group_by_commas(10000), '10,000')
# test.assert_equals(group_by_commas(100000), '100,000')
# test.assert_equals(group_by_commas(1000000), '1,000,000')
# test.assert_equals(group_by_commas(35235235), '35,235,235')

def group_by_commas(n):
    n = str(n)[::-1]
    ns = ''
    if len(n) > 3:
        for i in n:
            ns += i
            if ',' not in ns:
                if (len(ns) % 3) == 0 :
                    ns += ','
            else:
                if (len(ns) % 3) == ns.count(',')%3 :
                    ns += ','
    else:
        ns = n
    
    return ns.strip(',')[::-1]

print(group_by_commas(1), '1')
print(group_by_commas(10), '10')
print(group_by_commas(100), '100')
print(group_by_commas(1000), '1,000')
print(group_by_commas(10000), '10,000')
print(group_by_commas(100000), '100,000')
print(group_by_commas(1000000), '1,000,000')
print(group_by_commas(35235235), '35,235,235')
