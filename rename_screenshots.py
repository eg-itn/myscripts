import os, sys, shutil
import argparse
import glob
from multiprocessing import JoinableQueue, Process, cpu_count

def rename_potplayer(file, prefix, outdir):
    if file.endswith(".jpg") and prefix in file:
        ext = os.path.splitext(file)[1]
        new_name = os.path.basename(file)
        new_name = new_name.replace(prefix + " ", "")
        new_name = new_name[:19] + '-' + new_name[-11:-8] + ext

        return file, os.path.join(outdir, new_name)


def rename_galaxy(file, outdir):
    # ex)Screenshot_20210301-210417.jpg
    if file.endswith(".jpg") or file.endswith(".png"):
        ext = os.path.splitext(file)[1]
        new_name = os.path.basename(file)
        new_name = new_name.replace("Screenshot_", "").replace("-", "")

        year = new_name[0:4]
        month = new_name[4:6]
        day = new_name[6:8]
        hh = new_name[9:11]
        mm = new_name[11:13]
        ss = new_name[13:15]

        new_name = '-'.join([year, month, day]) + ' ' + '-'.join([hh, mm, ss, '000']) + ext

        return file, os.path.join(outdir, new_name)


def rename_steam(file, outdir):
    # ex)20201227223410_1.jpg
    if file.endswith(".jpg") or file.endswith(".png"):
        ext = os.path.splitext(file)[1]
        new_name = os.path.basename(file)

        year = new_name[0:4]
        month = new_name[4:6]
        day = new_name[6:8]
        hh = new_name[8:10]
        mm = new_name[10:12]
        ss = new_name[12:14]
        xx = new_name[15:16]

        new_name = '-'.join([year, month, day]) + ' ' + '-'.join([hh, mm, ss, xx+'00']) + ext

        return file, os.path.join(outdir, new_name)


def copy_files(older, newer):
    shutil.copy2(older, newer)
    print(older, newer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the folder containing the images")
    parser.add_argument("outdir", help="output directory")
    parser.add_argument("--type", choices=['1', '2', '3'], 
                        help="rename type..."+ \
                            "1: potplayer / "+ \
                            "2: galaxy / "+ \
                            "3: steam", \
                        required=True)
    parser.add_argument("--prefix", help="prefix of the images")

    args = parser.parse_args()

    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    args.type = int(args.type)

    # make queue
    q = JoinableQueue()
    for f in glob.glob(os.path.join(args.path, '**', '*.*'), recursive=True):
        q.put(f)

    # make worker
    def worker(q):
        while True:
            f = q.get()
            if args.type == 1:
                o, n = rename_potplayer(f, args.prefix, args.outdir)
            elif args.type == 2:
                o, n = rename_galaxy(f, args.outdir)
            elif args.type == 3:
                o, n = rename_steam(f, args.outdir)
            else:
                raise Exception("Invalid type")
            copy_files(o, n)
            q.task_done()
    
    # make processes
    for i in range(cpu_count()):
    # for i in range(1):
        p = Process(target=worker, args=(q,), daemon=True)
        p.start()
    
    # wait for processes to finish
    q.join()
