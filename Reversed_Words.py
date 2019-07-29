# Complete the solution so that it reverses all of the words within the string passed in.

# Example:

# test.assert_equals(reverseWords("hello world!"), "world! hello")

def reverseWords(str):
    str_list = str.split(' ')
    str = ''
    for str_num in range(len(str_list)):
        str += str_list.pop() +' '
    
    return str[:-1]

print(reverseWords("hello world!"))
