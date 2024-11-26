from display import display_two_datas
from load_csv import load
from describe import describe


def main():
#   assert len(sys.argv) == 2, "Please provide a data file"
#   data = load(sys.argv[1])
    data = load("datasets/dataset_train.csv")
    print(describe(data))
    print(data.describe())

    print(data['Herbology'].quantile([.25, .50, .75], interpolation='midpoint'))
    print(data['Herbology'].quantile([.25, .50, .75], interpolation='linear'))
    print(data['Index'].quantile([.25, .50, .75], interpolation='midpoint'))
    print(data['Index'].quantile([.25, .50, .75], interpolation='linear'))

    display_two_datas(describe(data), data.describe())


if __name__ == "__main__":
    main()
    