import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description = "Specify type mp3 or mp4."
)

parser.add_argument(
    '-e',
    type = str,
    required = True,
    help = "-e(extension) -> mp3 or mp4"
)

args = vars(parser.parse_args())

def delete2(ext):
    directory = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(directory)

    for item in files:
        if item.endswith(ext):
            os.remove(os.path.join(directory, item))

if __name__ == "__main__":
    if args['e'] == "mp3":
        delete2("mp3")
    elif args['e'] == "mp4":
        delete2("mp4")
    else:
        sys.stderr.write(
            "Unrecognized extension argument."
        )

