# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

# Test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
# Test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
# Test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
# Test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
# Test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
# Test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")

def queue_time(customers, n):
    n_list = []
    if n == 1 :
        return sum(customers)
    
    else:
        time = 1
        n_list = customers[:n]
        del customers[:n]
        for i in range(len(n_list)):
            n_list[i] = [n_list[i]]
        
        while len(customers) != 0:
            for nn in range(len(n_list)):
                if len(customers) != 0:
                    if (sum(n_list[nn])-time) <= 0:
                        n_list[nn] += [customers.pop(0)]

                else:
                    break
                    
            time += 1
                
    for nn in range(len(n_list)):
        n_list[nn] = sum(n_list[nn])

    return max(n_list)



# print(queue_time([], 1), 0)
# print(queue_time([5], 1), 5)
# print(queue_time([2], 5), 2)
# print(queue_time([1,2,3,4,5], 1), 15)
# print(queue_time([1,2,3,4,5], 100), 5)
print(queue_time([43, 3, 17, 16, 27, 22, 50, 14, 48, 23, 48, 18], 5))

