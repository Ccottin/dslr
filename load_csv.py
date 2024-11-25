import pandas as pd
from pandas import DataFrame
from display import display_data


def load(path: str) -> DataFrame:
    """takes a path as argument, writes the dimensions of the data set
    and returns it."""
    try:
        data = pd.read_csv(path)
        return (data)
    except Exception as e:
        print("Error: ", str(e))
        return None

# data = load("datasets/dataset_test.csv")


def main():
#   assert len(sys.argv) == 2, "Please provide a data file"
#   data = load(sys.argv[1])
    data = load("datasets/dataset_train.csv")
    sorted_args = list(data['Arithmancy'].dropna())
    sorted_args.sort()
    size = len(sorted_args)
    print(size)
    quartile = sorted_args[int(size / 4)]
    quartile3 = sorted_args[int(size * 3 / 4)]
    print(quartile, quartile3)
    print(data['Arithmancy'].quantile([0.25, 0.75]))
    display_data(data)




if __name__ == "__main__":
    main()


# TO DO == deja, faire un main :}}
# ensuite, ca serit bien de comprendre = comment sont traitees les donnees : std ou norm
# a savoir au'il n'y a rien en dessous de 0.
# voir comment skip les nans ; les virer de l'echantillon et de fait pas les prendre en compte 
# dans le calculs (genre faire un conpteur puis len - compteur maybe?)
# commencer par virer les nan,puis trouver  min max, total, moyenne, afficher et voir comment on peut 
# uniformiser notre bordel