import re
import os
import fire
from typing import Union, Tuple, List
from sort_key import natural_keys


class ImageRenamer(object):
    def __init__(
            self,
            target_dir: str = "",
            digit: int = 4,
            extensions: Union[str, Tuple[str]] = None
    ):
        self.target_dir: str = target_dir
        self.digit: int = digit
        if not extensions:
            extensions = ('jpg', 'png')
        self.extensions: Tuple[str] = extensions

    def _input_is_valid(self) -> bool:
        is_valid = True

        # Check target_dir
        if not isinstance(self.target_dir, str) or \
                not os.path.isdir(self.target_dir):
            print('[ERROR] You must type a valid directory for target directory.')
            is_valid = False

        # Check digit
        if not isinstance(self.digit, int) or \
                self.digit < 3 or 9 < self.digit:
            print('[ERROR] You must type a number for digit.(Min: 3, Max: 9)')
            is_valid = False

        # Check extensions
        if not isinstance(self.extensions, tuple) and \
                not isinstance(self.extensions, str):
            print('[ERROR] You must type at least one extension.')
            is_valid = False

        return is_valid

    def rename(self):
        print('#---PROCESS START.---#')
        if not self._input_is_valid():
            print('#---ERROR OCCURRED. PROCESS END.---#')
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

        for current_dir, dirs, files in os.walk(self.target_dir):
            print(f'[INFO] Watching {current_dir}.')
            filenames = []
            for filename in sorted(files, key=natural_keys):
                if filename.endswith(extensions):
                    path = os.path.join(current_dir, filename)
                    filenames.append(path)

            if not filenames:
                print(
                    f'[INFO] There are no {", ".join(self.extensions).upper()} files at {current_dir}.'
                )
                continue

            for i, filename in enumerate(sorted(filenames, key=natural_keys)):
                _, extension = os.path.splitext(filename)
                dst_filename = os.path.join(
                    current_dir, f'{i + 1:0{self.digit}}{extension}')
                os.rename(filename, dst_filename)
            print(
                f'[INFO] Renamed {", ".join(self.extensions).upper()} files at {current_dir}.'
            )

        print("#---PROCESS END.---#")


if __name__ == '__main__':
    fire.Fire(ImageRenamer)
