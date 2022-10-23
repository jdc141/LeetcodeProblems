class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapOfSToT = {}
        mapOfTToS = {}
        for char1, char2 in zip(s,t):
            if (char1 not in mapOfSToT) and (char2 not in mapOfTToS):
                mapOfSToT[char1] = char2
                mapOfTToS[char2] = char1
            if (mapOfSToT.get(char1) != char2) or (mapOfTToS.get(char2) != char1):
                return False
        
        return True
        