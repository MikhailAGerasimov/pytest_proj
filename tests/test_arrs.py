from utils import arrs
import pytest


@pytest.mark.parametrize('array, element_in_array, default_name, expected', [
    ([1, 2, 3], 1, "test", 2),
    (['a', 'b', 'c', 'd', 'e'], 4, "test", 'e'),
    ([1, 2, 3], -1, "test", "test"),

])
def test_get(array, element_in_array, default_name, expected):
    assert arrs.get(array, element_in_array, default_name) == expected


def test_get_empty_array():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_get_index_out_of_range():
    with pytest.raises(IndexError):
        arrs.get([1, 2, 3, 4], 7, "test")


@pytest.mark.parametrize('array, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([1, 2, 3, 4], -3, -1, [2, 3]),
    ([1, 2, 3, 4], -3, None, [2, 3, 4]),
    ([1, 2, 3, 4], 3, 1, []),
    ([1, 2, 3, 4], 0, 3, [1, 2, 3]),
    ([1, 2, 3, 4], -5, 3, [1, 2, 3]),
    ([], 0, 1, []),

])

def test_slice(array, start, end, expected):
    assert arrs.my_slice(array, start, end) == expected


def test_slice_with_one_parameter():
    assert arrs.my_slice([1, 2, 2, 5]) == [1, 2, 2, 5]


def test_slice_index_out_of_range():
    with pytest.raises(IndexError):
        arrs.get([1, 2, 3, 4], 5, 7)


def test_slice_empty_array():
    with pytest.raises(IndexError):
        arrs.get([], 5, 7)
