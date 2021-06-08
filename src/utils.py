import os
import re
import uuid
import logging
from typing import Union, List
from enum import Enum, auto


class UserResponse(Enum):
    """Enum for user's response.

    Yes or No.
    """
    YES = auto()
    NO = auto()

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False

        if self.value == other.value:
            return True

        return False


def setup_logger(name: str) -> logging.Logger:
    """Set up logger.

    Args:
        name (str): name of logger.

    Returns:
        logger (logging.Logger): logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler_format = logging.Formatter(
        '[%(levelname)s]: %(asctime)s - %(name)s: %(message)s'
    )
    handler.setFormatter(handler_format)

    logger.addHandler(handler)
    logger.propagate = False
    return logger


logger = setup_logger(__name__)


def _atoi(text: str) -> Union[int, str]:
    """Convert ascii to integer.

    Args:
        text (str): string.

    Returns:
        Union[int, str]: integer if number, string otherwise.
    """
    return int(text) if text.isdigit() else text


def natural_keys(text: str) -> Union[List[int], List[str]]:
    """Key for natural sorting

    Args:
        text (str): string

    Returns:
        Union[List[int], List[str]]: A list of mixed integer and strings.
    """
    return [_atoi(c) for c in re.split(r'(\d+)', text)]


def show_info(obj: object) -> None:
    """Show info for given paramters.

    Args:
        obj (object): instance
    """
    max_chars = max([len(key) for key in obj.__dict__])
    for key in sorted(obj.__dict__):
        logger.info(f'{key: <{max_chars}} -> {obj.__dict__[key]}')


def gen_random_filename(directory_name: str, extension: str) -> str:
    """Generate random filename in given directory.

    Args:
        directory_name (str): directory name.
        extension (str): extension includes dot.

    Returns:
        path (str): random filename(absolute path).
    """
    path = ''
    while True:
        random_filename = f'{uuid.uuid4().hex}{extension}'
        path = os.path.join(directory_name, random_filename)
        if os.path.exists(path):
            continue
        break

    return path


def append_prefix(targets: Union[str, list[str], tuple[str]], prefix: str) -> tuple[str]:
    """Append prefix to targets.

    Args:
        targets (Union[str, list[str], tuple[str]]): target to add prefix.
        prefix (str): string prefix.

    Returns:
        tuple[str]: tuple of string with prefix added
    """
    if isinstance(targets, str):
        return (prefix + targets,)
    elif isinstance(targets, list) or isinstance(targets, tuple):
        targets_prefix_added = []
        for target in targets:
            targets_prefix_added.append(prefix + target)
        return tuple(targets_prefix_added)


def enumerate_with_step(elements, initial_number=0, step=1):
    """Enumerate with step.

    Args:
        elements (list): Elements.
        initial_number (int, optional): Initial number. Defaults to 0.
        step (int, optional): Step number. Defaults to 1.

    Yields:
        (key, value): Counted number and the value.
    """
    for element in elements:
        yield (initial_number, element)
        initial_number += step


def ask() -> UserResponse:
    """Ask user to select yes or no.

    This will continue forever until keyboard-interrupt occurres or the user inputs "Yes" or "No".

    Returns:
        UserResponse: User's response(Yes or No)
    """
    user_input = ''
    while not re.search(r'^[ynYN].*$', user_input):
        user_input = input('Are you sure to execute?(y/n): ')

    if re.search(r'^[yY].*$', user_input):
        return UserResponse.YES
    else:
        return UserResponse.NO
