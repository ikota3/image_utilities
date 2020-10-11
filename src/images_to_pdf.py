import os
import fire
import img2pdf
from PIL import Image


class PDFConverter(object):
    """Convert images to pdf class."""

    def __init__(
            self,
            input_dir: str = "",
            output_dir: str = "",
            extensions: (str) = None,
            force_write: bool = False
    ):
        self.input_dir: str = input_dir
        self.output_dir: str = output_dir
        if not extensions:
            extensions = ('.jpg')
        self.extensions: (str) = tuple(extensions)
        self.force_write: bool = bool(force_write)

    def _input_is_valid(self) -> bool:
        is_valid = True
        if not os.path.isdir(self.input_dir):
            is_valid = False
            print('[ERROR] You must type a valid directory for input directory.')

        if not os.path.isdir(self.output_dir):
            is_valid = False
            print('[ERROR] You must type a valid directory for output directory.')

        return is_valid

    def convert(self):
        if not self._input_is_valid():
            return

        for current_dir, dirs, files in os.walk(self.input_dir):
            images = []
            for filename in sorted(files):
                if filename.endswith(self.extensions):
                    path = os.path.join(current_dir, filename)
                    images.append(path)

            pdf_filename = os.path.join(
                self.output_dir, f'{os.path.basename(current_dir)}.pdf'
            )

            if self.force_write:
                if images:
                    with open(pdf_filename, 'wb') as f:
                        f.write(img2pdf.convert(images))
                    print(f'[INFO] Created {pdf_filename}!')
            else:
                if os.path.exists(pdf_filename):
                    print(f"[ERROR] {pdf_filename} already exist!")
                    continue

                if images:
                    with open(pdf_filename, 'wb') as f:
                        f.write(img2pdf.convert(images))
                    print(f'[INFO] Created {pdf_filename}!')


if __name__ == '__main__':
    fire.Fire(PDFConverter)
