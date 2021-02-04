import pytest
import pandas as pd

from module import apartments


def test_if_returns_correct_type():
    # CHECK IF SUM WORKS
    new_df = apartments.scrapper(1)
    assert type(new_df) == pd.DataFrame


def test_rows_count():
    # CHECK IF SUM WORKS
    new_df = apartments.scrapper(20)
    assert new_df.shape[0] == 20


def test_if_bad_argument_passed():
    # CHECK IF SUM WORKS
    try:
        new_df = apartments.scrapper("not_relevant")
    except:
        assert True
