'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
strs = ["flower","flow","flight"]
# strs = ["c", "cacc", "ccc"]
# strs = ["abca", "aba", "aaab"]

print(sorted(strs))


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_world = min(strs, key=len)
        if len(min_world) != 0 and all(strs[0][0] in strs[i][0] for i in range(len(strs))):  # проверяем что все слова начинаются с одной буквы
            for i in range(len(min_world)):
                if all(min_world[:len(min_world) - i] in strs[n][:len(min_world) - i] for n in range(len(strs))):
                    return min_world[:len(min_world) - i]
        else:
            return ''




x = Solution().longestCommonPrefix(strs)
print(x)

