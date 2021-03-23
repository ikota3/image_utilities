import re
import os
import fire
from alive_progress import alive_bar
from typing import Union
from validator import is_dir, is_extension, is_bool, is_digit
from utils import natural_keys, show_info, setup_logger, append_prefix


logger = setup_logger(__name__)


class ImageRenamer():
    """Class for renaming images."""

    def __init__(
            self,
            target_dir: str = '',
            digit: int = 4,
            extensions: Union[str, tuple[str]] = None,
            yes: bool = False
    ):
        """Initialize

        Args:
            target_dir (str): Target directory. Defaults to ''.
            digit (int): Number of digits for renaming. Defaults to 4.
            extensions (Union[str, Tuple[str]]): Extensions. Defaults to None.
            yes (bool): Flag for asking to execute or not. Defaults to False.
        """
        self.target_dir: str = target_dir
        self.digit: int = digit
        if not extensions:
            extensions = ('jpg')
        self.extensions: Union[str, tuple[str]] = append_prefix(extensions, ".")
        self.yes: bool = yes

    def _input_is_valid(self) -> bool:
        """Validator for input.

        Returns:
            bool: True if is valid, False otherwise.
        """
        is_valid = True

        # Check target_dir
        if not is_dir(self.target_dir):
            logger.error(
                'You must type a valid directory for target directory.'
            )
            is_valid = False

        # Check digit
        if not is_digit(self.digit, 3, 9, False):
            logger.error('You must type a number for digit.(Min: 3, Max: 9)')
            is_valid = False

        # Check extensions
        for extension in self.extensions:
            if not is_extension(extension):
                logger.error('You must type at least one extension.')
                is_valid = False

        # Check yes
        if not is_bool(self.yes):
            logger.error(
                'You must just type -y flag. No need to type a parameter.'
            )
            is_valid = False

        return is_valid

    def rename(self):
        """Rename to sequential number.

        Rename the filename in each directory to sequential number.
        It will rename recursively based on the self.target_dir.
        """
        show_info(self)
        if not self._input_is_valid():
            logger.info('Input parameter is not valid. Try again.')
            return

        if not self.yes:
            user_input = ''
            while not re.search('^[yYnN].*$', user_input):
                user_input = input('Are you sure to execute?(y/n): ')

            logger.info(f'User input: {user_input}')
            if re.search('^[nN].*$', user_input):
                logger.info('Abort...')
                return

        logger.info('Start renaming images to sequential number...')

        for current_dir, dirs, files in os.walk(self.target_dir):
            logger.info(f'Watching {current_dir}.')
            filenames = []
            for filename in sorted(files):
                if filename.endswith(self.extensions):
                    path = os.path.join(current_dir, filename)
                    filenames.append(path)

            if not filenames:
                logger.info(
                    f'There are no {", ".join(self.extensions).upper()} files at {current_dir}.'
                )
                continue

            with alive_bar(len(filenames), bar='filling') as bar:
                for i, filename in enumerate(sorted(filenames, key=natural_keys)):
                    _, extension = os.path.splitext(filename)
                    dst_filename = os.path.join(
                        current_dir, f'{i + 1:0{self.digit}}{extension}')
                    os.rename(filename, dst_filename)
                    bar()

            logger.info(
                f'Renamed {", ".join(self.extensions).upper()} files at {current_dir}.'
            )

        logger.info('Abort...')


if __name__ == '__main__':
    fire.Fire(ImageRenamer)
