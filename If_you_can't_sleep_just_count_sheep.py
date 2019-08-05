# Test.assert_equals(count_sheep(1), "1 sheep...");
# Test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
# Test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")

def count_sheep(n):
    sheep = ''
    for time in range(1,n+1):
        sheep += '%d sheep...'%time
    
    return sheep

print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))