class custom_lt(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        sorted_array = ''.join(sorted(map(str, nums), key = custom_lt))
        return '0' if sorted_array[0] =='0' else sorted_array 