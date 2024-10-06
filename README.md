# WEBP to JPG Converter

1. [(here)](https://github.com/serrasqueiro/WEBP2JPG) _Python_ WEBP2JPG

These Python scripts allows you to convert WebP image files to JPG format using the Pillow library.

## What This Code Does ?

This code provides a convenient solution to convert multiple WebP files to the JPG format effortlessly. It ensures that the original image quality is maintained during the conversion process.

## Usage

1. Run the script to convert WEBP files to JPG format
   + `./main.py` accepts multiple arguments, one per input file.

## Now just fun
![Penguin taking a bath](https://github.com/serrasqueiro/WEBP2JPG/blob/my/penguin/penguin_taking_a_bath.jpg)

## PIL Library
Python **PIL** library allows image manipulation easily.
- Consider the following sample ...
```
from PIL import Image
img = Image.open("penguin_taking_a_bath.webp")
assert img.format.lower() == "webp", img.format
img.save("penguin.jpg", 'JPEG', quality=quality)
```

## Features

- Converts multiple WEBP files to JPG format.
- Preserves the original image quality.
- Supports batch conversion.
- Easy to use and configure.

Feel free to customize the script to suit your specific requirements.
