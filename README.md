## Text to Image Encoder Decoder (ttied)

TTIED aims to convert text files with compression and encryption into images.  
This improves security while decreasing storage needs, at the cost of processing.

### Example

The text file at *examples/message.txt* was converted to:
![output](https://github.com/catkane-doodles/ttied/blob/master/examples/output.png)

### Encoding and decoding

First, to convert text to image.

`$ python -m ttied.ttied encode -i examples/message.txt -o examples/output.png`

Now, given the encoded image, to recover the message hidden inside it.

`$ python -m bpcs.bpcs decode -i examples/output.png -o examples/message_decoded.txt`

The output, message_decoded.txt, should be the same as message.txt, which means we have recovered our original message.


### Inspiration
This project is largely inspired by Bit Plane Complexity Segmentation Steganography.
