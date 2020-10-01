import numpy as np
from PIL import Image


def decode(infile, outfile):
    """
    Converts image to numpy array.
    First converts images into a numpy array of RGB values
    Does not return any value
    """
    # Loading initial values from image
    arr = np.array(Image.open(
        infile).convert('RGB'),)

    arr = arr.reshape(-1)
    bits = arr[arr != 0]

    string = ''.join([chr(b) for b in bits])

    with open(outfile, 'w') as f:
        f.write(string)


if __name__ == "__main__":
    infile = "output.png"
    outfile = "output.txt"
    decode(infile, outfile)
