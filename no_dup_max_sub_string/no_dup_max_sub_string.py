def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        max_sub,start = 0,0
        for j in range(len(s)):
            if s[j] in res:
                start = max(res[s[j]], start)
            max_sub = max(max_sub,j-start+1)
            res[s[j]] = j+1
        return max_sub

if __name__ == "__main__":
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
