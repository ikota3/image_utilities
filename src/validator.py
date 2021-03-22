import re
import os


def is_dir(target: str):
    """Check target is dir path."""
    if not isinstance(target, str):
        return False
    if not os.path.isdir(target):
        return False

    return True


def is_extension(target: str):
    """Check target is extension(.ext)."""
    if not isinstance(target, str):
        return False
    if not re.search(r'^\..+$', target):
        return False

    return True


def is_bool(target: bool):
    """Check target is boolean."""
    if not isinstance(target, bool):
        return False

    return True
