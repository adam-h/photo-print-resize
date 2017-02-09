# Requirements

 - Python (2 or 3)
  - Tested on v2.7 and v3.5
 - Wand (python binding)
  - `pip install Wand` or `pip3 install Wand`
 - Imagick
  - Tested on v6.9.4-8
  - Must be in your path, specifically the `convert` binary

# Usage

Size all images in "test" directory to 4R / 4x6 size (default), outputting
processed files to "processed" directory

    python resize.py --input test --output processed

## Options

 - `--input` Directory to process images from
 - `--output` Directory to put processed images in
 - `--ratio` Decimal ratio, default is "1.5" which is known as 4R or 6x4
  - Calculate this by `largestSide / smallestSide` e.g. `6 / 4 = 1.5`
 - `--color` Color to use for borders, things like "white", "black"
  - Default "white"
  - See [imagick docs](http://php.net/manual/de/imagick.constants.php#imagick.constants.color)
 - `--gravity` Where to place the image in the output.
  - Default "northwest"
  - See [imagick docs](http://php.net/manual/de/imagick.constants.php#imagick.constants.gravity)

Full example:

    python resize.py --input test --output processed --ratio 1.5 --color red --gravity center
