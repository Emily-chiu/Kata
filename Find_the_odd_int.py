# Given an array, find the int that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# test.describe("Example")
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 == 1:
            return num

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


#---------------------------------------------

# def find_it(seq):
#     odd_time = []
#     for num in seq:
#         time = 0
#         for check in seq:
#             if num in odd_time:
#                 break
            
#             else:
#                 if check == num:
#                     time += 1

#         if time % 2 == 1:
#             odd_time.append(num)
        
#     return odd_time[0]


