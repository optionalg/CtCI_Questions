# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check
# if they are one edit (or zero edits) away.

# Strings are different in length by >=2 then false
# If strings are same length, go through the strings a character at a time for both and return false
# if more than 1 character changed
# Removal of a character is the same as an insert except switching the two strings
# To check inserting of a character, go through both strings one character at a time and if there is a mismatch,
# set a flag and move the character for the longer string ahead by one

# O(N) to scan first string
# O(N) to scan second string
# O(N) runtime

def isOneAway(string1, string2):
    # Swap so len(string1) <= len(string2)
    if len(string1) > len(string2):
        string1, string2 = string2, string1

    # At least two away
    if len(string2) - len(string1) >= 2:
        return False
        
    # Check for edit
    if len(string1) == len(string2):
        encounteredEdit = False
        for i in range(0, len(string1)):
            if string1[i] != string2[i] and encounteredEdit:
                return False
            elif string1[i] != string2[i]:
                encounteredEdit = True
        return True

    # Check for insert
    i, j = 0, 0 # i = index of string1, j = index of string2
    while i < len(string1):
        if (string1[i] != string2[j] and i != j):
            return False
        elif (string1[i] != string2[j]):
            j += 1
        else:
            i += 1
            j += 1
    
    return True

assert(isOneAway('jason', 'jason'))
assert(isOneAway('jason', 'bason'))
assert(isOneAway('jason', 'jasob'))
assert(isOneAway('jason', 'jaron'))
assert(not isOneAway('jason', 'jasir'))
assert(not isOneAway('jason', 'wdenr'))

assert(not isOneAway('jason', 'liu'))
assert(not isOneAway('liu', 'jason'))

assert(isOneAway('jason', 'jaso'))
assert(isOneAway('jason', 'ason'))
assert(isOneAway('jason', 'jaon'))
assert(isOneAway('jaon', 'jason'))
assert(isOneAway('ason', 'jason'))
assert(isOneAway('jaso', 'jason'))
assert(not isOneAway('jason', 'lson'))
assert(isOneAway('', 'a'))
assert(isOneAway('a', ''))