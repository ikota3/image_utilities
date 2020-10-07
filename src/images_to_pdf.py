import os
import fire
from PIL import Image


class PDFConverter(object):
    """Convert images to pdf class."""

    def __init__(self, input_dir=None, output_dir=None):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def convert(self):
        pass


if __name__ == '__main__':
    fire.Fire(PDFConverter)
