from src.validator import is_dir, is_extension, is_bool


def test_is_dir__boolean_should_return_false():
    ret_val = is_dir(True)
    expected_val = False
    assert ret_val == expected_val


def test_is_dir__filename_should_return_false():
    ret_val = is_dir('tests/func/test_validator.py')
    expected_val = False
    assert ret_val == expected_val


def test_is_dir__directory_should_return_true():
    ret_val = is_dir('tests/func/')
    expected_val = True
    assert ret_val == expected_val


def test_is_extension__boolean_should_return_false():
    ret_val = is_extension(False)
    expected_val = False
    assert ret_val == expected_val


def test_is_extension__without_dot_extension_should_return_false():
    ret_val = is_extension('jpg')
    expected_val = False
    assert ret_val == expected_val


def test_is_extension__dot_only_should_return_false():
    ret_val = is_extension('.')
    expected_val = False
    assert ret_val == expected_val


def test_is_extension__dot_plus_extension_should_return_true():
    ret_val = is_extension('.jpg')
    expected_val = True
    assert ret_val == expected_val


def test_is_bool__string_should_return_false():
    ret_val = is_bool('True')
    expected_val = False
    assert ret_val == expected_val


def test_is_bool__boolean_should_return_true():
    ret_val = is_bool(False)
    expected_val = True
    assert ret_val == expected_val
