import pytest
import pandas as pd
from bccovideda.show_summary_stat import show_summary_stat

def read_sample_data():
    df = pd.read_csv("tests/case_data_sample.csv")
    return df

def test_show_summary_stat():
    '''
     Testing the expected output of the function show_summary_stat(startDate, endDate)
     Test cases:
     1. Check None is returned if no matching data in the specified date range
     2. Check return type be a panda dataframe
     3. Check the number of rows in return dataframe 
     4. Check the number of columns in return dataframe 
     5. Check the expected value in the sample dataframe
    '''


    df_sample = read_sample_data()
    df_summary = show_summary_stat(df_sample, "2022-01-01", "2022-01-13")
    assert (df_summary is None), "Should return None if no matching data found"

    df_summary = show_summary_stat(df_sample, "2020-01-29", "2020-03-31")
    # test return type of normal case
    assert isinstance(df_summary, pd.DataFrame), "Should return panda.DataFrame"
    assert len(df_summary) == 1, "Should return only one row"
    assert df_summary.size == 15, "Should return 15 columns"

    # test return value of sample data
    assert df_summary.loc[0, "total_cases_count"]==100, "Should return 100 for total cases count between 20200129 and 20200331"
    assert df_summary.loc[0, "latest_daily_cases_count"]==16, "Should return 16 for latest_daily_cases_count between 20200129 and 20200331"
    assert df_summary.loc[0, "max_daily_cases_count"]==16, "Should return 16 for max_daily_cases_count between 20200129 and 20200331"
    assert df_summary.loc[0, "min_daily_cases_count"]==1, "Should return 1 for min_daily_cases_count between 20200129 and 20200331"
    assert df_summary.loc[0, "max_age_group_count"]==26, "Should return 26 for max_age_group_count between 20200129 and 20200331"
    assert df_summary.loc[0, "min_age_group_count"]==2, "Should return 2 for min_age_group_count between 20200129 and 20200331"
    assert df_summary.loc[0, "max_region_count"]==62, "Should return 62 for max_region_count between 20200129 and 20200331"
    assert df_summary.loc[0, "min_region_count"]==1, "Should return 1 for min_region_count between 20200129 and 20200331"
    assert df_summary.loc[0, "latest_date"]=="2020-03-13", "Should return '2020-03-13' for latest_date between 20200129 and 20200331"
    assert df_summary.loc[0, "max_date"]=="2020-03-11" or df_summary.loc[0, "max_date"]=="2020-03-13", "Should return either '2020-03-11' or '2020-03-13' for max_date between 20200129 and 20200331"
    assert df_summary.loc[0, "min_date"]=="2020-01-29", "Should return '2020-01-29' for min_date between 20200129 and 20200331"
    assert df_summary.loc[0, "max_age_group"]=="50-59", "Should return '50-59' for max_age_group between 20200129 and 20200331"
    assert df_summary.loc[0, "min_age_group"]=="10-19", "Should return '10-19' for min_age_group between 20200129 and 20200331"
    assert df_summary.loc[0, "max_region"]=="Vancouver Coastal", "Should return 'Vancouver Coastal' for max_region between 20200129 and 20200331"
    assert df_summary.loc[0, "min_region"]=="Interior", "Should return 'Interior' for min_region between 20200129 and 20200331"






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
    df = pd.DataFrame()

    # test input TypeError
    with pytest.raises(TypeError):
        show_summary_stat(123,"2022-01-18", "2022-01-18" )
    with pytest.raises(TypeError):
        show_summary_stat(df, 123, "2022-01-12")
    with pytest.raises(TypeError):
        show_summary_stat(df, "2022-01-12", 123)

    # test input ValueError
    with pytest.raises(ValueError):
        show_summary_stat(df,"abcd-01-18", "2022-01-12")
    with pytest.raises(ValueError):
        show_summary_stat(df,"abcd-01-18", "abcd-01-12")
    with pytest.raises(ValueError):
        show_summary_stat(df,"2022-01-18", "2022-01-12")
    with pytest.raises(ValueError):
        show_summary_stat(df,"2020-01-18", "2022-01-12")
    with pytest.raises(ValueError):
        show_summary_stat(df,"2020-01-18", "2999-01-12")