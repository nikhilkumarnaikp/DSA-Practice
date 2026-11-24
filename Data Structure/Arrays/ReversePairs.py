class Solution(object):
    def reversePairs(self, nums):
        def merge_sort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid)
            count += merge_sort(mid + 1, right)

            # Count reverse pairs
            j = mid + 1

            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1

                count += j - (mid + 1)

            # Merge two sorted halves
            temp = []
            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= right:
                temp.append(nums[j])
                j += 1

            nums[left:right + 1] = temp

            return count

        return merge_sort(0, len(nums) - 1)

s= Solution()
nums= [1, 3, 2, 3, 1]
print(s.reversePairs(nums))

"""
output: 2
index 1, 4: 3 > 2 * 1
index 3, 4: 3 > 2 * 1
"""