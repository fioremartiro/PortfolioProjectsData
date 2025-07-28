"""Plot a Mathplotlib pie chart"""
import get_df as data
import matplotlib.pyplot as plt

df = data.GetDf("files\\spacex_launch_data(prep).csv")

def prep_data():
    """Data preparation to pie chart"""
    csv_dataframe = df.get_df()
    #Outcome totals
    outcome_totals = {}
    #Output lists to pie chart
    new_outcome = []
    total_of_outcomes = []

    #Format "Mission Outcome" data to float totals
    for outcome in csv_dataframe["Mission Outcome"]:
        if outcome in outcome_totals:
            outcome_totals[outcome] = outcome_totals[outcome] + 1.0
            
        else:
            outcome_totals[outcome] = 1.0
    
    #Add totals to output lists
    for outcome2, number in outcome_totals.items():
        new_outcome.append(outcome2)
        total_of_outcomes.append(number)   

    return total_of_outcomes, new_outcome


def display_pie(total_of_outcomes: list, new_outcome: list):
    """Display pie plot from input lists"""
    colors = ['b', 'y', 'g', 'r']
    font1 = {'family':'serif','color':'blue','size':20}
    plt.title("Flight results", fontdict = font1)
    plt.pie(total_of_outcomes, labels = new_outcome, autopct = '%1.1f%%', colors=colors,
            radius = 1.2, shadow = True)
    plt.legend()
    plt.show()


def main():
    """Main execution"""
    total, new = prep_data()
    display_pie(total, new)



if __name__ == "__main__":
    main()