class Solution:
    def romanToInt(self, s: str) -> int:
        store = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}
        add = 0
        prev = 0
        for val in reversed(s):
            if store[val] < prev:
                add -= store[val]
            else:
                add += store[val]
            prev = store[val]
        return add
