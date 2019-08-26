# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.

# 1.  The input string will always be lower case but maybe empty.
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat.

# result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# test.it("Should return: '["+", ".join(result)+"]'")
# test.assert_equals(wave("hello"), result)

# result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
# test.it("Should return: '["+", ".join(result)+"]'")
# test.assert_equals(wave("codewars"), result)

# result = []
# test.it("Should return: '["+", ".join(result)+"]'")
# test.assert_equals(wave(""), result)

# result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
# test.it("Should return: '["+", ".join(result)+"]'")
# test.assert_equals(wave("two words"),result)

# result = [" Gap ", " gAp ", " gaP "]
# test.it("Should return: '["+", ".join(result)+"]'")
# test.assert_equals(wave(" gap "), result)

def wave(str):
    str_list = []
    num = 0 
    while num != len(str):
        if str[num] == ' ':
            num += 1

        else:
            str_list.append(str[:num]+str[num].upper()+str[num+1:])
            num += 1
        
    return str_list

# result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# print(wave("hello"))

# result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
# print(wave("codewars"))

# result = []
# print(wave(""))

# result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
# print(wave("two words"))

# result = [" Gap ", " gAp ", " gaP "]
print(wave(" gap "))