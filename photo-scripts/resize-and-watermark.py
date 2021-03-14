# Watermark file was created with:
# > convert -size 500x250 xc:none  -pointsize 35 -kerning 1 -gravity center -fill black -annotate 330x330+0+0 "ihsuanwu.com/surf" -fill white -annotate 330x330+2+2  "ihsuanwu.com/surf" watermark.png

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
    photo_files.sort()
    print(f'Found {len(photo_files)} photos in {input_dir}')

    for i, f in enumerate(photo_files):
        input_path = os.path.join(input_dir, f)
        output_path = os.path.join(output_dir, f)
        print(input_path)
        resize_photo(input_path, output_path)
        label = f'{os.path.basename(input_dir)}_{i + 1}'
        label_photo(output_path, label)
        watermark_photo(output_path)


def resize_photo(input_path, output_path):
    cmd = ['convert', input_path, '-resize', '20%', output_path]
    subprocess.run(cmd)


def label_photo(path, label):
    cmd = ['convert', path, '-fill', 'white', '-undercolor', '#00000080', '-gravity', 'SouthWest',
           '-pointsize', '25', '-annotate', '+25+15', label, path]
    subprocess.run(cmd)


def watermark_photo(path):
    cmd = ['composite', '-dissolve', '30%', '-tile', 'watermark.png', path, path]
    subprocess.run(cmd)


main()
