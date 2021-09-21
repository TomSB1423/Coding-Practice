# Initial attempt - RUNTIME ERROR
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxs = 0
        for i in range(len(nums)):
            count = 0
            replace = k
            for j in range(len(nums)):
                if nums[j] == 1:
                    count += 1
                elif j >= i and replace > 0:
                    count += 1
                    replace -= 1
                else:
                    count = 0
                maxs = max(maxs, count)
        return maxs

# Second attempt - WITH COUNT VAR


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                k -= 1
                count += 1

            if k < 0:
                count -= 1
                if nums[j] == 0:
                    k += 1
                j += 1

            i += 1
        return count


# Third attempt - WITHOUT COUNT VAR (FINAL)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                k -= 1

            if k < 0:
                if nums[j] == 0:
                    k += 1
                j += 1

            i += 1
        return i-j
