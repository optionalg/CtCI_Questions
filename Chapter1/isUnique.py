# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Assuming any character set
def isUnique(input_string):
    # Brute force: For every character, scan the remaining string to see if there is another occurrence
    # Brute force runtime: O(N^2) time
    # Best Conceivable Runtime: O(N) because you need to scan all the characters once
    # Use a hash table to map character to a value, and if the key exists in the table then it means it has been used
    # O(N) to scan through string, O(1) to add to dict, total O(N) time
    hashTable = {}
    for char in input_string:
        if char in hashTable:
            return False
        hashTable[char] = 0
    return True


# Test cases
assert(isUnique(''))
assert(isUnique('a'))
assert(not isUnique('aa'))
assert(isUnique('aABb'))
assert(not isUnique('abcdea'))
assert(not isUnique('aaaaaaa'))