import matplotlib.pyplot as plt
from load_csv import load


def main():
    """"""
    loaded = load('../population_total.csv')
    maroc = loaded[loaded['country'] == 'Morocco']
    france = loaded[loaded['country'] == 'France']
    maroc_values = maroc.loc[:, '1800':'2050'].values[0, :]
    france_values = france.loc[:, '1800':'2050'].values[0, :]
    maroc_years = maroc.loc[:, '1800':'2050'].columns[:]
    france_years = france.loc[:, '1800':'2050'].columns[:]
    print(maroc_years.shape, maroc_values.shape)
    plt.plot(maroc_years, maroc_values, label='Morocco')
    plt.plot(france_years, france_values, label='France')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(maroc_years[::40], france_years[::40])
    plt.yticks(maroc_values[::20], france_values[::20])
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
