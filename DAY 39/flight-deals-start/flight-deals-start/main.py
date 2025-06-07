from data_manager import DataManager
from flight_search import FlightSearch

# Initialize objects
data_manager_obj = DataManager()
flight_search_obj = FlightSearch()

# Get sheet data
sheet_data = data_manager_obj.get_data()

# Print current sheet data
print("Current sheet data:", sheet_data)

# Loop through each row and check if iataCode is empty
for row in sheet_data:
    if row["iataCode"] == "":
        city_name = row["city"]
        row_id = row["id"]

        # Call FlightData (for now returns "TESTING")
        iata_code = flight_search_obj.get_destination_code(city_name)

        # Update local sheet_data dictionary
        row["iataCode"] = iata_code

        # Update Google Sheet via DataManager
        data_manager_obj.update_iata_code(row_id, iata_code)

# Print updated sheet data in memory
print("Updated sheet data:", sheet_data)
