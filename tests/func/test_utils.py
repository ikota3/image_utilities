from src.utils import append_prefix


def test_append_prefix__string_should_return_tuple_of_one_item_prefix_added():
    targets = 'jpg'
    prefix = '.'
    ret_val = append_prefix(targets, prefix)
    expected = ('.jpg',)
    assert ret_val == expected
    assert isinstance(expected, tuple)


def test_append_prefix__list_should_return_tuple_of_multiple_item_prefix_added():
    targets = ['jpg', 'jpeg', 'png']
    prefix = '.'
    ret_val = append_prefix(targets, prefix)
    expected = ('.jpg', '.jpeg', '.png',)
    assert ret_val == expected
    assert isinstance(expected, tuple)


def test_append_prefix__tuple_should_return_tuple_of_multiple_item_prefix_added():
    targets = ('jpg', 'jpeg', 'png',)
    prefix = '.'
    ret_val = append_prefix(targets, prefix)
    expected = ('.jpg', '.jpeg', '.png',)
    assert ret_val == expected
    assert isinstance(expected, tuple)
