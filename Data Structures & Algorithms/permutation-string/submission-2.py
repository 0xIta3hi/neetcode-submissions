class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # simply check if the same character's with same frequency appear in s2 if appear ? true : false
        if len(s1) > len(s2): return False
        s1_count = {}
        window = {}

        # build the frequency count
        for c in s1:
            s1_count[c] = s1_count.get(c,0) + 1
        
        # build the window
        for c in s2[:len(s1)]:
            window[c] = window.get(c,0) + 1
        
        if window == s1_count: return True

        for r in range(len(s1), len(s2)):
            incoming = s2[r]
            outgoing = s2[r - len(s1)]

            window[incoming] = window.get(incoming, 0) + 1

            window[outgoing] -= 1
            if window[outgoing] == 0:
                del window[outgoing]
            if window == s1_count:
                return True
        return False