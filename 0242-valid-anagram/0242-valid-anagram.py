class Solution:
    def isAnagram(self, s, t):

        #to check length 
        if len(s) != len(t):
            return False

        #to sort both the strings 
        if sorted(s) == sorted(t):
            return True
        
        return False