import matplotlib.pyplot as plt
from load_csv import load


def main():
    loaded = load('../life_expectancy_years.csv')
    df = loaded[loaded['country'] == 'Morocco']

    years = df.columns[1:]
    country_values = df.values[0][1:]
    plt.plot(years, country_values)
    plt.title('Morocco Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.xticks(years[::40])
    plt.yticks(range(30, 110, 10))
    plt.show()


if __name__ == '__main__':
    main()
