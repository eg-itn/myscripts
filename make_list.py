# -*- coding: utf-8 -*-
import os
import sys


def make_list_from_two_path(path1, path2):
    """
    Make list from two path
    param path1: path1
    param path2: path2
    return: list of path
    """
    list1 = os.listdir(path1)
    list2 = os.listdir(path2)
    list1.sort()
    list2.sort()

    
    with open('data.list', 'w') as f:
        for i, file in enumerate(list1):
            str = os.path.join(path1, file) + ' ' + os.path.join(path2, list2[i])
            f.write(str + '\n')
            if os.path.splitext(file)[0] != os.path.splitext(list2[i])[0]:
                print(file, list2[i])
                input()

    return list1, list2


if __name__ == '__main__':
    path1 = 'data'
    path2 = 'gt'
    make_list_from_two_path(path1, path2)