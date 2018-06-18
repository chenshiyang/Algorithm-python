class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        leetcode 第三题

        示例：
        abbcad
        initial: start = 0 length = 0 maxLength = 0
        i = 0, => start = 0 length = 1 maxLength = 1 charMap = {a:0}
        i = 1, => start = 0 length = 2 maxLength = 2 charMap = {a:0, b:1}
        i = 2, => start = charMap[b] + 1 = 2 length = 1 maxLength = 2 charMap = {a:0 b:2}
        i = 3, => start = 2 length = 2 maxLength = 2 charMap = {a:0, b:2, c:3}
        i = 4, => start = 2, length = 3 maxLength = 3 charMap = {a:4 b:2 c:3}
        i = 5, => start = 2, length = 4 maxLength = 4 charMap = {a:4 b:2 c:3 d:5}

        return maxLength = 4
        核心思想：
        用一个map来记录每个字符的最新出现位置，如果字符没有出现过或者其上一次出现的位置在当前
        积累的子串的起始位置之前，那么该字符不会对子串的延伸有影响
        如果字符上一次出现的位置在当前子串的起始位置之后，那么子串要重新开始积累

        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        charMap = {}
        maxLength = 0
        length = 0
        start = 0
        for i in range(len(s)):
            if not s[i] in charMap:# 如果当前字符以前没有出现过
                length += 1
                charMap[s[i]] = i # 记录当前字符出现的地址
                maxLength = max(maxLength, length)
            else:
                if charMap[s[i]] < start:# 如果当前字符之前出现过，但其出现的地方在当前子字符串的起始地址之前，
                    length += 1               # 则不影响当前子字符串的延伸
                    charMap[s[i]] = i #更新当前字符的最新出现地址
                    maxLength = max(maxLength, length)
                else:
                    start = charMap[s[i]] + 1 # 新的子字符串的起始地址从重复的这个字符的下一个地方开始
                    length = i - start + 1
                    charMap[s[i]] = i
                    maxLength = max(maxLength, length)
        return maxLength


if __name__ == '__main__':
    so = Solution()
    s1 = "abcdabc"#4
    s2 = "abcad"#4
    s3 = "aabb"#2
    print(so.lengthOfLongestSubstring(s1))
    print(so.lengthOfLongestSubstring(s2))
    print(so.lengthOfLongestSubstring(s3))