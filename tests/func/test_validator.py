from src.validator import is_dir, is_extension, is_bool, is_digit


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


def test_is_digit__string_digit_should_return_false():
    target = '3'
    min_digit = 1
    max_digit = 5
    exclude = False
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected_val = False
    assert ret_val == expected_val


def test_is_digit__minimum_digit_should_return_false_when_exclude_option_is_true():
    target = 1
    min_digit = 1
    max_digit = 5
    exclude = True
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = False
    assert ret_val == expected


def test_is_digit__maximum_digit_should_return_false_when_exclude_option_is_true():
    target = 5
    min_digit = 1
    max_digit = 5
    exclude = True
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = False
    assert ret_val == expected


def test_is_digit__minimum_digit_should_return_true_when_exclude_option_is_false():
    target = 1
    min_digit = 1
    max_digit = 5
    exclude = False
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = True
    assert ret_val == expected


def test_is_digit__maximum_digit_should_return_true_when_exclude_option_is_false():
    target = 5
    min_digit = 1
    max_digit = 5
    exclude = False
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = True
    assert ret_val == expected


def test_is_digit__nearest_to_minimum_digit_in_range_should_return_true_when_exclude_option_is_true():
    target = 2
    min_digit = 1
    max_digit = 5
    exclude = True
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = True
    assert ret_val == expected


def test_is_digit__nearest_to_maximum_digit_in_range_should_return_true_when_exclude_option_is_true():
    target = 4
    min_digit = 1
    max_digit = 5
    exclude = True
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = True
    assert ret_val == expected


def test_is_digit__nearest_to_minimum_digit_in_range_should_return_true_when_exclude_option_is_false():
    target = 2
    min_digit = 1
    max_digit = 5
    exclude = False
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = True
    assert ret_val == expected


def test_is_digit__nearest_to_maximum_digit_in_range_should_return_true_when_exclude_option_is_false():
    target = 4
    min_digit = 1
    max_digit = 5
    exclude = False
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = True
    assert ret_val == expected


def test_is_digit__nearest_to_minimum_digit_out_of_range_should_return_false_when_exclude_option_is_true():
    target = 0
    min_digit = 1
    max_digit = 5
    exclude = True
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = False
    assert ret_val == expected


def test_is_digit__nearest_to_maximum_digit_out_of_range_should_return_false_when_exclude_option_is_true():
    target = 6
    min_digit = 1
    max_digit = 5
    exclude = True
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = False
    assert ret_val == expected


def test_is_digit__nearest_to_minimum_digit_out_of_range_should_return_false_when_exclude_option_is_false():
    target = 0
    min_digit = 1
    max_digit = 5
    exclude = False
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = False
    assert ret_val == expected


def test_is_digit__nearest_to_maximum_digit_out_of_range_should_return_false_when_exclude_option_is_false():
    target = 6
    min_digit = 1
    max_digit = 5
    exclude = False
    ret_val = is_digit(target, min_digit, max_digit, exclude)
    expected = False
    assert ret_val == expected
