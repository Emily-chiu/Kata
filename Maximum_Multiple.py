# Given a Divisor and a Bound , Find the largest integer N , Such That 

def max_multiple(divisor, bound):
    while bound % divisor != 0:
        bound -= 1
    
    return bound

print("Basic tests")
print(max_multiple(2,7))
print(max_multiple(3,10))
print(max_multiple(7,17))
print(max_multiple(10,50))
print(max_multiple(37,200))
print(max_multiple(7,100))
print(max_multiple(37,100))
print(max_multiple(1,13))
print(max_multiple(1,1))
print(max_multiple(4,1))
print("<COMPLETEDIN::>")