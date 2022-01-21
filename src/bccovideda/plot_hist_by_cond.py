import pandas as pd
import altair as alt
import datetime
alt.data_transformers.enable('data_server')


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
