import os
import re
import uuid
from typing import Union, List


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
        print(f'{key: <{max_chars}} -> {obj.__dict__[key]}')


def gen_random_filename(directory_name: str, extension: str) -> str:
    """Generate random filename in given directory.

    Args:
        directory_name (str): directory name.
        extension (str): extension includes dot.
    """
    path = ""
    while True:
        random_filename = f'{uuid.uuid4().hex}{extension}'
        path = os.path.join(directory_name, random_filename)
        if os.path.exists(path):
            continue
        break

    return path
