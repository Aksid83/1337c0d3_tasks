"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""

# Pythonic!
def longestCommonPrefixPythonic(strs: list([str])) -> str:
    import os
    return os.path.commonprefix(strs)

# Python zip() solution :(
def longestCommonPrefix(strs: list([str])) -> str:
        pref = ""
        # Checking for empty list or list of empty strings
        if len(strs) == 0 or len(strs[0]) == 0: 
            return pref
        # Checking if list has one not empty string
        if len(strs) == 1:
            return strs[0]
        # Returning tuple of corresponding letters from each element in the list    
        for x in zip(*strs):
            # Checking if all the letters are the same 
            if len(set(x)) == 1:
                # If same letters adding the letter to prefix
                pref += x[0]        
            else:
                # If at least one letter is different, common prefix is done, exiting the loop
                break
        return pref

# Horisontal scanning method
def longestCommonPrefixHorScan (strs: list([str])) -> str:
    n = len(strs)
    if n == 0 or len(strs[0]) == 0:
        return ""
    if n == 1:
        return strs[0]
    pref = strs[0]
    for i in range(1, n):
        while strs[i].find(pref) != 0:
            pref = pref[:-1]
            if len(pref) == 0: return ""
    return pref

# Vertical scanning method
def longestCommonPrefixVertScan (strs: list([str])) -> str:
    n = len(strs)
    if n == 0 or len(strs[0]) == 0:
        return ""
    if n == 1:
        return strs[0]
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, n):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]          
    return strs[0]
