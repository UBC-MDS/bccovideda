# bccovideda

**Milestone1 Link**: <https://github.com/UBC-MDS/bc_covid_simple_eda>
**Authors**:  Lianna Hovhannisyan, John Lee, Vadim Taskaev, Vanessa Yuen

The British Columbia Center for Disease Control (BCCDC) manages a range of provincial programs and clinics that contribute to public health and help control the spread of disease in BC. It administers and distributes the latest daily data on COVID-19 in British Columbia, which it provides in csv format along case-, lab- and regional-specific features as well as in comprehensive ArcGIS format via its [COVID-19 webpage](http://www.bccdc.ca/health-info/diseases-conditions/covid-19/data) (under "Download the data"). This package leverages daily case-specific COVID-19, allowing users to conveniently download the latest data, and - per specified date range interval - compute several key statistics, visualize time series progression along age-related and regional parameters, and generate exploratory data analysis in the form of histogram figures supporting on-demand analysis. COVID-19 case detail parameters extracted using this package: 
- Reported_Date (in YYYY-MM-DD format)
- HA (provincial health region, e.g., "Vancouver Coast Health")
- Sex (M or F)
- Age_Group (reported along 10-yr age group bins, e.g., "60-69")
- Classification_Reported (diagnosis origin, e.g., "Lab-diagnosed")

## Installation

This package can be installed from PyPI using the terminal command:
```bash
$ pip install bccovideda
```

## Package Functions 

`getData()`
This function...

`showSummaryStat()`
This function...

`plotLineByDate()`
This function...

`plotHistByCond()`
This function...


## Usage

- TODO


## Role within Python Ecosystem

## Dependencies

-   Python 3.9 and Python packages:

    -   pandas==1.3.5
    -   requests==2.27.1

## Documentation

Documentation `bccovideda` can be found at [Read the Docs]()

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Contributors

Group 25 Contributors:
- Lianna Hovhannisyan: @liannah
- John Lee: @max780228
- Vadim Taskaev: @vtaskaev1
- Vanessa Yuen: @imtvwy

## License

The `bccovideda` project was created by DSCI 524 (Collaborative Software Development) Group 25 within the Master of Data Science program at the University of British Columbia (2021-2022). It is licensed under the terms of the MIT license.

## Credits

`bccovideda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
