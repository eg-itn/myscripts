import sys
import os
import shutil
import argparse
from datetime import datetime as dt


def main(args):
    # コピー先がない場合作る
    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)

    # リストファイルを開く
    with open(args.list, 'r') as f:
        line = f.readline().rstrip()
        while line:
            print(line)
            copy_from = os.path.join(args.inputdir, line)
            copy_to = os.path.join(args.outputdir, line)
            shutil.copy2(copy_from, copy_to)
            line = f.readline().rstrip()


if __name__ == "__main__":
    # 受け取る引数を追加する

    parser = argparse.ArgumentParser(description='対象ファイルコピーツール')  # parserを定義

    parser.add_argument('inputdir', type=str, help='コピー元')  # 必須の引数を追加
    parser.add_argument('list', type=str, help='対象ファイルのリスト')  # 必須の引数を追加
    parser.add_argument('outputdir', type=str, help='コピー先')  # 必須の引数を追加

    parser.add_argument('--opt', help='オプション', metavar='OPTION_STR')

    args = parser.parse_args()  # 引数を解析

    time1 = dt.now()
    main(args)
    time2 = dt.now()
    # sys.stdout.write('Start: {}\n'.format(time1))
    # sys.stdout.write('End  : {}\n'.format(time2))
    sys.stdout.write('Elapsed time[ALL]:     {}\n'.format(time2 - time1))
