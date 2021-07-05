# This script relies on the `convert` and `composite` commands from ImageMagick:
#   https://imagemagick.org/script/download.php#macosx
# Watermark file was created with:
# > convert -size 500x250 xc:none  -pointsize 35 -kerning 1 -gravity center -fill black -annotate 330x330+0+0 "ihsuanwu.com/surf" -fill white -annotate 330x330+2+2  "ihsuanwu.com/surf" watermark.png

import argparse
import os
import subprocess
import sys


def check_version():
    ver = sys.version_info
    if ver.major < 3 or ver.minor < 9:
        sys.exit('Requires Python >= 3.9')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    return parser.parse_args()


def main():
    check_version()
    args = parse_args()
    input_dir = args.input_dir

    photo_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')]
    photo_files.sort()
    print(f'Found {len(photo_files)} photos in {input_dir}')

    resize_photos(photo_files, input_dir, preview=False)
    resize_photos(photo_files, input_dir, preview=True)


def resize_photos(photo_files, input_dir, preview):
    folder_ext = '_preview' if preview else '_watermark'
    output_dir = input_dir + folder_ext
    os.makedirs(output_dir, exist_ok=True)
    print(f'Generating photos into {output_dir}')

    for i, f in enumerate(photo_files):
        input_path = os.path.join(input_dir, f)
        output_path = os.path.join(output_dir, f)
        print(input_path)
        resize_photo(input_path, output_path, preview)
        if not preview:
            label = f'{os.path.basename(input_dir)}_{i + 1}'
            label_photo(output_path, label)
            watermark_photo(output_path)


def resize_photo(input_path, output_path, preview):
    scale_perc = '12%' if preview else '20%'
    cmd = ['convert', input_path, '-resize', scale_perc, output_path]
    subprocess.run(cmd)


def label_photo(path, label):
    cmd = ['convert', path, '-fill', 'white', '-undercolor', '#00000080', '-gravity', 'SouthWest',
           '-pointsize', '25', '-annotate', '+25+15', label, path]
    subprocess.run(cmd)


def watermark_photo(path):
    cmd = ['composite', '-dissolve', '30%', '-tile', 'watermark.png', path, path]
    subprocess.run(cmd)


main()
