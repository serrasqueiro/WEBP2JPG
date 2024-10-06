#!/bin/sh
#
# Do first:
#	git checkout my/penguin

echo "Converting penguin_taking_a_bath.webp into a JPG"
python main.py *.webp
