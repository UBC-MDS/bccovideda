import pytest
import pandas as pd
import numpy as np
from bccovideda.show_summary_stat import show_summary_stat
from bccovideda.get_data import get_data


def read_sample_data():
    df = pd.read_csv("tests/case_data_sample.csv")
    return df


def test_show_summary_stat():
    '''
     Testing the expected output of the function show_summary_stat(startDate, endDate, df)
     with the sample data
     Test cases:
     1. Check None is returned if no matching data in the specified date range
     2. Check return type be a panda dataframe
     3. Check the number of rows in return dataframe 
     4. Check the number of columns in return dataframe 
     5. Check the expected value in the sample dataframe

    '''

    df = get_data()
    # no reported case on 2020-01-30
    df_summary = show_summary_stat("2020-01-30", "2020-01-30")
    assert (df_summary is None), "Should return None if no matching data found"

    df_summary = show_summary_stat("2020-01-29", "2020-03-31")
    # test return type of normal case
    assert isinstance(
        df_summary, pd.DataFrame), "Should return panda.DataFrame"
    assert len(df_summary) == 1, "Should return only one row"
    assert df_summary.size == 15, "Should return 15 columns"

    # test return value of sample data
    assert type(df_summary.loc[0, "total_cases_count"]
                ) == np.int64, "Total count should be integer"
    assert type(df_summary.loc[0, "max_daily_cases_count"]
                ) == np.int64, "Max daily count should be integer"
    assert type(df_summary.loc[0, "min_daily_cases_count"]
                ) == np.int64, "Min dailycount should be integer"
    assert type(df_summary.loc[0, "max_age_group_count"]
                ) == np.int64, "Max age group count should be integer"
    assert type(df_summary.loc[0, "min_age_group_count"]
                ) == np.int64, "Min age group count should be integer"
    assert type(df_summary.loc[0, "max_region_count"]
                ) == np.int64, "Max region count should be integer"
    assert type(df_summary.loc[0, "min_region_count"]
                ) == np.int64, "Min count should be integer"
    assert type(df_summary.loc[0, "latest_date"]
                ) == pd.Timestamp, "Latest date should be pandas Timestamp"
    assert type(df_summary.loc[0, "max_date"]
                ) == pd.Timestamp, "Maximum date should be pandas Timestamp"
    assert type(df_summary.loc[0, "min_date"]
                ) == pd.Timestamp, "Minimum date should be pandas Timestamp"
    assert type(df_summary.loc[0, "max_age_group"]
                ) == str, "Maximum Age Group date should be string"
    assert type(df_summary.loc[0, "min_age_group"]
                ) == str, "Minimum Age Group date should be string"
    assert type(df_summary.loc[0, "max_region"]
                ) == str, "Maximum Region date should be string"
    assert type(df_summary.loc[0, "min_region"]
                ) == str, "Minimum Region date should be string"


def test_show_summary_stat_input():
    '''
     Testing the input parameters of the function show_summary_stat(startDate, endDate)
     Test cases:
     1. startDate is of invalid type
     2. endDate is of invalid type
     3. startDate is of invalid date value
     4. endDate is of invalid date value
     5. endDate is earlier than startDate
     6. startDate is ealier than possible date, '2020-01-29'
     7. endDate is later than today
     '''

    # test input TypeError
    with pytest.raises(TypeError):
        show_summary_stat("2022-01-18", "2022-01-18", 123)
    with pytest.raises(TypeError):
        show_summary_stat(123, "2022-01-12")
    with pytest.raises(TypeError):
        show_summary_stat("2022-01-12", 123)

    # test input ValueError
    with pytest.raises(ValueError):
        show_summary_stat("abcd-01-18", "2022-01-12")
    with pytest.raises(ValueError):
        show_summary_stat("abcd-01-18", "abcd-01-12")
    with pytest.raises(ValueError):
        show_summary_stat("2022-01-18", "2022-01-12")
    with pytest.raises(ValueError):
        show_summary_stat("2020-01-18", "2022-01-12")
    with pytest.raises(ValueError):
        show_summary_stat("2020-01-18", "2999-01-12")
