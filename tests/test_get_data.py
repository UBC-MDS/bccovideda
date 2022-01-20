from bccovideda import bccovideda
from bccovideda.bccovideda import get_data

import pandas as pd
import os
from datetime import timedelta


def test_check_colnames():
    """Test that column header names of pd.DataFrame constructed 
    from downloaded csv file."""
    case_df_sample = pd.read_csv("tests/case_data_sample.csv")
    expected = case_df_sample.columns.values.tolist()
    actual = get_data().columns.values.tolist()
    assert actual == expected, "Error: Column headers of downloaded data do not match those of sample case data!"


def test_check_dtypes():
    """"Test that cases_df column dtypes are as expected."""
    case_df_sample = pd.read_csv(
        "tests/case_data_sample.csv", parse_dates=["Reported_Date"])
    expected = case_df_sample.dtypes
    actual = get_data().dtypes
    assert len(actual) == len(expected) and sorted(
        actual) == sorted(expected), "Error: Column dtypes of downloaded data do not match those of sample case data!"


def test_recent_data():
    """"Test that most recent data is not from 7 or more days ago."""
    expect = pd.to_datetime("now") - timedelta(days=7)
    actual = get_data()["Reported_Date"].max()
    assert actual > expect, "Error: Most recent data is from 7 or more days ago!"
