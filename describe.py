from pandas import DataFrame
import numpy as np


def modify_col(column):
    new_column = column.sort_values(ignore_index=True)
    new_column.dropna()
    return (new_column)


def ft_count(column):
    total = 0
    for row in column:
        total += 1
    return total


def ft_mean(column, total):
    sumr = 0
    for row in column:
        sumr += row
    return (sumr / total)


def ft_quartiles(column, total, desc_df):
    """A quartile is value, that a certain percentage will stand above.
    i.e : in a range from 1 to 10, second quartile (50%) would be 5.5, 
    so half of value would stand below and half above"""

    if total % 2 == 0:
        desc_df[column]['25%'] = (column[total / 4] + column[total / 4] - 1) / 2
        desc_df[column]['50%'] = (column[total / 2] + column[total / 2] - 1) / 2
        desc_df[column]['75%'] = (column[total / 4 * 3] + column[total / 4 * 3] + 1) / 2
    else:
        desc_df[column]['25%'] = (column[total / 4]) / 2
        desc_df[column]['50%'] = (column[total / 2]) / 2
        desc_df[column]['75%'] = (column[total / 4 * 3]) / 2


def ft_var(column, total):


def calculate_for_col(column, desc_df):
    total = ft_count(column)
    desc_df[column]['total'] = total
    desc_df[column]['Mean'] = ft_mean(column, total)
    desc_df[column]['Min'] = desc_df[column][0]
    desc_df[column]['Max'] = desc_df[column][total - 1]
    ft_quartiles(column, total, desc_df)
    desc_df[column]['Var'] = ft_var()
    desc_df[column]['Max'] = desc_df[column][total - 1]
    



def describe(data: DataFrame):
    """Homemade describe function"""
    # select all numerics datas
    features = data.select_dtypes(include=np.number)
    # check s'il est vide!
    # virer l index
    columns = features.columns
    desc_df = DataFrame(columns=columns,
                        index=["Count", "Mean", "Std", "Min", "25%",
                               "50%", "75%", "Max"])
    
    for col in columns:
        sorted_column = modify_col(features[col])
        calculate_for_col(sorted_column, desc_df)