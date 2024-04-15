import os
os.mkdir("testdir")
os.mkdir("testdir/subdir")
os.chmod("testdir", 0o111)

O_SEARCH = (0x40000000 | 0x00100000)

# linux: O_SEARCH = 0o10000000

fd = os.open("testdir", O_SEARCH)
os.fchdir(fd)
os.open("subdir", O_SEARCH)
