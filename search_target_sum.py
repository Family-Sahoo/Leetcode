class Solution:
    def get_indices(self, arr, sum):
        dict = {}
        for i in range(len(arr)):
            temp = sum - arr[i]
            if temp == 0:
                return [i, arr[i]]
            if temp in dict:
                return [arr[dict[temp]], arr[i]]
            dict[arr[i]] = i    

arr, sum = [2, 0, 5], 7
sol = Solution()
print(sol.get_indices(arr, sum))
