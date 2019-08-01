# ..Or rather, what's a name in? For us, a particular string is where we are looking for a name.

# Test.describe("Basic tests")
# Test.assert_equals(name_in_str("Across the rivers", "chris"), True)
# Test.assert_equals(name_in_str("Next to a lake", "chris"), False)
# Test.assert_equals(name_in_str("Under a sea", "chris"), False)
# Test.assert_equals(name_in_str("A crew that boards the ship", "chris"), False)
# Test.assert_equals(name_in_str("A live son", "Allison"), False)
# Test.assert_equals(name_in_str("Just enough nice friends","Jennifer"),False)
# Test.assert_equals(name_in_str("thomas","Thomas"),True)
# Test.assert_equals(name_in_str("pippippi","Pippi"),True)
# Test.assert_equals(name_in_str("pipipp","Pippi"),False)
# Test.assert_equals(name_in_str("ppipip","Pippi"),False)

def name_in_str(str, name):
    str = str.lower()
    name = name.lower()
    
    str_list = []
    name_list = []

    for str_num in str:
        str_list.append(str_num)
    
    for str_name in name:
        if len(str_list) != 0:
            for str_time in range(len(str_list)):
                a = str_list.pop(0)
                if a == str_name:
                    break

                elif len(str_list) == 0:
                    return False
        else:
            return False
    return True
    
print("Basic tests")
print(name_in_str("Across the rivers", "chris"))
print(name_in_str("Next to a lake", "chris"))
print(name_in_str("Under a sea", "chris"))
print(name_in_str("A crew that boards the ship", "chris"))
print(name_in_str("A live son", "Allison"))
print(name_in_str("Just enough nice friends","Jennifer"))
print(name_in_str("thomas","Thomas"))
print(name_in_str("pippippi","Pippi"))
print(name_in_str("pipipp","Pippi"))
print(name_in_str("ppipip","Pippi"))