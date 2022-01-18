import os
import glob
import argparse
import shutil


def pick_file_per_number(srcdir, dstdir, number):
    if not os.path.exists(dstdir):
        os.makedirs(dstdir)
    files = glob.glob(os.path.join(srcdir, '*.*'))
    files.sort()
    for i in range(len(files)):
        if i % number == 0:
            shutil.copy(files[i], dstdir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('srcdir', help='source directory')
    parser.add_argument('dstdir', help='destination directory')
    parser.add_argument('number', help='number of files to copy', type=int)
    args = parser.parse_args()
    pick_file_per_number(args.srcdir, args.dstdir, args.number)