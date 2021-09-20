class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(numbers)):
            if numbers[i] not in store:
                store[target - numbers[i]] = i
            else:
                return [store[numbers[i]]+1, i+1]
