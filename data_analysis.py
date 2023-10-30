import pandas as pd
import time
import psutil


def load_data(datapath):
    return pd.read_csv(datapath, sep=";")


def get_data_descriptive_stats(dataframe, column):
    statistics = {
        "Mean": dataframe[column].mean(),
        "Median": dataframe[column].median(),
        "StdDev": dataframe[column].std(),
        "Min": dataframe[column].min(),
        "Max": dataframe[column].max(),
    }
    return pd.Series(statistics)


def test_loaddata():
    # load iris dataset
    path = "cars.csv"
    iris_df = load_data(path)
    assert isinstance(iris_df, pd.DataFrame)
    assert not iris_df.empty


def test_descriptive_stats():
    path = "cars.csv"
    vehicles_df = load_data(path)
    statistics = get_data_descriptive_stats(vehicles_df, "Acceleration")
    # print(statistics['Mean'])
    assert statistics["Mean"] == 15.519704433497537
    print(statistics)


def test():
    start = time.time()
    test_loaddata()
    test_descriptive_stats()

    end = time.time()
    duration = end - start
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory()

    print(f"Elapsed time: {duration:.4f} seconds")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {mem_usage.percent}%")


if __name__ == "__main__":
    print("Python performance:")
    test()
