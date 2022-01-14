
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
