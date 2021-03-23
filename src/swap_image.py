import re
import os
import fire
from validator import is_dir, is_extension, is_bool
from utils import show_info, natural_keys, gen_random_filename, setup_logger


logger = setup_logger(__name__)


class ImageSwap():
    """Class for swaping images."""

    def __init__(
        self,
        target_dir: str = '',
        extension: str = '',
        yes: bool = False
    ):
        """Initialize

        Args:
          target_dir (str): Target directory. Defaults to ''.
          extension (str): Extension. Defaults to 'jpg'.
          yes (bool): Flag for asking to execute or not. Defaults to False.
        """
        self.target_dir: str = target_dir
        if extension == '':
            extension = 'jpg'
        self.extension: str = f'.{extension}'
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

        # Check extension
        if not is_extension(self.extension):
            logger.error('You must type a extension.')
            is_valid = False

        # Check yes
        if not is_bool(self.yes):
            logger.error(
                'You must just type -y flag. No need to type a parameter.'
            )
            is_valid = False

        return is_valid

    def swap(self):
        """Swap first and second image.

        Swap first and second image in each directory.
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

        logger.info('Start swaping first image and second image...')

        for current_dir, dirs, files in os.walk(self.target_dir):
            logger.info(f'Watching {current_dir}.')
            filenames = []
            for filename in files:
                if filename.endswith(self.extension):
                    path = os.path.join(current_dir, filename)
                    filenames.append(path)

            if not filenames:
                logger.info(
                    f'There are no {self.extension.upper()} files at {current_dir}'
                )
                continue

            if not 2 < len(filenames):
                logger.info(
                    f'There are not enough {self.extension.upper()} files at {current_dir}'
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
            logger.info(f'Swap {first_file} and {second_file}')

        logger.info('Abort...')


if __name__ == '__main__':
    fire.Fire(ImageSwap)
