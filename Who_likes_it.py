# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

# Test.assert_equals(likes([]), 'no one likes this')
# Test.assert_equals(likes(['Peter']), 'Peter likes this')
# Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
# Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
# Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    
    elif len(names) == 1:
        return names[0] + ' likes this'

    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    
    elif len(names) == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others like this'

print(likes([]), 'no one likes this')
print(likes(['Peter']), 'Peter likes this')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')