# Watermark file was created with:
# > convert -size 500x250 xc:none  -pointsize 35 -kerning 1 -gravity center -fill black -annotate 330x330+0+0 "ihsuanwu.com" -fill white -annotate 330x330+2+2  "ihsuanwu.com" watermark.png

import argparse
import os
import subprocess


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    return parser.parse_args()


def main():
    args = parse_args()
    input_dir = args.input_dir
    output_dir = input_dir + '_resized'
    os.makedirs(output_dir, exist_ok=True)

    photo_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')]
    print(f'Found {len(photo_files)} in {input_dir}')

    for f in photo_files:
        input_path = os.path.join(input_dir, f)
        output_path = os.path.join(output_dir, f)
        print(input_path)
        resize(input_path, output_path)
        watermark(output_path)


def resize(input_path, output_path):
    cmd = ['convert', input_path, '-resize', '20%', output_path]
    subprocess.run(cmd)


def watermark(path):
    cmd = ['composite', '-dissolve', '30%', '-tile', 'watermark.png', path, path]
    subprocess.run(cmd)


main()
