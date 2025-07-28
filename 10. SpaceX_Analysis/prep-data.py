"""Data preparation from MAthplotlib utilization"""
import config as conf

SPACEX_DF = spacex_df = conf.prepData.get_df()

def normalize_data():
    """Normalize csv data"""
    SPACEX_DF.set_index("Flight Number")
    #Fill NaN (meaning null) values from column "Payload Mass (kg)"
    SPACEX_DF["Payload Mass (kg)"].fillna(0,inplace=True)


def add_obirt_distances():
    """Add orbit distances from String name"""
    orbit_distances_km = {
        "LEO": "160-1000", 
        "LEO (ISS)": "70000", 
        "Polar LEO": "1000-200000",
        "GTO": "35786", 
        "Sun–Earth L1": "1500000", 
        "SSO": "1000-200000", 
        "HEO": "UNKNOWN",
        "Heliocentric 0.99–1.67 AU (close to Mars transfer orbit)": "<1500000" 
    }

    #Create variable to add new values to column
    orbitkm_column = []

    #Add column "Orbit" to new variable list
    orbit_names = spacex_df["Orbit"].to_list()

    for orbit in orbit_names:
        if orbit in orbit_distances_km.keys():
            orbitkm_column.append(orbit_distances_km[orbit])
            
        else:
            orbitkm_column.append("UNKNOWN")


    #Create new column in dataframe
    SPACEX_DF["Distance(km)"] = orbitkm_column


def add_launchpad_location():
    """Add launchpad location coordiante from String name"""
    luanchpad_locations = {
        "CCAFS LC-40": {
            "lat": "28.562330237327476",
            "lon": "-80.57737793335"
                    },
        "VAFB SLC-4E": {
            "lat": "34.6320855521928",
            "lon": "-120.6106501433503"
                    },
        "KSC LC-39A": {
            "lat": "34.641428083361867",
            "lon": "-120.5889458642861"
                    },
        "CCAFS SLC-40": {
            "lat": "28.562330237327476",
            "lon": "-80.57737793335"
                    }
    }

    #Create  empty variables to store new data
    launchpad_lat = []
    launchpad_lon = []

    #Save launchpad names column to a list
    launchpad_name = SPACEX_DF["Launch Site"].to_list()

    #1. Go trough each launchpad_name
    for site in launchpad_name:
    #2. Check if the launchpad name is in luanchpad_locations
        if site in luanchpad_locations.keys():
        #3. Add latitud and logitud to list variables (launchpad_lat & launchpad_lon)
            launchpad_lat.append(luanchpad_locations[site]["lat"])
            launchpad_lon.append(luanchpad_locations[site]["lon"])

    #4. Add list to dataframe
    SPACEX_DF["lat"] = launchpad_lat
    SPACEX_DF["lon"] = launchpad_lon

def create_new_csv():
    """Create new csv from pandas DataFrame"""
    conf.prepData.save_csv(SPACEX_DF)


def main():
    """Main execution"""
    #Normalize data
    normalize_data()
    #Add location to df
    add_launchpad_location()
    #Add distance to df
    add_obirt_distances()
    #Save new df to csv
    create_new_csv()


if __name__ == "__main__":
    main()