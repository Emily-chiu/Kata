# The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

# test.assert_equals(century(1705), 18, 'Testing for year 1705')
# test.assert_equals(century(1900), 19, 'Testing for year 1900')
# test.assert_equals(century(1601), 17, 'Testing for year 1601')
# test.assert_equals(century(2000), 20, 'Testing for year 2000')
# test.assert_equals(century(356), 4, 'Testing for year 356')
# test.assert_equals(century(89), 1, 'Testing for year 89')

def century(year):
    if year % 100 != 0:
        return year // 100 +1
        
    else:
        return year // 100
    
print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
print(century(356))
print(century(89))