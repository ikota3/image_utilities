import os
import re
import uuid
import logging
from typing import Union, List


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


def append_prefix(targets: Union[str, list, tuple], prefix: str) -> tuple[str]:
    """Append prefix to targets.

    Args:
        targets (Union[str, list, tuple]): target to add prefix.
        prefix (str): string prifix.

    Returns:
        tuple[str]: tuple of string with prefix added
    """
    if isinstance(targets, str):
        return tuple([prefix + targets])
    elif isinstance(targets, list) or isinstance(targets, tuple):
        ret_val = []
        for target in targets:
            ret_val.append(prefix + target)
        return tuple(ret_val)
