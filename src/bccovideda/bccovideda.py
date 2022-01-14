import requests
import os
import pandas as pd


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
