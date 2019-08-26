# Pair of gloves
# Winter is comming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# A pair of gloves is constituted of two gloves of the same color.

# You are given an array containing the color of each glove.

# You must return the number of pair you can constitute.

# You must not change the input array.

# Test.describe("Basic tests")
# Test.assert_equals(number_of_pairs(["red","red"]),1)
# Test.assert_equals(number_of_pairs(["red","green","blue"]),0)
# Test.assert_equals(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
# Test.assert_equals(number_of_pairs([]),0)
# Test.assert_equals(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4)

def number_of_pairs(gloves):
    sum = 0
    for i in set(gloves):
        if gloves.count(i) != 1:
            sum += gloves.count(i)//2
    return sum

print("Basic tests")
print(number_of_pairs(["red","red"]),1)
print(number_of_pairs(["red","green","blue"]),0)
print(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
print(number_of_pairs([]),0)
print(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4)