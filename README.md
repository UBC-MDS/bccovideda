[![ci-cd](https://github.com/UBC-MDS/bccovideda/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/bccovideda/actions/workflows/ci-cd.yml)
[![codecov](https://codecov.io/github/UBC-MDS/bccovideda/branch/main/graph/badge.svg)](https://codecov.io/github/UBC-MDS/bccovideda)
[![Documentation Status](https://readthedocs.org/projects/bccovideda/badge/?version=latest)](https://bccovideda.readthedocs.io/en/latest/?badge=latest)
# bccovideda

**Authors**:  Lianna Hovhannisyan, John Lee, Vadim Taskaev, Vanessa Yuen

The British Columbia Center for Disease Control (BCCDC) manages a range of provincial programs and clinics that contribute to public health and help control the spread of disease in BC. It administers and distributes the latest daily data on COVID-19 in British Columbia, which it provides in csv format along case-, lab- and regional-specific features as well as in comprehensive ArcGIS format via the [COVID-19 webpage](http://www.bccdc.ca/health-info/diseases-conditions/covid-19/data) (under "Download the data"). This package leverages daily case-specific COVID-19 data, allowing users to conveniently download the latest case data, and - per specified date range interval - compute several key statistics, visualize time series progression along age-related and regional parameters, and generate exploratory data analysis in the form of histogram figures supporting on-demand analysis. COVID-19 case detail parameters extracted using this package: 
- Reported_Date (in YYYY-MM-DD format)
- HA (provincial health region, e.g., "Vancouver Coast Health")
- Sex (M or F)
- Age_Group (reported along 10-yr age group bins, e.g., "60-69")
- Classification_Reported (diagnosis origin, e.g., "Lab-diagnosed")

## Installation

`bccovideda` can be installed from PyPI using the following terminal command:
```bash
$ pip install bccovideda
```

## Package Functions 

- `get_data()`
  - This function downloads the latest detailed daily case-specific COVID-19 from BCCDC's dedicated [COVID-19 homepage](http://www.bccdc.ca/health-info/diseases-conditions/covid-19/data). It returns a dataframe containing the extracted raw data. 

- `show_summary_stat()`
  - This function computes summary statistics from the available case-specific parameters, such as age-related and regional aggregate metrics. It returns a dataframe listing key identified summary statistics specified per the time interval queried. 

- `plot_line_by_date()`
  - This function returns a line chart plot of daily case counts, based on parameters and grouping selected by the user, per the time interval queried.

- `plot_hist_by_cond()`
  - This function returns a histogram plot based on parameters and grouping selected by the user, per the time interval queried, allowing for on-demand exploratory data analysis. 


## Usage

`bccovideda` can be used to download and compute summary statistics, generate exploratory data analysis histogram plots, and plot time series chart data as follows:
```python
from bccovideda.get_data import get_data
from bccovideda.show_summary_stat import show_summary_stat
from bccovideda.plot_hist_by_cond import plot_hist_by_cond
from bccovideda.plot_line_by_date import plot_line_by_date
```

```python
bccovideda.show_summary_stat("2022-01-01", "2022-01-13")
bccovideda.plot_hist_by_cond("2021-01-01", "2021-12-31", "Age")
bccovideda.plot_line_by_date("2021-01-01", "2021-12-31", region = ['Fraser'])
```

## Role within Python Ecosystem

Given the relatively adequate accessibility of latest aggregate COVID-19 data combined with its persistent impact on socio-economics since early 2020, there are a number of rather comprehensive Python packages that perform similar data extract and exploratory data analysis functions, such as [covid](https://pypi.org/project/covid/), [covid19pyclient](https://pypi.org/project/covid19pyclient/), [covid19pandas](https://github.com/PayneLab/covid19pandas). In contrast to existing packages, `bccovideda` provides a simple user interface that  focuses on the localized provincial context of British Columbia, utilizing features specific to BCCDC's data administration conventions for generating a quick overview and on-demand analysis of trends and statistics pertaining to age-related and regional case characteristics.

## Dependencies

-   Python 3.9 and Python packages:

    -   pandas==1.3.5
    -   requests==2.27.1
    -   altair==4.2.0
    -   altair-saver==0.5.0

## Documentation

Documentation `bccovideda` can be found at [Read the Docs](https://bccovideda.readthedocs.io)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Contributors

Group 25 Contributors:
- Lianna Hovhannisyan: @liannah
- John Lee: @johnwslee
- Vadim Taskaev: @vtaskaev1
- Vanessa Yuen: @imtvwy

## License

The `bccovideda` project was created by DSCI 524 (Collaborative Software Development) Group 25 within the Master of Data Science program at the University of British Columbia (2021-2022). It is licensed under the terms of the MIT license.

## Credits

`bccovideda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
