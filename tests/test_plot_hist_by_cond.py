import pandas as pd
import altair as alt
import datetime
alt.data_transformers.enable('data_server')
from bccovideda.bccovideda import get_data
from bccovideda.plot_hist_by_cond import plot_hist_by_cond

def test_input_data():
  """
  Check Errors raised when incorrect inputs are used
  Test cases:
    1. input type
    2. input format
    3. input value
  
  """

  # test input type
  with pytest.raises(TypeError):
    plot_hist_by_cond(2021-01-01, 2021-12-31, Age)
    
  with pytest.raises(TypeError):
    plot_hist_by_cond("2021-01-01", "2021-12-31", Region)
    
  with pytest.raises(TypeError):
    plot_hist_by_cond(2021-01-01, 2021-12-31, "Age")
    
  with pytest.raises(TypeError):
    plot_hist_by_cond("2021-01-01", 2021-12-31, "Region")


  # test input format
  with pytest.raises(ValueError):
    plot_hist_by_cond("20210101", "20211231", "Age")
    
  with pytest.raises(ValueError):
    plot_hist_by_cond("2021/01/01", "2021/12/31", "Age")

  with pytest.raises(ValueError):
    plot_hist_by_cond("01-01-2021", "12-31-2021", "Age")
    
  with pytest.raises(ValueError):
    plot_hist_by_cond("Jan-01-2021", "Dec-31-2021", "Age")


  # test input value    
  with pytest.raises(ValueError):
    plot_hist_by_cond("2021-13-01", "2021-12-31", "Age")
    
  with pytest.raises(ValueError):
    plot_hist_by_cond("2021-01-01", "2021-12-31", "age")
    
  with pytest.raises(ValueError):
    plot_hist_by_cond("2021-13-01", "2021-12-31", "region")
    
  with pytest.raises(ValueError):
    plot_hist_by_cond("2021-01-01", "2021-12-31", "area")
