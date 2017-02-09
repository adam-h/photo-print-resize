#!/bin/env python3

from __future__ import print_function
import os
import glob
import argparse
from wand.image import Image
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Input directory', required=True)
parser.add_argument('--output', help='Output directory', required=True)
parser.add_argument('--ratio', help='Image ratio', default=1.5)
parser.add_argument('--gravity', help='Gravity for the image (borders will be opposite)', default='northwest')
parser.add_argument('--color', help='Color for borders', default='white')
args = parser.parse_args()

extensions = ('png', 'gif', 'jpg', 'jpeg')
image_paths = []
ratio = int(100 * args.ratio)

for extension in extensions:
    image_paths.extend(glob.glob(os.path.join(args.input, '*.' + extension)))

for input_path in image_paths:
    with Image(filename=input_path) as img:
        output_path = os.path.join(args.output, os.path.basename(input_path))
        w = img.width
        h = img.height
        ratio = int(100 * args.ratio)

        if w < h:
            extent = str(ratio) + '%x100%'
        else:
            extent = '100%x' + str(ratio) + '%'

        call(['convert', input_path, '-gravity', args.gravity, '-background', args.color, '-extent', extent, output_path])
