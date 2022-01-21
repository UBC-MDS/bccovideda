import pandas as pd
import altair as alt
import datetime
alt.data_transformers.enable('data_server')
from bccovideda.bccovideda import get_data


def plot_hist_by_cond(startDate, endDate, condition):
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

    # test input type
    if not isinstance(startDate, str):
        raise TypeError("'startDate' should be string.")
    if not isinstance(endDate, str):
        raise TypeError("'endDate' should be string.")
    if not isinstance(condition, str):
        raise TypeError("'endDate' should be string.")


    # test input format 
    try:
        datetime.datetime.strptime(startDate, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    try:
        datetime.datetime.strptime(endDate, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


    covid = get_data()
    

    # test input value
    if not(endDate <= covid.iloc[-1:, 0].values[0]):
        raise ValueError('Invalid argument value: endDate cannot be later '
                         'than the day the package is called.')
    if not(startDate >= covid.iloc[0:, 0].values[0]):
        raise ValueError('Invalid argument value: startDate cannot be earlier '
                         'than the day the first case was recorded.')
    if not(startDate < endDate):
        raise ValueError('Invalid argument value: endDate cannot be earlier '
                         'than the startDate.')
    if not(condition == "Age" or "Region"):
        raise ValueError('Invalid argument value: condition should be either '
                         '"Age" or "Region"')

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
