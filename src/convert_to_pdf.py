import os
import fire
import img2pdf
from validator import is_dir, is_extension, is_bool
from typing import Union
from utils import natural_keys, show_info, setup_logger, append_prefix, UserResponse, ask


logger = setup_logger(__name__)


class ImageConverter():
    """Class for convert images to pdf."""

    def __init__(
            self,
            input_dir: str = '',
            output_dir: str = '',
            extensions: Union[str, tuple[str]] = None,
            force_write: bool = False,
            yes: bool = False
    ):
        """Initialize

        Args:
            input_dir (str): Input directory. Defaults to ''.
            output_dir (str): Output directory. Defaults to ''.
            extensions (Union[str, Tuple[str]]): Extensions. Defaults to ('jpg').
            force_write (bool): Flag for overwrite the converted pdf. Defaults to False.
            yes (bool): Flag for asking to execute or not. Defaults to False.
        """
        self.input_dir: str = input_dir
        self.output_dir: str = output_dir
        if not extensions:
            extensions = ('jpg')
        self.extensions: Union[str, tuple[str]] = append_prefix(extensions, '.')
        self.force_write: bool = force_write
        self.yes: bool = yes

    def _input_is_valid(self) -> bool:
        """Validator for input.

        Returns:
            bool: True if is valid, False otherwise.
        """
        is_valid = True

        # Check input_dir
        if not is_dir(self.input_dir):
            logger.error(
                'You must type a valid directory for input directory.'
            )
            is_valid = False

        # Check output_dir
        if not is_dir(self.output_dir):
            logger.error(
                'You must type a valid directory for output directory.'
            )
            is_valid = False

        # Check extensions
        for extension in self.extensions:
            if not is_extension(extension):
                logger.error('You must type at least one extension.')
                is_valid = False

        # Check force_write
        if not is_bool(self.force_write):
            logger.error(
                'You must just type -f flag. No need to type a parameter.'
            )
            is_valid = False

        # Check yes
        if not is_bool(self.yes):
            logger.error(
                'You must just type -y flag. No need to type a parameter.'
            )
            is_valid = False

        return is_valid

    def convert(self):
        """Convert images to pdf.

        Convert images in each directory to pdf.
        It will convert recursively based on the self.input_dir.
        """
        show_info(self)
        if not self._input_is_valid():
            logger.info('Input parameter is not valid. Try again.')
            return

        if not self.yes:
            user_response = ask()
            if user_response == UserResponse.NO:
                logger.info('Abort...')
                return

        logger.info('Start converting images to pdf...')

        for current_dir, dirs, files in os.walk(self.input_dir):
            logger.info(f'Watching {current_dir}.')
            images = []
            for filename in sorted(files, key=natural_keys):
                if filename.endswith(self.extensions):
                    path = os.path.join(current_dir, filename)
                    images.append(path)

            if not images:
                logger.info(
                    f'There are no {", ".join(self.extensions).upper()} files at {current_dir}.'
                )
                continue

            pdf_filename = os.path.join(
                self.output_dir, f'{os.path.basename(current_dir)}.pdf'
            )

            if self.force_write:
                with open(pdf_filename, 'wb') as f:
                    f.write(img2pdf.convert(images))
                logger.info(f'Created {pdf_filename}!')
            else:
                if os.path.exists(pdf_filename):
                    logger.warning(f'{pdf_filename} already exist! SKIP!')
                    continue

                with open(pdf_filename, 'wb') as f:
                    f.write(img2pdf.convert(images))
                logger.info(f'Created {pdf_filename}!')

        logger.info('Abort...')


if __name__ == '__main__':
    fire.Fire(ImageConverter)
