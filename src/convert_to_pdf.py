import re
import os
import fire
import json
import img2pdf
from typing import Union, Tuple
from PIL import Image
from utils import natural_keys, show_info


class PDFConverter(object):
    """Class for convert images to pdf."""

    def __init__(
            self,
            input_dir: str = "",
            output_dir: str = "",
            extensions: Union[str, Tuple[str]] = None,
            force_write: bool = False,
            yes: bool = False
    ):
        """Initialize

        Args:
            input_dir (str): Input directory. Defaults to "".
            output_dir (str): Output directory. Defaults to "".
            extensions (Union[str, Tuple[str]]): Extensions. Defaults to None.
            force_write (bool): Flag for overwrite the converted pdf. Defaults to False.
            yes (bool): Flag for asking to execute or not. Defaults to False.
        """
        self.input_dir: str = input_dir
        self.output_dir: str = output_dir
        if not extensions:
            extensions = ('jpg', 'png')
        self.extensions: Tuple[str] = extensions
        self.force_write: bool = force_write
        self.yes: bool = yes

    def _input_is_valid(self) -> bool:
        """Validator for input.

        Returns:
            bool: True if is valid, False otherwise.
        """
        is_valid = True

        # Check input_dir
        if not isinstance(self.input_dir, str) or \
                not os.path.isdir(self.input_dir):
            print('[ERROR] You must type a valid directory for input directory.')
            is_valid = False

        # Check output_dir
        if not isinstance(self.output_dir, str) or \
                not os.path.isdir(self.output_dir):
            print('[ERROR] You must type a valid directory for output directory.')
            is_valid = False

        # Check extensions
        if not isinstance(self.extensions, tuple) and \
                not isinstance(self.extensions, str):
            print('[ERROR] You must type at least one extension.')
            is_valid = False

        # Check force_write
        if not isinstance(self.force_write, bool):
            print('[ERROR] You must just type -f flag. No need to type a parameter.')
            is_valid = False

        # Check yes
        if not isinstance(self.yes, bool):
            print('[ERROR] You must just type -y flag. No need to type a parameter.')
            is_valid = False

        return is_valid

    def convert(self):
        """Convert images to pdf.

        Convert images in each directory to pdf.
        It will convert recursively based on the self.target_dir.
        """
        print('#---PROCESS START.---#')
        show_info(self)
        if not self._input_is_valid():
            print('#---ERROR OCCURRED. PROCESS END.---#')
            return

        if not self.yes:
            user_input = ""
            while not re.search("^[yYnN].*$", user_input):
                user_input = input("Are you sure to execute?(y/n): ")

            if re.search("^[nN].*$", user_input):
                print("Abort...")
                print('#---PROCESS END.---#')
                return

        # Append "." to prefix for extensions
        extensions: Union[str | Tuple[str]] = None
        if isinstance(self.extensions, tuple):
            extensions = []
            for extension in self.extensions:
                extensions.append(f'.{extension}')
            extensions = tuple(extensions)
        elif isinstance(self.extensions, str):
            extensions = tuple([f'.{self.extensions}'])

        for current_dir, dirs, files in os.walk(self.input_dir):
            print(f'[INFO] Watching {current_dir}.')
            images = []
            for filename in sorted(files, key=natural_keys):
                if filename.endswith(extensions):
                    path = os.path.join(current_dir, filename)
                    images.append(path)

            if not images:
                print(
                    f'[INFO] There are no {", ".join(extensions).upper()} files at {current_dir}.'
                )
                continue

            pdf_filename = os.path.join(
                self.output_dir, f'{os.path.basename(current_dir)}.pdf'
            )

            if self.force_write:
                with open(pdf_filename, 'wb') as f:
                    f.write(img2pdf.convert(images))
                print(f'[INFO] Created {pdf_filename}!')
            else:
                if os.path.exists(pdf_filename):
                    print(f'[ERROR] {pdf_filename} already exist!')
                    continue

                with open(pdf_filename, 'wb') as f:
                    f.write(img2pdf.convert(images))
                print(f'[INFO] Created {pdf_filename}!')

        print("#---PROCESS END.---#")


if __name__ == '__main__':
    fire.Fire(PDFConverter)
