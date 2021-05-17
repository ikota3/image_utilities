from src.utils import append_prefix, enumerate_with_step


def test_append_prefix__string_should_return_tuple_of_one_item_prefix_added():
    targets = 'jpg'
    prefix = '.'
    ret_val = append_prefix(targets, prefix)
    expected_val = ('.jpg',)
    assert ret_val == expected_val
    assert isinstance(expected_val, tuple)


def test_append_prefix__list_should_return_tuple_of_multiple_item_prefix_added():
    targets = ['jpg', 'jpeg', 'png']
    prefix = '.'
    ret_val = append_prefix(targets, prefix)
    expected_val = ('.jpg', '.jpeg', '.png',)
    assert ret_val == expected_val
    assert isinstance(expected_val, tuple)


def test_append_prefix__tuple_should_return_tuple_of_multiple_item_prefix_added():
    targets = ('jpg', 'jpeg', 'png',)
    prefix = '.'
    ret_val = append_prefix(targets, prefix)
    expected_val = ('.jpg', '.jpeg', '.png',)
    assert ret_val == expected_val
    assert isinstance(expected_val, tuple)


def test_enumerate_with_step__starts_from_one_and_step_is_one():
    targets = range(0, 3)
    initial = 1
    step = 1
    expected_val = [
        (1, 0),
        (2, 1),
        (3, 2),
    ]
    ret_val = []
    for key_value in enumerate_with_step(targets, initial, step):
        ret_val.append(key_value)
    assert ret_val == expected_val


def test_enumerate_with_step__starts_from_one_and_step_is_two():
    targets = range(0, 3)
    initial = 1
    step = 2
    expected_val = [
        (1, 0),
        (3, 1),
        (5, 2),
    ]
    ret_val = []
    for key_value in enumerate_with_step(targets, initial, step):
        ret_val.append(key_value)
    assert ret_val == expected_val


def test_enumerate_with_step__starts_from_two_and_step_is_three():
    targets = range(0, 3)
    initial = 2
    step = 3
    expected_val = [
        (2, 0),
        (5, 1),
        (8, 2),
    ]
    ret_val = []
    for key_value in enumerate_with_step(targets, initial, step):
        ret_val.append(key_value)
    assert ret_val == expected_val
