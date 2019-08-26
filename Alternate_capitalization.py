# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

# Good luck!

# If you like this Kata, please try:

# Test.it("Basic tests")
# Test.assert_equals(capitalize("abcdef"),['AbCdEf', 'aBcDeF'])
# Test.assert_equals(capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])
# Test.assert_equals(capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
# Test.assert_equals(capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])

def capitalize(s):
    s.lower()
    s_list = ['','']
    for s_num in range(2):
        new_s = ''
        if s_num == 0:
            for ss in range(len(s)):
                if ss == 0:
                    new_s += s[ss].upper()

                elif ss % 2 == 0:
                    new_s += s[ss].upper()
                
                else:
                    new_s += s[ss]

        if s_num == 1:
            for ss in range(len(s)):
                if ss == 0:
                    new_s += s[ss]

                elif ss % 2 == 1:
                    new_s += s[ss].upper()
                
                else:
                    new_s += s[ss]
        
        s_list[s_num] = new_s
    
    return s_list

print("Basic tests")
print(capitalize("abcdef"),['AbCdEf', 'aBcDeF'])
print(capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])
print(capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
print(capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])