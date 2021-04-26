# Eluvio Core Engineering Challenge

### Problem

Given a large number of binary files, write a program that finds the
longest strand of bytes that is identical between two or more files.

### Input

Binary files that are placed into the input directory.

### Algorithm

1. Grab all binary files in the input directory and convert them into byte arrays
2. For each possible pair of binary files, find the longest common substring and continuously compare the length of each substring to find the longest common substring between any 2 files
3. Find all binary files that contain this longest substring as well as the offset of where this substring first occurs
4. Print output

### Time and Space Complexity

N = total number of binary files in input
M = largest file size in input

Time Complexity: O((N(N-1)/2) * M^2) -> O(N^2 * M^2)

The time complexity is dominated by step 2 of the algorithm, where there are N(N-1) / 2 total possible combinations of binary file pairs and for each pair it takes O(M^2) time to find the longest common substring

Space Complexity: O(N*M)

This is the space it takes to store all the binary files into the byte dictionary

### How To Run The Program:

`python3 main.py`

### Sample Output
