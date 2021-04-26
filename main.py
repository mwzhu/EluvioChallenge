import os
from pathlib import Path
from itertools import combinations

# Helper function to find the longest common substring given two strings
def findLongestCommonSubstring(stringOne, stringTwo):
    # Initialize DP matrix, length and index trackers, and output
    m = len(stringOne)
    n = len(stringTwo)
    lengths = [[0 for i in range(n + 1)] for j in range(m + 1)]
    maxLength = 0
    outputString = ''

    # Iterate through each pair of letters and populate DP matrix
    for i in range(m + 1):
        for j in range(n + 1):

            if (i == 0 or j == 0):
                lengths[i][j] = 0

            elif (stringOne[i-1] == stringTwo[j-1]):
                lengths[i][j] = lengths[i-1][j-1] + 1

                if (lengths[i][j] > maxLength):
                    maxLength = lengths[i][j]
                    start = i - maxLength

            else:
                lengths[i][j] = 0

    # Build and return output
    if maxLength > 0:
        outputString = stringOne[start : start + maxLength]

    return outputString

# Helper function to find all files and offsets that contain the given substring -> returns a list of lists
def findFilesWithSubstring(files, substring):
    output = []
    for fileName, fileString in files.items():
        if fileString.find(substring) != -1:
            output.append([fileName, fileString.find(substring)])
    return output

# Main driver function that handles inputs and outputs
def main():
    # Initialize byte dictionary to store files, maxLength tracker, and substring
    bytes = {}
    maxLength = 0
    maxSubstring = ""

    #Populate bytes dictionary
    for file in os.listdir("input"):
        bytes[file] = Path("./input/" + file).read_bytes()

    # Iterate through each pair of files and find the longest common substring between 2 files
    for file_pair in combinations(bytes, 2):
        fileOne = bytes[file_pair[0]]
        fileTwo = bytes[file_pair[1]]
        substring = findLongestCommonSubstring(fileOne, fileTwo)
        substringLength = len(substring)

        # Update maxLength tracker and output variables if we have found a longer common substring
        if substringLength > maxLength:
            maxLength = substringLength
            maxSubstring = substring

    # Find all files that contain the substring
    outputList = findFilesWithSubstring(bytes, maxSubstring)

    # Print Output
    print("Length of Longest Strand: " + str(maxLength))
    print("Files that contain longest strand and offset: ")
    for file in outputList:
        fileName = file[0]
        fileOffset = file[1]
        print(fileName + ": " + str(fileOffset))

if __name__ == "__main__":
    main()
