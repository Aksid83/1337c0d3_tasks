"""
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. 
From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

# Solution 1
def isPalindrome_v1(self, x: int) -> bool:
        sx = str(x)
        return sx == sx[::-1]

# Solution 2
def isPalindrome_v2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
           return False
        rev = 0
        while x > rev:
           rev = rev * 10 + x % 10
           x //= 10
        return x == rev or x == rev//10