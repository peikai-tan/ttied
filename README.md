## Text to Image Encoder Decoder (ttied)

TTIED aims to encode text files into images.

### Features
* Compression (to be refined)
* Encryption (to be implemented)

### Example

The text file at *examples/message.txt* was encoded to:
![output](https://github.com/catkane-doodles/ttied/blob/master/examples/output.png)


### Encoding and decoding

First, to encode text into an image.

`$ python -m ttied.ttied encode -i examples/message.txt -o examples/output.png`

Now, given the encoded image, to recover the message hidden inside it.

`$ python -m ttied.ttied decode -i examples/output.png -o examples/message_decoded.txt`

The output, message_decoded.txt, should be the same as message.txt, which means we have recovered our original message.


### Inspiration
This project is largely inspired by Bit Plane Complexity Segmentation Steganography.
