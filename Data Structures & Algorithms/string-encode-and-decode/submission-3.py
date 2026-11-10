class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            length = len(string)
            res += str(length) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) if s[i:j].strip() else 0

            res.append(s[j + 1 : j + 1 + length])
        
            i = j + 1 + length

        return res