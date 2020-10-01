#!/usr/bin/env python
"""
BEHAVIORS:
    encoding
        * expects a message file
        * converts the contents of a file into an image
    decoding
        * expects a image file
        * converts the image back into text
"""
import os.path
import argparse

from .decode import decode
from .encode import encode

__author__ = "Peikai Tan"

parser = argparse.ArgumentParser()

valid_opt_behaviors = {
    'encode': ['infile', 'messagefile'],
    'decode': ['infile', 'outfile'],
}

parser.add_argument('behavior', type=str, help='interaction modes: {0}'.format(
    valid_opt_behaviors.keys()))
parser.add_argument('-i', '--infile', type=str, help='path to input file')
parser.add_argument('-o', '--outfile', type=str,
                    help='path to write output file')
opts = parser.parse_args()


def check_file_exists(filename):
    if not os.path.exists(filename):
        parser.error('The file "{0}" could not be found.'.format(filename))


if opts.behavior == 'decode':
    check_file_exists(opts.infile)
    decode(opts.infile, opts.outfile)
elif opts.behavior == 'encode':
    check_file_exists(opts.infile)
    encode(opts.infile, opts.outfile)
