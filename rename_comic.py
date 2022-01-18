import glob
import os
import shutil
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='')  # parserを定義

    parser.add_argument('input')  # 必須の引数を追加
    parser.add_argument('output')  # 必須の引数を追加
    args = parser.parse_args()  # 引数を解析

    if not os.path.isdir(args.output):
        os.makedirs(args.output)

    for i, directory in enumerate(glob.iglob(os.path.join(args.input, '*'))):
        try:
            if "후" in directory:
                fore_dir = directory.replace("후", "전")
                lastfile = list(glob.iglob(fore_dir + '/*.*'))[-1]
                filename = os.path.basename(lastfile)
                filename, ext = os.path.splitext(filename)
                num = int(filename)

                cnt = 0
                for fullname in glob.glob(directory + '/*.*'):
                    cnt += 1
                    # print(fullname)
                    dirname = os.path.dirname(fullname)
                    dirnames = os.path.split(dirname)
                    basedir = dirnames[-1]
                    basename = os.path.basename(fullname)
                    filename, ext = os.path.splitext(basename)

                    new_num = cnt + num
                    new_num = '{:04d}'.format(new_num)
                    new_basename = new_num + ext
                    fore_dir = os.path.split(fore_dir)[-1]
                    new_fullname = os.path.join(args.output, fore_dir, new_basename)

                    print(new_fullname)
                    if not os.path.isdir(os.path.join(args.output, fore_dir)):
                        os.makedirs(os.path.join(args.output, fore_dir))
                    shutil.copy2(fullname, os.path.join(args.output, fore_dir, new_basename))
            elif "전" in directory:
                for fullname in glob.glob(directory + '/*.*'):
                    dirname = os.path.dirname(fullname)
                    dirnames = os.path.split(dirname)
                    basedir = dirnames[-1]
                    basename = os.path.basename(fullname)
                    print(os.path.join(args.output, basedir, basename))
                    if not os.path.isdir(os.path.join(args.output, basedir)):
                        os.makedirs(os.path.join(args.output, basedir))
                    shutil.copy2(fullname, os.path.join(args.output, basedir, basename))
            else:
                continue
            # if i > 2:break
            # print(fullname)

            # print(f"dirname: {dirname}, basename: {basename}, filename: {filename}, ext: {ext}")


        # filename, ext = os.path.splitext(os.path.basename(fullname))
        # if not (type(int(filename[0:14])) == int and filename[14] == '_'): continue
        #
        # year = filename[0:4]
        # month = filename[4:6]
        # day = filename[6:8]
        # hh = filename[8:10]
        # mm = filename[10:12]
        # ss = filename[12:14]
        # # print(year, month, day, hh, mm, ss)
        # outname = '-'.join([year, month, day + ' ' + hh, mm, ss, '000' + ext])
        # print(outname)
        # shutil.copy2(fullname, os.path.join(sys.argv[1], outname))
        #
        except Exception as e:
            import traceback
            print(traceback.format_exc())



if __name__ == "__main__":
    main()
