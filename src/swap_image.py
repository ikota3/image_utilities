import re
import os
import fire
import uuid
from typing import Union, Tuple
from utils import show_info, natural_keys, gen_random_filename


class ImageSwap(object):
    def __init__(
        self,
        target_dir: str = "",
        extension: str = "jpg",
        yes: bool = False
    ):
        """Initialize

        Args:
          target_dir (str): Target directory. Defaults to "".
          extension (str): Extension. Defaults to "jpg".
          yes (bool): Flag for asking to execute or not. Defaults to False.
        """
        self.target_dir: str = target_dir
        self.extension: str = extension
        self.yes: bool = yes

    def _input_is_valid(self) -> bool:
        """Validator for input.

        Returns:
            bool: True if is valid, False otherwise.
        """
        is_valid = True

        # Check target_dir
        if not isinstance(self.target_dir, str) or \
                not os.path.isdir(self.target_dir):
            print('[ERROR] You must type a valid directory for target directory.')
            is_valid = False

        # Check extension
        if not isinstance(self.extension, str) or \
                not self.extension:
            print('[ERROR] You must type a extension.')
            is_valid = False

        # Check yes
        if not isinstance(self.yes, bool):
            print('[ERROR] You must just type -y flag. No need to type a parameter.')
            is_valid = False

        return is_valid

    def swap(self):
        """Swap first and second image.

        Swap first and second image in each directory.
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

        # Append "." to prefix for extension
        self.extension = f'.{self.extension}'

        for current_dir, dirs, files in os.walk(self.target_dir):
            print(f'[INFO] Watching {current_dir}.')
            filenames = []
            for filename in files:
                if filename.endswith(self.extension):
                    path = os.path.join(current_dir, filename)
                    filenames.append(path)

            if not filenames:
                print(
                    f'[INFO] There are no {self.extension.upper()} files at {current_dir}'
                )
                continue

            if not 2 < len(filenames):
                print(
                    f'[INFO] There are not enough {self.extension.upper()} files at {current_dir}'
                )
                continue

            filenames.sort(key=natural_keys)
            first_file = filenames[0]
            second_file = filenames[1]
            tmp_file = gen_random_filename(
                os.path.dirname(first_file),
                self.extension
            )
            os.rename(first_file, tmp_file)
            os.rename(second_file, first_file)
            os.rename(tmp_file, second_file)
            print(f'[INFO] Swap {first_file} and {second_file}')

        print("#---PROCESS END.---#")


if __name__ == '__main__':
    fire.Fire(ImageSwap)
