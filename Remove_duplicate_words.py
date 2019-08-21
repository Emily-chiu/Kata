# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

# Test.it("Basic tests")
# Test.assert_equals(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
# Test.assert_equals(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")


def remove_duplicate_words(s):
    s = s.split(' ')
    for ns in range(len(s)-1, 0, -1):
        if s.count(s[ns]) != 1:
            del s[ns]

    s_str = ''
    for ss in s:
        s_str += ss + ' '
    return s_str.strip(' ')


print("Basic tests")
print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
print(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")
