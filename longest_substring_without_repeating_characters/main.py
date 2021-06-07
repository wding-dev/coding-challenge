"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "pwwkew"
Output: 3
"""


def solution(s: str) -> int:

    substr = ""
    max_substr_length = 0

    for ele in s:

        if ele not in substr:
            substr = substr + ele
        else:
            substr = substr[substr.index(ele)+1:] + ele

        if max_substr_length < len(substr):
            max_substr_length = len(substr)

    return max_substr_length
