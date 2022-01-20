
import requests
import os
import pandas as pd
import altair as alt
import datetime
alt.data_transformers.enable('data_server')


def get_data(url="http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv", out_folder="data/raw"):
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
    >>> get_data()
    """
    if not os.path.exists(os.getcwd() + "/" + out_folder):
        os.makedirs(out_folder + "/")

    req = requests.get(url)
    url_content = req.content

    csv_file = open("data/raw/case_data.csv", "wb")
    csv_file.write(url_content)
    csv_file.close()

    cases_df = pd.read_csv("data/raw/case_data.csv", 
                            parse_dates = ['Reported_Date'])

    return cases_df


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


def plot_line_by_date(startDate, endDate, region='all'):
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
    region    : list or str = 'all'
                Default value is string 'all' - displaying all regions.
                Other available values: combination of list of strings
                from available regions - Fraser, Vancouver Coastal, Vancouver Island, 
                Interior, Northern, Out of Canada

    Returns
    -------
    plot : altair.Chart object
           An altair plot object displaying line chart

    Examples
    --------
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31")
    >>> bccovideda.plotLineByDate("2021-01-01", "2021-12-31", region = ['Fraser'])
    """

    covid = get_data()

    # convert date column to string 
    covid['Reported_Date'] = covid['Reported_Date'].apply(str)
    covid['Reported_Date']= covid['Reported_Date'].str.slice(0, 10)

    # check the date format 
    try:
        datetime.datetime.strptime(startDate, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    try:
        datetime.datetime.strptime(endDate, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    # check argument validity
    if not(isinstance(startDate, str)):
        raise TypeError('Invalid argument type: startDate must be a string.')
    elif not(isinstance(endDate, str)):
        raise TypeError('Invalid argument type: endDate must be a string.')
    elif not(isinstance(region, list) or region == 'all'):
        raise TypeError(
            'Invalid argument type: region must be a list or have a value `"all"`.')

    # check arguments value
    elif not(endDate <= covid.iloc[-1:, 0].values[0]):
        raise ValueError('Invalid argument value: endDate cannot be later '
                         'than the day the package is called.')
    elif not(startDate >= covid.iloc[0:, 0].values[0]):
        raise ValueError('Invalid argument value: startDate cannot be earlier '
                         'than the day the first case was recorded.')
    elif not(startDate < endDate):
        raise ValueError('Invalid argument value: endDate cannot be earlier '
                         'than the startDate.')
    elif not(set(region).issubset(set(pd.unique(covid['HA']))) or region == 'all'):
        raise ValueError('Invalid argument value: region must be valid BC region - '
                         'Either combination of `Fraser, Vancouver Coastal, Vancouver Island, '
                         'Interior, Northern, Out of Canada` or `all`')
    elif not(len(region) > 0):
        raise ValueError(
            'Invalid argument value: region cannot be an empty list')
    elif not(len(startDate) == 10 and len(endDate) == 10):
        raise ValueError('Invalid argument value: startDate and endDate format is ' \
                         '`YYYY-MM-DD` without spaces.'
                        )

    # filter the data
    if region == 'all':
        mask = ((covid["Reported_Date"] > startDate) &
                (covid["Reported_Date"] <= endDate))
    else:
        mask = ((covid["Reported_Date"] > startDate) &
                (covid["Reported_Date"] <= endDate) &
                covid["HA"].isin(region))

    # keep the filtered data
    temp = covid.loc[mask]

    # plot the line chart
    plot = (alt.Chart(temp,
                      title="Number of COVID19 cases over time")
            .mark_line().encode(
                x=alt.X("Reported_Date",
                        title="Date"),
                y=alt.Y("count()",
                        title="Number of Cases"),
                color=alt.Color("HA",
                                title='Region'))
            )

    return plot


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
