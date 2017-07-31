# Given a string, write a function to check if it is a permutation of a palindrome.
# The palindrome does not need to be limited to just dictionary words.

# Count all occurrences, at most one character can be an odd number
# O(N) time to scan through string
# O(N) time to count number of odd # of occurrences
# Can use a list/array instead of dictionary if using ASCII/known character set
# Can sort the string and count occurrences as it goes for better space complexity
#   in which case check occurrence % 2 when character is different from previous
def isPalindromePermutation(input_string):
    charactersSeen = {}

    for char in input_string:
        if char in charactersSeen:
            charactersSeen[char] += 1
        else:
            charactersSeen[char] = 1
    
    oddExists = False

    for char in charactersSeen:
        if charactersSeen[char] % 2 == 1:
            if oddExists:
                return False
            oddExists = True
        
    return True

assert(isPalindromePermutation('aba'))
assert(isPalindromePermutation('weogknwegokn'))
assert(isPalindromePermutation('werlknwerlknh'))
assert(not isPalindromePermutation('weroknwerkni'))
assert(isPalindromePermutation(''))