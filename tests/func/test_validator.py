from src.validator import is_dir, is_file, is_extension, is_bool, is_in_range


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


def test_is_file__boolean_should_return_false():
    ret_val = is_file(False)
    expected_val = False
    assert ret_val == expected_val


def test_is_file__directory_should_return_false():
    ret_val = is_file('tests/func/')
    expected_val = False
    assert ret_val == expected_val


def test_is_file__filename_should_return_true():
    ret_val = is_file('tests/func/test_validator.py')
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


def test_is_in_range__string_num_should_return_false():
    target = '3'
    min_num = 1
    max_num = 5
    exclude = False
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected_val = False
    assert ret_val == expected_val


def test_is_in_range__minimum_num_should_return_false_when_exclude_option_is_true():
    target = 1
    min_num = 1
    max_num = 5
    exclude = True
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = False
    assert ret_val == expected


def test_is_in_range__maximum_num_should_return_false_when_exclude_option_is_true():
    target = 5
    min_num = 1
    max_num = 5
    exclude = True
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = False
    assert ret_val == expected


def test_is_in_range__minimum_num_should_return_true_when_exclude_option_is_false():
    target = 1
    min_num = 1
    max_num = 5
    exclude = False
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = True
    assert ret_val == expected


def test_is_in_range__maximum_num_should_return_true_when_exclude_option_is_false():
    target = 5
    min_num = 1
    max_num = 5
    exclude = False
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = True
    assert ret_val == expected


def test_is_in_range__nearest_to_minimum_num_in_range_should_return_true_when_exclude_option_is_true():
    target = 2
    min_num = 1
    max_num = 5
    exclude = True
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = True
    assert ret_val == expected


def test_is_in_range__nearest_to_maximum_num_in_range_should_return_true_when_exclude_option_is_true():
    target = 4
    min_num = 1
    max_num = 5
    exclude = True
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = True
    assert ret_val == expected


def test_is_in_range__nearest_to_minimum_num_in_range_should_return_true_when_exclude_option_is_false():
    target = 2
    min_num = 1
    max_num = 5
    exclude = False
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = True
    assert ret_val == expected


def test_is_in_range__nearest_to_maximum_num_in_range_should_return_true_when_exclude_option_is_false():
    target = 4
    min_num = 1
    max_num = 5
    exclude = False
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = True
    assert ret_val == expected


def test_is_in_range__nearest_to_minimum_num_out_of_range_should_return_false_when_exclude_option_is_true():
    target = 0
    min_num = 1
    max_num = 5
    exclude = True
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = False
    assert ret_val == expected


def test_is_in_range__nearest_to_maximum_num_out_of_range_should_return_false_when_exclude_option_is_true():
    target = 6
    min_num = 1
    max_num = 5
    exclude = True
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = False
    assert ret_val == expected


def test_is_in_range__nearest_to_minimum_num_out_of_range_should_return_false_when_exclude_option_is_false():
    target = 0
    min_num = 1
    max_num = 5
    exclude = False
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = False
    assert ret_val == expected


def test_is_in_range__nearest_to_maximum_num_out_of_range_should_return_false_when_exclude_option_is_false():
    target = 6
    min_num = 1
    max_num = 5
    exclude = False
    ret_val = is_in_range(target, min_num, max_num, exclude)
    expected = False
    assert ret_val == expected
