# Greed is a dice game played with five six-sided dice. 
# Your mission, should you choose to accept it, is to score a throw according to these rules. 
# You will always be given an array with five six-sided dice values.

# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point

# test.describe("Example Tests")
# test.it("Example Case")
# test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
# test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
# test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)

def score(dice):
    count_list = [dice.count(1),dice.count(2),dice.count(3),dice.count(4),dice.count(5),dice.count(6)]
    sum_list = []

    for ns in range(len(count_list)):
        if ns == 0:     #1
            if count_list[ns] >= 3:
                sum_list.append(1000)
                count_list[ns] = count_list[ns] - 3
        
        else:
            if count_list[ns] >= 3:
                sum_list.append(100*(ns+1))
                count_list[ns] = count_list[ns] - 3
    
    if count_list[0] != 0:  #1
        sum_list.append(100*count_list[0])
    
    if count_list[4] != 0:  #5
        sum_list.append(50*count_list[4])

    return sum(sum_list)

print("Example Tests")
print("Example Case")
print( score( [2, 3, 4, 6, 2] ), 0)
print( score(  [4, 4, 4, 3, 3] ), 400)
print( score(  [2, 4, 4, 5, 4] ), 450)