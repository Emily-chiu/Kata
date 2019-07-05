# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

# test.assert_equals( string_to_number("1234"), 1234)
# test.assert_equals( string_to_number("605"), 605)
# test.assert_equals( string_to_number("1405"), 1405)
# test.assert_equals( string_to_number("1234"), 1234)

def string_to_number(s):
    # ... your code here
    s = int(s)
    return s

print(string_to_number("1234"))