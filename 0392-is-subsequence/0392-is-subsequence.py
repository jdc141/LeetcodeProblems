class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pL = pR = 0
        
        while pL < len(s) and pR < len(t):
            if s[pL] == t[pR]:
                pL += 1
            pR += 1
            
        return pL == len(s)