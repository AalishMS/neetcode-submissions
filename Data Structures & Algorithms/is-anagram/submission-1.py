class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)==len(s):
            c=0
            s_list = list(s)
            for each in t:
                if each in s_list:
                    s_list.remove(each)
                    c=c+1
            if c==len(t):
                return True
            else:
                return False
        else:
            return False