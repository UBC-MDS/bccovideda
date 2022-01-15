
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
    url        : string
                 URL to case data download page
    out_folder : string
                 Path to folder storing raw data set csv file

    Returns
    -------
    pandas.DataFrame : Dataframe containing entire BC Case Details Data

    Examples
    --------
    >>> getData()
    """


def showSummaryStat(startDate, endDate):
    """
    Shows summary statistics for the Covid19 cases in BC for the period
    specified by startDate and endDate (format: YYYY-MM-DD).

    Parameters
    ----------
    startDate : string
                the start date of the period 
                (no earlier than '2020-01-29')
    endDate   : string
                the end date of the period 
                (no later than today)

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


def plotLineByDate(startDate, endDate, region='all'):
    """
    Plots the line chart of regional Covid19 cases over the period specified by 
    startDate and endDate (format: YYYY-MM-DD). The default argument value 
    for region is "all", showing the total number of Covid19 cases in BC.

    Parameters
    ----------
    startDate : string
                the start date of the period 
                (no earlier than '2020-01-29')
    endDate   : string
                the end date of the period 
                (no later than today)
    region    : string
                Available regions - Fraser, Vancouver Coastal, Vancouver Island, Interior,
                Northern, Out of Canada, all(default)

    Returns
    -------
    plot : altair.Chart object
           An altair plot object displaying line chart

    Examples
    --------
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31")
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31", region = 'Fraser')
    """


def plotHistByCond(startDate, endDate, condition):
    """
    Plots the number of Covid19 cases with respect to the condition(per Age Group
    or Region) using histogram for the period specified by startDate and endDate

    Parameters
    ----------
    startDate : string
                the start date of the period 
                (no earlier than '2020-01-29')
    endDate   : string
                the end date of the period 
                (no later than today)
    condition : string
                Available condition - Age, Region

    Returns
    -------
    plot : altair.Chart object
           An altair plot object displaying histogram

    Examples
    --------
    >>> bccovideda.plotHistByCond("2021-01-01", "2021-12-31", "Age")
    """