arr1 = [0, 3, 4, 31]
arr2 = [4, 6, 30]

# arr1.extend(arr2)
# print(sorted(arr1))

class Solution:
    def merge_sortedarray(self, arr1, arr2):
        i, j = 0, 0
        arr3 = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr3.append(arr1[i])
                i += 1
            elif arr2[j] < arr1[i]:
                arr3.append(arr2[j])
                j += 1
        print(i, j, arr3, arr2[j:])
        print("A1: ", arr1)        
        return arr3 + arr1[i:] + arr2[j:]  



obj = Solution()
print(obj.merge_sortedarray(arr1, arr2))