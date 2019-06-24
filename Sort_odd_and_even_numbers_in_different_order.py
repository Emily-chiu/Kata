# You have an array of numbers.

# Your task is to sort odd numbers within the array in ascending order, and even numbers in descending order.

# Note that zero is an even number. If you have an empty array, you need to return it.

# Example
# sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 8, 4, 5, 2]

#**************************************************
#先將奇數偶數分開再一個一個放進去

# def sort_array(a):
#     result = []     #放結果的陣列
#     even = []       #放偶數的陣列
#     odd = []        #放奇數的陣列
#     for i in a:     #判斷把原本輸入的數字是偶數還是奇數，分別放入even和odd陣列
#         if i % 2 == 0:
#             even.append(i)

#         else:
#             odd.append(i)
    
#     even.sort()     #將偶數陣列由小到大排序
#     even.reverse()  #將排序好的偶數陣列前後翻轉
#     odd.sort()      #將奇數陣列由小到大排序

#     for i in a:     #判斷原本輸入近來的陣列是奇數還是偶數
#         if i % 2 == 0:      #如果是偶數就將排序好的偶數陣列的第一個數字放進結果陣列
#             result.append(even[0])  #將偶數陣列的第一個數加入結果陣列
#             del even[0]     #將偶數陣列的第一個數刪除，後面的會往前遞補

#         else:
#             result.append(odd[0])   #將奇數陣列的第一個數加入結果陣列
#             del odd[0]  #將奇數陣列的第一個數刪除，後面的會往前遞補

#     return result

#**************************************************

#判斷大小交換位置

def sort_array(a):
    for i in range(0,len(a)):       #判斷每一個位置的值是偶數還是奇數，抓出第一個值
        if a[i]%2 == 0:             #如果是偶數
            for j in range(0,len(a)):   #再判斷每一個位置的值是偶數還是奇數
                if (a[j]%2 == 0 and a[i] > a[j]):   #如果第一次抓到的值比第二次的值大，就裡面的值交換位置
                    a[j] , a[i] = a[i] , a[j]

        else:
            for j in range(0,len(a)):   #再判斷每一個位置的值是偶數還是奇數，抓出第二個值
                if (a[j]%2 != 0 and a[i] < a[j]):   #如果第一次抓到的值比第二次的值小，就裡面的值交換位置
                    a[j] , a[i] = a[i] , a[j] 

    return a

print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 2, 8, 1, 4, 11]))
print(sort_array([2, 22, 37, 11, 4, 1, 5, 0]))
print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]))
print(sort_array([]))