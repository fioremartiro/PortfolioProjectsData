import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns

# URL of the World Surf League women's rankings page
url = "https://www.worldsurfleague.com/athletes/tour/wct?year=2024"

# Perform the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    if len(tables) > 0:
        # Select the first table
        table = tables[0]
        
        # Extract table headers
        headers = [header.text.strip() for header in table.find_all('th')]
        
        # Define the expected headers
        expected_headers = ['Rank', 'Name', '1 event', '2 event', '3 event', '4 event', '5 event', '6 event', '7 event', '8 event', 'Total Points']
        
        # Extract table rows
        rows = table.find_all('tr')[1:]  # Skip the header row
        
        # Extract data from each row
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            
            # Combine the relevant columns into the desired structure
            if len(cols) >= 14:
                combined_row = [
                    cols[0],  # Rank
                    cols[3],  # Name
                    cols[4],  # 1 event
                    cols[5],  # 2 event
                    cols[6],  # 3 event
                    cols[7],  # 4 event
                    cols[8],  # 5 event
                    cols[9],  # 6 event
                    cols[10],  # 7 event
                    cols[11],  # 8 event
                    cols[13]  # Total Points
                ]
                data.append(combined_row)
        
        # Create a DataFrame with the data
        df = pd.DataFrame(data, columns=expected_headers)
        
        # Replace "-" with 0 and convert to numeric
        df.replace("-", "0", inplace=True)
        
        # Remove commas and convert columns to numeric types where applicable
        for col in df.columns[2:]:
            df[col] = df[col].str.replace(",", "").astype(float)
        
        # Split the 'Name' column into 'Name' and 'Country'
        df[['Name', 'Country']] = df['Name'].str.extract(r'^(.*?)([A-Z][a-z]+(?: [A-Z][a-z]+)*)$')
        
        # Replace specific incorrect country abbreviations
        df['Country'].replace({'States': 'United States', 'Rica': 'Costa Rica'}, inplace=True)
        
        # Ensure the correct column order
        df = df[['Rank', 'Country', 'Name'] + df.columns[2:10].tolist() + ['Total Points']]
        
        # Save the cleaned DataFrame to a CSV file
        df.to_csv('women_surf_rankings_2024_cleaned.csv', index=False)
        print("Cleaned data saved to 'women_surf_rankings_2024_cleaned.csv'")
        
        # Upload the DataFrame to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['surf_database']
        collection = db['women_surf_rankings_2024']
        
        # Convert the DataFrame to a dictionary and insert into MongoDB
        data = df.to_dict(orient='records')
        collection.insert_many(data)
        print("Data successfully uploaded to MongoDB.")
        
        # Data visualization
        # First analysis of performance by Country
        country_points = df.groupby('Country')['Total Points'].sum()
        
        # Plot a pie chart of the total points by country
        plt.figure(figsize=(10, 8))
        country_points.plot.pie(autopct='%1.1f%%', colors=sns.color_palette('Blues', len(country_points)))
        plt.title('Performance by Country')
        plt.ylabel('')
        plt.show()
        
        # Second analysis: Bar graph of scores across events for different countries
        event_cols = ['1 event', '2 event', '3 event', '4 event', '5 event', '6 event', '7 event', '8 event']
        df_melted = df.melt(id_vars=['Country', 'Name'], value_vars=event_cols, var_name='Event', value_name='Points')
        
        plt.figure(figsize=(12, 8))
        sns.barplot(data=df_melted, x='Event', y='Points', hue='Country', ci=None)
        plt.title('Scores Across Events for Different Countries')
        plt.xlabel('Event')
        plt.ylabel('Points')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig('scores_by_event_country.png')
        plt.show()
        
    else:
        print("No tables found on the page.")
else:
    print("Failed to retrieve the webpage:", response.status_code)
