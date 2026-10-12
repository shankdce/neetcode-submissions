class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for s in strs:
            encodeStr += str(len(s)) + '#' + s
        return encodeStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            len1 = int(s[i:j])
            res.append(s[j+1:j+1+len1])
            i = j+1+len1
        return res 
