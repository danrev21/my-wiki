#!/usr/bin/env python

# Create a program that compares two directories and reports the differences between them.

# Output:
# Unique files in each directory.
# Files that are in both directories but differ.
# A summary report of the findings.

# Tips:
# Use the filecmp module for comparing files and directories.
# Consider the dircmp class for detailed comparisons.

import filecmp

def comparison_dirs(dir1 = 'dir1', dir2 = 'dir2'):

    # Create a directory comparison object
    comparison = filecmp.dircmp(dir1, dir2)

    # Access comparison results
    print(f"Unique files in {dir1}: {comparison.left_only}")
    print(f"Unique files in {dir2}: {comparison.right_only}")
    print(f"Files that are in both directories but differ: {comparison.diff_files}")
    print("\nA summary report of the findings:")
    print(comparison.report())

if __name__ == "__main__":
    comparison_dirs()




