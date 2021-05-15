import re
import os


def is_dir(target: str) -> bool:
    """Check target is dir."""
    if not isinstance(target, str):
        return False
    if not os.path.isdir(target):
        return False

    return True


def is_file(target: str) -> bool:
    """Check target is file."""
    if not isinstance(target, str):
        return False
    if not os.path.isfile(target):
        return False

    return True


def is_extension(target: str) -> bool:
    """Check target is extension(.ext)."""
    if not isinstance(target, str):
        return False
    if not re.search(r'^\..+$', target):
        return False

    return True


def is_bool(target: bool) -> bool:
    """Check target is boolean."""
    if not isinstance(target, bool):
        return False

    return True


def is_in_range(target: int, min_num: int, max_num: int, exclude: bool = False) -> bool:
    if not isinstance(target, int):
        return False

    if exclude:
        if min_num < target < max_num:
            return True
    else:
        if min_num <= target <= max_num:
            return True

    return False


def is_positive_number(target: int) -> bool:
    if not isinstance(target, int):
        return False

    if target < 0:
        return False

    return True
