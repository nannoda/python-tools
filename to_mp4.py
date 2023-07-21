import sys
import argparse
import subprocess
import os

from get_name import get_name
from has_ffmpeg import has_ffmpeg


def simple_conversion(input_file: str, output_file: str) -> bool:
    p = subprocess.run(
        args=[
            "ffmpeg",
            "-i",
            input_file,

            output_file
        ]
    )
    return p.returncode == 0


def fallback_conversion(input_file: str, output_file: str) -> bool:
    p = subprocess.run(
        args=[
            "ffmpeg",
            "-i",
            input_file,
            "-b:v",
            "0",
            "-crf",
            "1",
            "-c:v",
            "libx264",
            output_file
        ]
    )
    return p.returncode == 0


def main():
    if not has_ffmpeg():
        print("You need to have ffmpeg in path.")

    parser = argparse.ArgumentParser(
        prog="to_mp4.py",
        description="Convert a file to mp4"
    )
    parser.add_argument("input", type=str)
    parser.add_argument("output", type=str, nargs="?")

    args = parser.parse_args()

    input_file = args.input

    if not os.path.isfile(input_file):
        print("Input is not a valid file...")
        return

    output_file = args.output or get_name(input_file + ".mp4")

    print(f"input file: {input_file}")
    print(f"output file: {output_file}")

    success = simple_conversion(input_file, output_file)
    if success:
        print("Done!")
        return

    print("simple_conversion failed, trying fallback (information may lost)...")
    success = fallback_conversion(input_file, output_file)

    if success:
        print("Done with fallback.")
        return

    print("Sorry, but there is nothing we can do...")


if __name__ == "__main__":
    main()
