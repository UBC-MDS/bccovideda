from bccovideda.bccovideda import plot_line_by_date

import pytest 
import pandas as pd

def test_type_error():
    """
    Tests the plot_line_by_date function to make sure the inputs' type are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    pd.read_csv("tests/case_data_sample.csv")

    # Test the TypeError is correctly raised when the type of
    # arguments is incorrect
    with pytest.raises(TypeError):
         plot_line_by_date(21, '2021-10-08')
    
    with pytest.raises(TypeError):
         plot_line_by_date('2021-10-08', 21)
    
    with pytest.raises(TypeError):
         plot_line_by_date('2021-10-08', '2021-10-20', 24)

def test_value_error():
    """
    Tests the plot_line_by_date function to make sure the inputs' values are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Test the ValueError is correctly raised when the value of
    # arguments is incorrect
    with pytest.raises(ValueError):
         plot_line_by_date('2018-09-08', '2021-10-08')
    
    with pytest.raises(ValueError):
         plot_line_by_date('2021-09-08', '2023-10-08')

    with pytest.raises(ValueError):
         plot_line_by_date('2021-09-08', '2021-10-08', ['Frazer'])
    
    with pytest.raises(ValueError):
         plot_line_by_date('2021-09-08', '2021-10-08', ['all'])

    with pytest.raises(ValueError):
         plot_line_by_date('2021-09-08', '2021-10-08', [])

    with pytest.raises(ValueError):
         plot_line_by_date('2021- 0 9-08', '2021-10-08')

def test_date_format():
    """
    Tests the plot_line_by_date function to make sure the passed date is of correct format
    values are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    with pytest.raises(ValueError) as e:
        plot_line_by_date('20-10-2021', '2020-10-08')
    assert str(e.value) == "Incorrect date format, should be YYYY-MM-DD"

    with pytest.raises(ValueError) as e:
        plot_line_by_date('2020-10-08', '2020-14-08')
    assert str(e.value) == "Incorrect date format, should be YYYY-MM-DD"

def test_plot_attributes():
    """
    Tests the plot_line_by_date function to make sure the passed date is of correct format
    values are correct.
    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """

    # Test the plot attributes
    plot_all = plot_line_by_date('2021-10-28', '2021-12-28')
    plot_filter = plot_line_by_date('2021-10-28', '2021-12-28', ['Fraser'])
    assert str(type(plot_all)) == "<class 'altair.vegalite.v4.api.Chart'>"
    assert str(type(plot_filter)) == "<class 'altair.vegalite.v4.api.Chart'>"
    assert plot_all.encoding.x.shorthand == 'Reported_Date', 'x_axis should be mapped to the x axis'
    assert plot_all.encoding.y.shorthand == 'count()', 'y_axis should be mapped to the y axis'
    assert plot_all.encoding.color.shorthand == 'HA', 'color should be mapped to the color axis'
    assert plot_filter.encoding.color.shorthand == 'HA', 'color should be mapped to the color axis'
    assert plot_all.mark == 'line', 'mark should be a line'
    assert plot_filter.mark == 'line', 'mark should be a line'

