#!/usr/bin/env python
# main.py -- mainly copied from https://github.com/dragonGR/PyWEBP2JPG

import sys
import os.path
from PIL import Image
import converter

OUT_FMTS = {
    "jpeg": (".jpg", ".jpeg"),
}

def main():
    """ Run script directly """
    runner(sys.argv[1:])

def runner(args):
    """ Example:
    input_image = 'sample.webp'
    output_image = 'sample.jpg'
    convert_webp_to_jpg(input_image, output_image)
    """
    param = args
    if not param:
        return None
    for fname in param:
        outer, ext = os.path.splitext(fname)
        if not ext:
            print("No extension?", fname)
            continue
        if not outer:
            continue
        if ext.lower() in OUT_FMTS["jpeg"]:
            print("Ignoring:", fname)
            continue
        outname = outer + ".jpg"
        print(f"Calling: convert_webp_to_jpg({repr(fname)}, {repr(outname)})")
        code, msg = converter.convert_webp_to_jpg(fname, outname)
        if msg:
            print(msg)
            return code
    return 0

if __name__ == "__main__":
    main()
