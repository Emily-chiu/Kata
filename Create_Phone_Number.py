# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Test.describe("Basic tests")
# Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
# Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
# Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
# Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
# Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

# def create_phone_number(n):
#     phone_number = '('
#     for num in range(len(n)):
#         if num <= 2:
#             phone_number += str(n[num])

#             if num == 2:
#                 phone_number += ') '
        
#         elif num == len(n)-1:
#             phone_number += str(n[num])

#         else:
#             phone_number += str(n[num])
#             if num == 5:
#                 phone_number += '-' 
    
#     return phone_number

# print("Basic tests")
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
# print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

#---------------------------------------------------
def create_phone_number(n):
    phone_number = '('

    for num in n[0:3]:
        phone_number += str(num)
    
    phone_number += ') '

    for num in n[3:6]:
        phone_number += str(num)
    
    phone_number += '-'

    for num in n[6:]:
        phone_number += str(num)

    return phone_number
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

print("Basic tests")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

