class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                start = num
                while start in num_set:
                    start += 1
                    longest = max(longest, start - num)
        return longest