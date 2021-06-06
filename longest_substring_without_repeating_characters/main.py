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
    substr_char_count = []

    for ele in s:
        if ele not in substr:
            substr = substr + ele
        else:
            substr_char_count.append(len(substr))
            substr = ele

    return max(substr_char_count)
