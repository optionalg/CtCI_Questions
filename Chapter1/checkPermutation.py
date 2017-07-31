# Given two strings, write a method to decide if one is a permutation of the other

# Solution using a dictionary
def checkPermutationDict(string1, string2):
    # Count number of occurrences per character
    # Simple case: length are different
    if len(string1) != len(string2):
        return False

    # Use a dict
    charactersSeen = {}

    # Count occurrences in string1
    for char in string1:
        if char in charactersSeen:
            charactersSeen[char] += 1
        else:
            charactersSeen[char] = 1

    # Check occurrences in string2
    for char in string2:
        if char in charactersSeen:
            if charactersSeen[char] == 0:
                return False
            charactersSeen[char] -= 1
        else:
            return False
    
    return True

assert(checkPermutationDict('abc', 'abc'))
assert(checkPermutationDict('', ''))
assert(checkPermutationDict('abbbbba', 'bbaabbb'))
assert(checkPermutationDict('AaaAAaaab', 'bAAAaaaaa'))
assert(not checkPermutationDict('a', 'b'))
assert(not checkPermutationDict('', 'enlknr'))
assert(not checkPermutationDict('welknrewl', ''))
assert(not checkPermutationDict('ewrwe', 'onkok'))
assert(not checkPermutationDict('aaabbb', 'aaabbc'))
assert(not checkPermutationDict('ew', 'knlkn'))
assert(not checkPermutationDict('ew', 'eww'))

# Done by sorting strings
def checkPermutationSort(string1, string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)

assert(checkPermutationSort('abc', 'abc'))
assert(checkPermutationSort('', ''))
assert(checkPermutationSort('abbbbba', 'bbaabbb'))
assert(checkPermutationSort('AaaAAaaab', 'bAAAaaaaa'))
assert(not checkPermutationSort('a', 'b'))
assert(not checkPermutationSort('', 'enlknr'))
assert(not checkPermutationSort('welknrewl', ''))
assert(not checkPermutationSort('ewrwe', 'onkok'))
assert(not checkPermutationSort('aaabbb', 'aaabbc'))
assert(not checkPermutationSort('ew', 'knlkn'))
assert(not checkPermutationSort('ew', 'eww'))