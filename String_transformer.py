# Given a string, return a new string that has transformed based on the input:

# Change case of every character, ie. lower case to upper case, upper case to lower case.
# Reverse the order of words from the input.
# Note: You will have to handle multiple spaces, and leading/trailing spaces.

# test.assert_equals(string_transformer("Example string"), "STRING eXAMPLE")
# test.assert_equals(string_transformer("Example Input"), "iNPUT eXAMPLE")
# test.assert_equals(string_transformer("To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO")
# # Should handle empty string
# test.assert_equals(string_transformer(""), "")
# # Should handle multiple spaces
# test.assert_equals(string_transformer("You Know When  THAT  Hotline Bling"), "bLING hOTLINE  that  wHEN kNOW yOU")
# # Should handle leading space
# test.assert_equals(string_transformer(" A b C d E f G "), " g F e D c B a ")

def string_transformer(s):
    s = s.split(' ')
    s.reverse()

    
    for s_num in range(len(s)):
        if ' ' not in s[s_num]:
            new_s_str = ''
            for s_str in s[s_num]:
                if s_str.islower() == True:
                    new_s_str += s_str.upper()
                
                else:
                    new_s_str += s_str.lower()
            s[s_num] = new_s_str

    new_s = ''
    for ns in s:
        new_s += ns + ' '

    return new_s[:len(new_s)-1]

print(string_transformer("Example string")) # "STRING eXAMPLE"
print(string_transformer("Example Input")) # "iNPUT eXAMPLE"
print(string_transformer("To be OR not to be That is the Question")) # "qUESTION THE IS tHAT BE TO NOT or BE tO"
print(string_transformer("")) #""
print(string_transformer("You Know When  THAT  Hotline Bling")) # "bLING hOTLINE  that  wHEN kNOW yOU"
print(string_transformer(" A b C d E f G ")) # " g F e D c B a "