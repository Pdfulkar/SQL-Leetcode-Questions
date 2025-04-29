class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = list(s)
        b = list(t)
        d = []
        for i in a:
                if i in b:
                    d.append(i)
        for p in d:
            if p in b:
                b.remove(p)
        if len(b) > 1 or len(b) == 0:
            return 0 
        else:
            return b[0]