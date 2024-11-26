import pandas as pd
from pandas import DataFrame
from display import display_data
from load_csv import load
import numpy as np

def modify_col(column):
    new_column = column.sort_values(ignore_index=True)
    return (new_column)

def main():
#   assert len(sys.argv) == 2, "Please provide a data file"
#   data = load(sys.argv[1])
    data = load("datasets/dataset_train.csv")

    print(data.dtypes)
    features = data.select_dtypes(include=np.number)
    columns = features.columns
    s_features = DataFrame()
    for col in columns:
        #print(col)
        s_features[col] = modify_col(features[col])
        print(s_features)
    display_data(s_features)

    print(data['Arithmancy'].quantile([0.25, 0.75]))
    display_data(data)




if __name__ == "__main__":
    main()


# ensuite, ca serit bien de comprendre = comment sont traitees les donnees : std ou norm
# a savoir au'il n'y a rien en dessous de 0.
# voir comment skip les nans ; les virer de l'echantillon et de fait pas les prendre en compte 
# dans le calculs (genre faire un conpteur puis len - compteur maybe?)
# commencer par virer les nan,puis trouver  min max, total, moyenne, afficher et voir comment on peut 
# uniformiser notre bordel