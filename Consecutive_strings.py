# You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#=======================================================
# solution 1
def longest_consec(strarr, k):
    new_strarr = []
    
    if k > len(strarr):
        return ''
    
    elif k <= 0 :
        return ''
    
    else:
        strarr_count = []
        for strarr_num in range(len(strarr)-k+1):
            strarrstr = ''
            for strarr_str in strarr[strarr_num:strarr_num+k]:
                strarrstr += strarr_str
    
            strarr_count.append(len(strarrstr))

        for strarr_num in range(len(strarr)-k+1):
            strarrstr = ''
            for strarr_str in strarr[strarr_num:strarr_num+k]:
                strarrstr += strarr_str
    
            if len(strarrstr) == max(strarr_count):
                return strarrstr


#=======================================================
# solution 2

# def longest_consec(strarr, k):
#     result = ''

#     if k > 0 and k <= len(strarr):
#         strarr_count = []
#         result = ''
#         for strarr_num in range(len(strarr)-k+1):
#             strarrstr = ''
#             for strarr_str in strarr[strarr_num:strarr_num+k]:
#                 strarrstr += strarr_str
    
#             if len(strarrstr) > len(result):
#                 result = strarrstr

#     return result





print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)) # "abigailtheta"
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)) # "oocccffuucccjjjkkkjyyyeehh"
print(longest_consec([], 3)) # ""
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)) # "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)) # "wlwsasphmxxowiaxujylentrklctozmymu"
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)) # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)) # "ixoyx3452zzzzzzzzzzzz"
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)) # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)) # ""



#========================================================
# def longest_consec(strarr, k):
#     new_strarr = []
#     strarrstr = ''
#     if k > len(strarr):
#         return ''
    
#     elif k <= 0 :
#         return ''
    
#     else:
#         strarr_count = []
#         for strarr_str in strarr:
#             strarr_count.append(len(strarr_str))
        
#         write_list = []
#         new_strarr_count = sorted(strarr_count,reverse = True)
#         for num in range(k):
#             for num_1 in range(len(strarr_count)):
#                 if strarr_count[num_1] == new_strarr_count[num]:
#                     write_list.append(strarr_count[num_1])
#                     break
        
#         for num in range(len(strarr_count)):
#             if len(strarr[num]) in write_list:
#                 new_strarr.append(strarr[num])
        
#         for i in range(k):
#             strarrstr += new_strarr[i]
    
#     return strarrstr