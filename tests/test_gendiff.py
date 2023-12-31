
from gendiff.parsers import generate_diff
import os
import pytest


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


file_path_json1 = get_fixture_path('file1.json')
file_path_json2 = get_fixture_path('file2.json')
file_path_yaml1 = get_fixture_path('file1.yaml')
file_path_yaml2 = get_fixture_path('file2.yaml')
result_stylish = read(get_fixture_path('result_stylish'))
result_plain = read(get_fixture_path('result_plain'))
result_json = read(get_fixture_path('result_json'))


formats = [
    (file_path_json1, file_path_json2, 'stylish', result_stylish),
    (file_path_yaml1, file_path_yaml2, 'stylish', result_stylish),
    (file_path_json1, file_path_json2, 'plain', result_plain),
    (file_path_yaml1, file_path_yaml2, 'plain', result_plain),
    (file_path_json1, file_path_json2, 'json', result_json),
    (file_path_yaml1, file_path_yaml2, 'json', result_json),
]


@pytest.mark.parametrize('file_path1, file_path2, format, result_format',
                         formats,
                         )
def test_generate_diff(file_path1, file_path2, format, result_format):
    assert generate_diff(file_path1, file_path2, format) == result_format
