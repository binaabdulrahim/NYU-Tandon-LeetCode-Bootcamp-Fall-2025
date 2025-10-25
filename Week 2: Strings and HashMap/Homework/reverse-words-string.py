'''Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.'''


def reverseWords(s):
    # Step 1: Split into words
    words = s.split()
    
    # Step 2: Reverse the list
    words.reverse()
    
    # Step 3: Join with single space
    result = " ".join(words)
    
    # Step 4: Return
    return result