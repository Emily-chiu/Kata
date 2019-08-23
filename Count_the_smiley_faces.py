# Description:
# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :] 


# Test.describe("Basic tests")
# Test.assert_equals(count_smileys([]), 0)
# Test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
# Test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
# Test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)

def count_smileys(arr):
    sum = 0
    for a in arr:
        if len(a) == 2:
            if a[0] == ':' or a[0] == ';':
                if a[1] == ')' or a[1] == 'D':
                    sum += 1

        elif len(a) == 3:
            if a[0] == ':' or a[0] == ';':
                if a[1] == '-' or a[1] == '~':
                    if a[2] == ')' or a[2] == 'D':
                        sum += 1
            
    return sum


print("Basic tests")
print(count_smileys([]), 0)
print(count_smileys([':D',':~)',';~D',':)']), 4)
print(count_smileys([':)',':(',':D',':O',':;']), 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)