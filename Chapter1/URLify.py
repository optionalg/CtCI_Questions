# Write a method to replace all spaces in a string with '%20'.

def URLify(input_string):
    return input_string.strip().replace(' ', '%20')

assert(URLify('google.ca/hi dude') == 'google.ca/hi%20dude')
assert(URLify('google.ca/hidude    ') == 'google.ca/hidude')
assert(URLify('google.ca/hi') == 'google.ca/hi')
assert(URLify('google .ca /   e   ') == 'google%20.ca%20/%20%20%20e')