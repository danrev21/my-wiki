


# File and Directory Comparison
# Overview of the filecmp Module

# Comparing Files
cmp(file1, file2, shallow=True)
cmp compares two files and returns True if they are identical, False otherwise.
- shallow mode: where only metadata of the files are compared like the size, date modified, etc.
- deep mode: where the content of the files are compared.

# Example:
import filecmp
result = filecmp.cmp('file1.txt', 'file2.txt')
print(f"Files are {'identical' if result else 'different'}.")

# Comparing Directories
dircmp(same_files, diff_files, report=False)
dircmp compares two directories and their contents, providing detailed information.

same_files: List of filenames existing in both directories.
diff_files: List of filenames existing in one directory but not the other.
report: Boolean flag indicating whether to print a detailed comparison report.

# Example:

import filecmp

dir1 = '/path/to/directory1'
dir2 = '/path/to/directory2'

# Create a directory comparison object
comparison = filecmp.dircmp(dir1, dir2)

# Access comparison results
print(f"Common files: {comparison.common}")
print(f"Files only in {dir1}: {comparison.left_only}")
print(f"Files only in {dir2}: {comparison.right_only}")
print(f"Differences between common files: {comparison.diff_files}")

# Optionally, print a comparison report
if report:
    comparison.report()

----------------------------------------------------------------------------
# This is the constructor. a and b are directories to be compared. By default system files in the directories are hidden and ignored in comparison

filecmp.dircmp(a,b)

result = filecmp.dircmp('dir1', 'dir2')

----------------------------------------------------------------------------

# This function makes comparison of files in two directories and returns a three item tuple. 
filecmp.cmpfiles("./dir1", "./dir2", common, shallow = True)

a, b -- directory names
common -- list of file names found in both directories
shallow -- if true, do comparison based solely on stat() information

    Returns a tuple of three lists:
      files that compare equal
      files that are different
      filenames that aren't regular files.

------------------------------------------------------------------------
# This method prints result of comparison between directories.

report()

result = filecmp.dircmp('dir1', 'dir2')
result.report()
# output:
diff dir1 dir2
Only in dir1 : ['newfile.txt']
Identical files : ['file1.txt']
Differing files : ['file2.txt']    

--------------------------------------------------------------------------
filecmp.dircmp??

"""A class that manages the comparison of 2 directories.

    dircmp(a, b, ignore=None, hide=None)
      A and B are directories.
      IGNORE is a list of names to ignore,
        defaults to DEFAULT_IGNORES.
      HIDE is a list of names to hide,
        defaults to [os.curdir, os.pardir].

    High level usage:
      x = dircmp(dir1, dir2)
      x.report() -> prints a report on the differences between dir1 and dir2
       or
      x.report_partial_closure() -> prints report on differences between dir1
            and dir2, and reports on common immediate subdirectories.
      x.report_full_closure() -> like report_partial_closure,
            but fully recursive.

    Attributes:
     left_list, right_list: The files in dir1 and dir2,
        filtered by hide and ignore.
     common: a list of names in both dir1 and dir2.
     left_only, right_only: names only in dir1, dir2.
     common_dirs: subdirectories in both dir1 and dir2.
     common_files: files in both dir1 and dir2.
     common_funny: names in both dir1 and dir2 where the type differs between
        dir1 and dir2, or the name is not stat-able.
     same_files: list of identical files.
     diff_files: list of filenames which differ.
     funny_files: list of files which could not be compared.
     subdirs: a dictionary of dircmp instances (or MyDirCmp instances if this
       object is of type MyDirCmp, a subclass of dircmp), keyed by names
       in common_dirs.
     """
     