class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1,len(arr)):
            if diff != arr[i] - arr[i-1]:
                return False
        
        return True
        