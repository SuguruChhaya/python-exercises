
# *Approach 1, brute-force: search through list twice: time complexity: O^2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in range(0, len(nums)):
            # *So much easier to use range instead
            print("first loop")
            #!I have to make sure they are not the same number
            for b in range(0, len(nums)):
                # *Somehow the indexes are messed up
                #!This is because the numbers are the same and the index system doesn't work properly
                # *I would use range from now on
                if nums[a] + nums[b] == target and a != b:
                    return [a, b]


'''
a = Solution()
print(a.twoSum([3, 3], 6))

class SecondSolution(object):
    def twoSum(self, nums, target):
        h = {}
        for a, b in 
'''


class SecondSolution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        #!The enumerate method assigns a count in form of tuples
        for i, num in enumerate(nums):
            n = target - num
            if n


a = SecondSolution()
print(a.twoSum([2, 4, 5], 9))

# *When asked if an element is in a dictionary, it looks through the keys
'''
my_dict = {0: 1, 2: 3}
print(1 in my_dict.values())
'''
