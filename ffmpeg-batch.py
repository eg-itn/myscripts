import os
import ffmpeg
import sys
import argparse


def check_fps(input_file):
    fps = ffmpeg.probe(input_file)['streams'][0]['avg_frame_rate'].split('/')[0]
    return fps


def ffmpeg_change_format(args):
    input_dir = args.input_dir
    output_dir = args.output_dir
    output_format = args.output_format

    # Check if input directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(input_dir):
        if file.endswith(".mp4"):
            input_file = os.path.join(input_dir, file)

            # create output file name
            if output_format != "mp4":
                output_file = os.path.join(output_dir, file.replace(".mp4", "." + output_format))
            else:
                output_file = os.path.join(output_dir, file)
        
            # run ffmpeg
            try:
                ffmpeg.input(input_file).output(output_file).run()
            except ffmpeg.Error as e:
                print(e.stderr, file=sys.stderr)


def ffmpeg_to_jpg(args):
    input_dir = args.input_dir
    output_dir = args.output_dir

    # Check if input directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file in os.listdir(input_dir):
        if file.endswith(".mp4"):
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(output_dir, os.path.splitext(file)[0])

            # run ffmpeg
            try:
                if args.fps == None:
                    ffmpeg.input(input_file).output(f"{output_file}_%05d.jpg").run()
                else:
                    ffmpeg.input(input_file).filter('fps', fps=args.fps).output(f"{output_file}_%05d.jpg").run()
            except ffmpeg.Error as e:
                print(e.stderr, file=sys.stderr)


def ffmpeg_checkfps(args):
    input_dir = args.input_dir

    for file in os.listdir(input_dir):
        if file.endswith(".mp4"):
            input_file = os.path.join(input_dir, file)
            fps = check_fps(input_file)
            print(f"{input_file} fps: {fps}")

if __name__ == "__main__":

    # Parse arguments
    argparse.ArgumentParser(description="Convert video files")
    parser = argparse.ArgumentParser()
    # Required arguments
    parser.add_argument("input_dir", help="Input directory")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument("-f", "--output_format", help="Output format", default="mp4")  # Default is mp4
    parser.add_argument("--fps", help="input fps", type=float)
    parser.add_argument("--task", help="task", required=True, choices=["change_format", "to_jpg", "checkfps"])
    args = parser.parse_args()

    if args.task == "change_format":
        ffmpeg_change_format(args)
    args = parser.parse_args()

    # Call ffmpeg_batch function
    if args.task == "change_format":
        ffmpeg_change_format(args)
    elif args.task == "to_jpg":
        ffmpeg_to_jpg(args)
    elif args.task == "checkfps":
        ffmpeg_checkfps(args)
    else:
        print("Error: Invalid task")