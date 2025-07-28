"""Plot a Mathplotlib plot chart"""
import pandas as pd
import matplotlib.pyplot as plt

def prep_data(data: pd.DataFrame):
    """Prep dates data for Mathplotlib chart"""
    years = {}

    csv_dataframe = data.get_df()

    for date in csv_dataframe["Date"]:
        new_date = date[:-6]
        
        if new_date in years:
            years[new_date] = years[new_date] + 1
            
        else:
            years[new_date] = 1
            
            
    dates = []
    total_of_launches = []

    for date, number in years.items():
        dates.append(date)
        total_of_launches.append(number)  

    return dates, total_of_launches

def plot_chart(dates: list, total_of_launches: list):
    """Plot Mathplotlib chart"""
    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Launches by  Year", fontdict = font1)
    plt.grid(zorder=0)
    plt.plot(dates, total_of_launches,marker='o', markersize=4)
    plt.xlabel("Year")
    plt.ylabel("Total launches")
    plt.show()


def main():
    """Main execution"""
    dates, total = prep_data()
    plot_chart(dates, total)


if __name__ == "__main__":
    main()