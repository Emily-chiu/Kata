# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
# test.assert_equals(reverse_words('apple'), 'elppa')
# test.assert_equals(reverse_words('a b c d'), 'a b c d')
# test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')

def reverse_words(text):
    text_split = text.split(" ")
    j = ''

    for i in text_split:
        j += i[::-1] + " "

    return j.strip(' ')

print(reverse_words('double  spaced  words'))
print(reverse_words('a b c d'))
print(reverse_words('apple'))


# x = "eeeffff"
# print(x[::-1])

