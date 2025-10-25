'''Find All Anagrams in a String
Given two strings s and p, return an array of all the start 
indices of p's anagrams in s. You may return the answer in any order.'''


def findAnagrams(s, p):
    # Edge case: if s is shorter than p, no anagrams possible
    if len(s) < len(p):
        return []
    
    result = []
    
    # Step 1: Count letters in p
    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1
    
    # Step 2: Count letters in first window
    window_count = {}
    for i in range(len(p)):
        char = s[i]
        window_count[char] = window_count.get(char, 0) + 1
    
    # Step 3: Check if first window is an anagram
    if window_count == p_count:
        result.append(0)
    
    # Step 4: Slide the window through the rest of s
    for i in range(len(p), len(s)):
        # Add new character (right side of window)
        right_char = s[i]
        window_count[right_char] = window_count.get(right_char, 0) + 1
        
        # Remove old character (left side of window)
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        # Check if current window is an anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

