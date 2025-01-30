class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i, c in enumerate(word1):
            result += c
            try:
                result += word2[i]
            except IndexError:
                result += word1[i+1:]
                return result
        result += word2[len(word1):]
        return result

print("should be apbqcr")
res = Solution().mergeAlternately("abc", "pqr")
print(res)

print("should be apbqcd")
res = Solution().mergeAlternately("abcd", "pq")
print(res)

print("should be apbqrs")
res = Solution().mergeAlternately("ab", "pqrs")
print(res)

print("edge cases")
res = Solution().mergeAlternately("oasifhnaosfi", "")
print(res)

res = Solution().mergeAlternately("", "")
print(res)
