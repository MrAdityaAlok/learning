# Amazon Summer School (2026)

"""
Problem Statement:
Alex is given a bracket sequence seq of length n. He found a way to calculate the difficulty of this sequence.
The sequence consists of balanced brackets which means every [ is paired with a corresponding ] which comes after it.
The difficulty of the sequence is the sum of distances between these brackets.

For the sequence ([][]):
Distance between the [ at position 1 and the ] at position 4 = 4-1=3;
Distance between the [ at position 2 and the ] at position 3 = 3-2=1;
Distance between the [ at position 5 and the ] at position 6 = 6-5=1.
The difficulty of the sequence = 3+1+1=5.

You are given a damaged form of sequence seq in which only the even positions have characters.
You need to find the brackets that should be placed in the odd positions such that the difficulty of the
resultant sequence is minimum and the brackets remain balanced.

Input Format:
- The first line of input contains a single integer N, the length of string seq.
- The second line of input contains a string seq of length N, where all characters at odd positions are '_'
  and all characters at even positions are either '[' or ']'.

Output Format:
- Output the minimum difficulty of the resultant sequence.

Constraints:
- 2 <= N <= 10^2
- N is even.
"""

from typing import List, Tuple
import sys


def solve_sequence(seq: str) -> int:
    stack: List[Tuple[str, int]] = []
    p, d = 0, 0

    for s in seq:
        p += 1

        if s == "_" and not stack:
            stack.append(("[", p))

        # if it is closing bracket or we would be adding a closing bracket, then pop:
        elif s == "]" or (s == "_" and stack[-1][0] == "["):
            _, position = stack.pop()
            d += p - position

        elif s == "[" or s == "_":
            stack.append(("[", p))

    return d


print(solve_sequence(sys.argv[1]))
