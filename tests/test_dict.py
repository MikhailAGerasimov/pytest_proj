from utils import dict
import pytest

def test_get_val():
    assert dict.get_val({}, 'vsc') == 'git'
    assert dict.get_val({}, 'vsc', 'mamba') == 'mamba'
    assert dict.get_val({'one':'mercurial'}, 'one') == 'mercurial'
    assert dict.get_val({'two': 'mercurial'}, 'one') == 'git'