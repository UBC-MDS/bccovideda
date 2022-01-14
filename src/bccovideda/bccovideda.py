


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