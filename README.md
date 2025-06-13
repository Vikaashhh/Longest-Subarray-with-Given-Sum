# 📅 Day 62 – GFG 160 Days DSA Challenge
### 🧪 Problem: Longest Subarray with Sum K
### 💡 Difficulty: Medium
### 📌 Tags: #Day62 #gfg160 #geekstreak2025
### 🧠 Solved In: 1st Attempt ✅

## 📘 Problem Statement:
Given an array of integers and an integer K, the objective is to determine the length of the longest subarray that sums exactly to K.

## 💡 Intuition:
A brute-force approach would check all subarrays, resulting in O(n²) time — not scalable.
The optimal solution involves prefix sums and hash mapping to track previously seen sums, reducing time complexity to linear.

## ⚙️ Optimized Strategy:
1. Maintain a cumulative sum (curr_sum) as we traverse.

2. Use a hash map (prefix_map) to store the first occurrence of each prefix sum.

3. For each index i:

- If curr_sum == k, update the answer to i + 1.

- If (curr_sum - k) exists in prefix_map, it implies a subarray summing to k exists.

- Store curr_sum in the map if it hasn’t been seen before.

## 📊 Submission Stats:
- ✅ Test Cases Passed: 1115 / 1115

- 🧠 Accuracy: 100%

- 🎯 Attempts: 1 / 1

- ⏱️ Execution Time: 1.03 sec

- 🏅 Points Earned: 4 / 4

- 📈 Total Score: 231


## 📈 Time & Space Complexity:
- Time Complexity: O(n)

- Space Complexity: O(n)

## 💬 Reflection:
This problem refined my understanding of prefix sums and hash-based lookups, which are crucial in time-efficient data handling — especially useful in state management, analytics, and real-time UI rendering.


## 📢 Hashtags:
#Day62 #gfg160 #geekstreak2025
#longestsubarray #prefixsum #hashmap
#problemSolving #dsachallenge #pythonlogic
#devjourney #frontenddeveloper #framesbyvikash
