
import requests
import os
import pandas as pd
import altair as alt


def getData(url="http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv", out_folder="data/raw"):
    """
    Downloads the entire "case details" data set from
    http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv
    and returns it as a pandas data frame.

    Parameters
    ----------
    url : str
        URL to case data download page
    out_folder : str
        Path to folder storing raw data set csv file

    Returns
    -------
    pandas.DataFrame
        Data frame containing entire BC Case Details Data

    Examples
    --------
    >>> getData()
    """

    if not os.path.exists(os.getcwd() + "/" + out_folder):
        os.makedirs(out_folder + "/")

    req = requests.get(url)
    url_content = req.content

    csv_file = open("data/raw/case_data.csv", "wb")
    csv_file. write(url_content)
    csv_file.close()

    cases_df = pd.read_csv("data/raw/case_data.csv")

    return cases_df


def plotHistByCond(startDate, endDate, condition):
    """
    Plots the number of covid19 cases with respect to the condition
    using histogram for the period specified by startDate and endDate

    Parameters
    ----------
    startDate : datetime64
                the start date of the period
    endDate   : datetime64
                the end date of the period
    condition : string
                Age or Region

    Returns
    -------
    plot : altair.Chart object
           An altair plot object displaying histogram

    Examples
    --------
    >>> bccovideda.plotHistByCond("2021-01-01", "2021-12-31", Age)
    """

    covid = getData()

    mask = (covid["Reported_Date"] > startDate) & (covid["Reported_Date"] <= endDate)
    temp = covid.loc[mask]

    age_group_label = [
        '90+', '80-89', '70-79', '60-69', '50-59', '40-49', '30-39',
        '20-29', '10-19', '<10'
    ]

    region_label = [
        'Fraser', 'Vancouver Coastal', 'Vancouver Island', 'Interior',
        'Northern', 'Out of Canada'
    ]

    if condition == "Age":
        plot = alt.Chart(temp, title="Number of Cases by Age Group").mark_bar().encode(
            y=alt.Y("Age_Group", sort=age_group_label, title="Age Group"),
            x=alt.X("count()", title="Number of Cases"))
    if condition == "Region":
        plot = alt.Chart(temp, title="Number of Cases by Region").mark_bar().encode(
            y=alt.Y("HA", sort=region_label, title="Region"),
            x=alt.X("count()", title="Number of Cases"))

    return plot


def plotLineByDate(startDate, endDate, region = 'all'):
    """
    Plots the line chart of regional cases over the period of specified time range.
    The lines are colored according to the region. The default starts from
    '2020-01-29' date. 

    Parameters
    ----------
    startDate : string
                the start date of the period. The first accepted value is 
                set to'2020-01-29'.
    endDate   : string
                the end date of the period. Cannot take on date that comes before
                the last record available (one day prior the day of using the package). 
    region : string 
             specify the region for the line to be plotted. Default are all regions. 

    Returns
    -------
    plot : altair.Chart object
           An altair plot object displaying line chart

    Examples
    --------
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31")
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31", region = 'HA')
    """

def showSummaryStat(startDate, endDate):
    """
    A function to show summary statistics for the COVID cases in BC
    for the period specified in the parameter

    Parameters
    ----------
    param1 : startDate (str: YYYY-MM-DD)
        Start Date of the period (inclusive)
    param2 : endDate (str: YYYY-MM-DD)
        End Date of the period (inclusive)

    Returns
    -------
    pandas.DataFrame
        Data frame containing summary statistics with the followings:
        total_cases_count, latest_date, latest_daily_cases_count, 
        max_date, max_daily_cases_count, min_date, min_daily_cases_count, 
        max_age_group, max_age_group_count, min_age_group, min_age_group_count,
        max_region, max_region_count, min_region, min_region_count,


    Examples
    -------
    >>> showSummaryStat("2022-01-01", "2022-01-13")

    """

    df = getData()
    mask = (df["Reported_Date"] >= startDate) & (df["Reported_Date"] <= endDate)
    df = df.loc[mask]

    # total_cases_count
    total = len(df)

    # count by date
    count_df = df["Reported_Date"].value_counts()
    # latest_date, latest_daily_cases_count
    latest_date_count = count_df.loc[endDate]
    # max_date, max_daily_cases_count
    max_date = count_df.idxmax()
    max_daily_cases_count = count_df.max()
    # min_date, min_daily_cases_count
    min_date = count_df.idxmin()
    min_daily_cases_count = count_df.min()

    # count by age group
    age_df = df["Age_Group"].value_counts()
    # max_age_group, max_age_group_count
    max_age_group = age_df.idxmax()
    max_age_group_count = age_df.max()
    # min_age_group, min_age_group_count
    min_age_group = age_df.idxmin()
    min_age_group_count = age_df.min()

    # count by region
    region_df = df["HA"].value_counts()
    # max_region, max_region_count
    max_region = region_df.idxmax()
    max_region_count = region_df.max()

    # min_region, min_region_count,
    min_region = region_df.idxmin()
    min_region_count = region_df.min()

    summary_df = pd.DataFrame(
        {
            "total_cases_count": [total],
            "latest_date": [endDate],
            "latest_daily_cases_count": [latest_date_count],
            "max_date": [max_date],
            "max_daily_cases_count": [max_daily_cases_count],
            "min_date": [min_date],
            "min_daily_cases_count": [min_daily_cases_count],
            "max_age_group": [max_age_group],
            "max_age_group_count": [max_age_group_count],
            "min_age_group": [min_age_group],
            "min_age_group_count": [min_age_group_count],
            "max_region": [max_region],
            "max_region_count": [max_region_count],
            "min_region": [min_region],
            "min_region_count": [min_region_count],
        }
    )

    return summary_df

def plotLineByDate(startDate, endDate, region='all'):
    """
    Plots the line chart of regional cases over the period of specified time range.
    The lines are colored according to the region. The default starts from
    '2020-01-29' date. 

    Parameters
    ----------
    startDate : string
                the start date of the period. The first accepted value is 
                '2020-01-29'.
    endDate   : string
                the end date of the period. Cannot take on date that comes before
                the last record available (one day prior the day of using the package). 
    region : string 
             specify the region for the line to be plotted. Default is all regions. 

    Returns
    -------
    plot : altair.Chart object
           An altair plot object displaying line chart

    Examples
    --------
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31")
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31", region = 'HA')
    """