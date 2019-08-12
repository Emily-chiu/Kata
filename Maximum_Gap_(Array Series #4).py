# Given an array/list [] of integers , Find The maximum difference between the successive elements in its sorted form.

# Test.describe("Basic tests")
# Test.assert_equals(max_gap([13,10,2,9,5]),4)
# Test.assert_equals(max_gap([13,3,5]),8)
# Test.assert_equals(max_gap([24,299,131,14,26,25]),168)
# Test.assert_equals(max_gap([-3,-27,-4,-2]),23)
# Test.assert_equals(max_gap([-7,-42,-809,-14,-12]),767)
# Test.assert_equals(max_gap([12,-5,-7,0,290]),278)
# Test.assert_equals(max_gap([-54,37,0,64,-15,640,0]),576)
# Test.assert_equals(max_gap([130,30,50]),80)
# Test.assert_equals(max_gap([1,1,1]),0)
# Test.assert_equals(max_gap([-1,-1,-1]),0)
# print("<COMPLETEDIN::>")

def max_gap(numbers):
    max_number = 0
    # print(sorted(numbers))
    numbers.sort()
    for i in range(len(numbers)-1):
        # print('numbers[',i,']=',numbers[i])
        # print('numbers[',i+1,']=',numbers[i+1])
        # print(numbers[i] - numbers[i+1])
        # print(- (numbers[i] - numbers[i+1]))
        if (numbers[i] - numbers[i+1]) < 0:
            if (-(numbers[i] - numbers[i+1])) > max_number:
                max_number = (-(numbers[i] - numbers[i+1]))
        
        else:
            if (numbers[i] - numbers[i+1]) > max_number:
                max_number = (numbers[i] - numbers[i+1])
        # print
    
    return max_number

print("Basic tests")
print(max_gap([13,10,2,9,5]),4)
print(max_gap([13,3,5]),8)
print(max_gap([24,299,131,14,26,25]),168)
print(max_gap([-3,-27,-4,-2]),23)
print(max_gap([-7,-42,-809,-14,-12]),767)
print(max_gap([12,-5,-7,0,290]),278)
print(max_gap([-54,37,0,64,-15,640,0]),576)
print(max_gap([130,30,50]),80)
print(max_gap([1,1,1]),0)
print(max_gap([-1,-1,-1]),0)
print("<COMPLETEDIN::>")