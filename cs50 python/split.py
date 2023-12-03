from os.path import splitext
import sys
file1 = splitext(sys.argv[1])
file2 = splitext(sys.argv[2])
print(file1, file2)