import pandas as pd


def load(path: str) -> pd.DataFrame:
    """"""
    try:
        df = pd.read_csv(path)
        print('Loading dataset of dimensions ', df.shape)
    except FileNotFoundError as e:
        print(e)
    return df


print(load('../life_expectancy_years.csv').head(5))
