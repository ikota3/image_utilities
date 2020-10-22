import re
from typing import Union, List


def _atoi(text: str) -> Union[int, str]:
    """Convert ascii to integer"""
    return int(text) if text.isdigit() else text


def natural_keys(text: str) -> Union[List[int], List[str]]:
    """Key for natural sorting"""
    return [_atoi(c) for c in re.split(r'(\d+)', text)]
