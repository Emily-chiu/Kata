# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

# test.describe("is_square")
# test.it("should work for some examples")
# test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
# test.assert_equals(is_square( 0), True, "0 is a square number")
# test.assert_equals(is_square( 3), False, "3 is not a square number")
# test.assert_equals(is_square( 4), True, "4 is a square number")
# test.assert_equals(is_square(25), True, "25 is a square number")
# test.assert_equals(is_square(26), False, "26 is not a square number")

#----------------------------------------------------

# def is_square(n):
#     num = 0
#     sum = 0
#     if n < 0:
#         return False
    
#     else:
#         while sum <= n:
#             sum = num **2
            
#             if sum == n:
#                 return True

#             else:
#                 num += 1

#     return False

#----------------------------------------------------

def is_square(n):
    if n >= 0:
        num = n ** 0.5
        if num % 1 == 0:
            return True

    return False

#----------------------------------------------------
print("is_square")
print("should work for some examples")
print(is_square(-1), False)
print(is_square( 0), True)
print(is_square( 3), False)
print(is_square( 4), True)
print(is_square(25), True)
print(is_square(26), False)