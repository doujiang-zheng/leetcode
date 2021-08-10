class Solution:
    def isPrefixString(self, s: str, words) -> bool:
        flag = True
        for k in range(len(words)):
            if len(s) <= 0 or flag is False:
                break
            w = words[k]
            flag = flag and s.startswith(w)
            s = s[len(w):]
        return flag and len(s) <= 0


if __name__ == '__main__':
    sol = Solution()
    s = ["iloveleetcode", "iloveleetcode", "a", "aaa"]
    words = [["i", "love", "leetcode", "apples"],
             ["apples", "i", "love", "leetcode"], ["aa", "aaaa", "banana"],
             ["aa", "aaa", "fjaklfj"]]
    for es, ewords in zip(s, words):
        print(sol.isPrefixString(es, ewords))
