import re
from typing import Union, List


def atoi(text: str) -> Union[int, str]:
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
    return [atoi(c) for c in re.split(r'(\d+)', text)]
