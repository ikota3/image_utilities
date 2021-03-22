from src.validator import is_dir, is_extension, is_bool


def test_is_dir_boolean_value_return_false():
    ret_val = is_dir(True)
    expected_val = False
    assert ret_val == expected_val


def test_is_dir_filename_return_false():
    ret_val = is_dir('tests/func/test_validator.py')
    expected_val = False
    assert ret_val == expected_val


def test_is_dir_directory_return_true():
    ret_val = is_dir('tests/func/')
    expected_val = True
    assert ret_val == expected_val


def test_is_extension_boolean_value_return_false():
    ret_val = is_extension(False)
    expected_val = False
    assert ret_val == expected_val


def test_is_extension_without_dot_extension_return_false():
    ret_val = is_extension('jpg')
    expected_val = False
    assert ret_val == expected_val


def test_is_extension_dot_only_return_false():
    ret_val = is_extension('.')
    expected_val = False
    assert ret_val == expected_val


def test_is_extension_dot_plus_extension_return_true():
    ret_val = is_extension('.jpg')
    expected_val = True
    assert ret_val == expected_val


def test_is_bool_string_return_false():
    ret_val = is_bool('True')
    expected_val = False
    assert ret_val == expected_val


def test_is_bool_boolean_return_true():
    ret_val = is_bool(False)
    expected_val = True
    assert ret_val == expected_val
