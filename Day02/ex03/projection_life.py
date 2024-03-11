import matplotlib.pyplot as plt
from load_csv import load

# TODO: add __doc__


def main():
    """"""
    loaded_income_pp = load('../income_per_person_gdppercapita\
                            _ppp_inflation_adjusted.csv')
    loaded_life_expectancy = load('../life_expectancy_years.csv')
    income_pp = loaded_income_pp['1900']
    life_expectancy = loaded_life_expectancy['1900']
    life_expectancy.fillna(0, inplace=True)
    plt.scatter(income_pp, life_expectancy)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    plt.show()


if __name__ == '__main__':
    main()
