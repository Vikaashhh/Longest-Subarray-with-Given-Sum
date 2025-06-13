class Solution:
    def longestSubarray(self, arr, k):
        # Dictionary to store prefix_sum and its first index
        prefix_map = {}
        max_len = 0
        curr_sum = 0

        for i in range(len(arr)):
            curr_sum += arr[i]  # Current tak ka sum calculate karo

            # Agar current sum hi k hai to length = i + 1
            if curr_sum == k:
                max_len = i + 1

            # Agar pehle koi prefix sum aisa mila jiska difference k ho
            if (curr_sum - k) in prefix_map:
                length = i - prefix_map[curr_sum - k]
                max_len = max(max_len, length)

            # Store the first occurrence of curr_sum
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i

        return max_len
