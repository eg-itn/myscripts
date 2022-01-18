import os
import shutil
import argparse


def copy_file(src_list, folder1, folder2):
    with open(src_list, 'r') as list:
        for line in list:
            src = line.strip()
            src = os.path.join(folder1, src)
            src_basename, _ = os.path.splitext(src)
            if os.path.isfile(src):
                dst = os.path.join(folder2, line.strip())
                dst_basename, _ = os.path.splitext(dst)
                if not os.path.exists(os.path.dirname(dst)):
                    os.makedirs(os.path.dirname(dst))
                print(f'{src} to {dst}')
                shutil.copy(src, dst)
                shutil.copy(src_basename + '.txt', dst_basename + '.txt')
                shutil.copy(src_basename + '.json', dst_basename + '.json')
            else:
                print(f'file not found: {src}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src_list', required=True)
    parser.add_argument('-f1', '--folder1', required=True)
    parser.add_argument('-f2', '--folder2', required=True)
    args = parser.parse_args()
    copy_file(args.src_list, args.folder1, args.folder2)