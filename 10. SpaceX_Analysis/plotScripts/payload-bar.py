"""Plot a Mathplotlib barh chart"""
import pandas as pd
import get_df as data
import matplotlib.pyplot as plt

df = data.GetDf("files\\spacex_launch_data(prep).csv")

def prep_data():
    """Prep csv dataframe to barh chart. returns top_10 by Payload Mass"""
    csv_dataframe = df.get_df()

    csv_dataframe.sort_values(by='Payload Mass (kg)')
    df_top_10 = csv_dataframe.head(10)

    df_top_10['Payload Mass (kg)'].str.replace('~', '')
    df_top_10['Payload Mass (kg)'].replace('Classified', "0") 
    df_top_10['Payload Mass (kg)'].fillna('0',inplace=True)

    
    return df_top_10
    

def plot_chart(df_top_10: pd.DataFrame):
    """Plot barh chart fom pandas dataframe"""
   # plotting a pie chart
    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Top 10 payload mass (kg) launches", fontdict = font1)
    plt.grid(zorder=0)
    plt.barh(df_top_10['Customer'], df_top_10['Payload Mass (kg)'], zorder=3)
    plt.show()


def main():
    """Main execution"""
    df = prep_data()
    plot_chart(df)



if __name__ == "__main__":
    main()