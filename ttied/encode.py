import numpy as np
from PIL import Image


def encode(infile, outfile):
    arr = np.array([ord(s) for s in open(infile).read()])

    bitPlanes = 3
    arrLen = len(arr)

    # calculating how many pixels are needed
    # squared cos each grid is a square
    rowSize = int(np.ceil(np.sqrt(arrLen/bitPlanes)))
    pixelsNeeded = np.square(rowSize)

    # fill up arr with zeros until same length as final image
    while (len(arr)/bitPlanes) % 3 != 0:
        arr = np.append(arr, [0], 0)

    arr = np.pad(arr.reshape(-1), (0, int(
        pixelsNeeded - len(arr)/bitPlanes) * bitPlanes), 'constant')

    # reshaping to correct shape
    arr = arr.reshape((rowSize, rowSize, bitPlanes))

    # Saving image
    Image.fromarray(np.uint8(arr)).save(outfile)


if __name__ == "__main__":
    infile = "./examples/message.txt"
    outfile = "./examples/output.png"
    encode(infile, outfile)
