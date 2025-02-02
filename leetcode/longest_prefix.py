class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_common_prefix = ""
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            char = shortest_str[i]
            if all([x[i] == char for x in strs]):
                longest_common_prefix += char
            else:
                return longest_common_prefix

        return longest_common_prefix


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["cir", "car"]))
