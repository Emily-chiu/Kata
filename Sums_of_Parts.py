# @test.describe('Tests')
# def fixed_tests():
#     def dotest(ls, expected):
#         actual = parts_sums(ls)
#         Test.assert_equals(actual, expected)
        
#     @test.it('Basic')
#     def basic_tests():
#         dotest([], [0])
#         dotest([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0])
#         dotest([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0])
        
#         dotest([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358], 
#             [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0])

def parts_sums(ls):
    ls.append(0)
    for num in range(len(ls)-1,-1,-1):
        if num == len(ls)-1:
            ls[num] = ls[num]

        else:
            ls[num] += ls[num+1]

    return ls

print(parts_sums([0, 1, 3, 6, 10]))
print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))
print(parts_sums([]))

# x = []
# print(len(x))

