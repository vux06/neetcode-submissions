class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        symbols = list((r'!@#$%^&*(<>[]''\',.;+{}"|\:"<>?'))
        for i in s:
            if (i in symbols):
                s=s.replace(i,"")
        return s == s[::-1]
        return s == s[::-1]
        