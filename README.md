# Requirements

- Python 3 & pipx
- Imagick
  - Tested on v7
  - Must be in your path, specifically the `magick` binary

# Usage

Size all images in "test" directory to 4R / 4x6 size (default), outputting
processed files to "processed" directory

    pipx run resize.py --input test --output processed

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

    pipx run resize.py --input test --output processed --ratio 1.5 --color red --gravity center
