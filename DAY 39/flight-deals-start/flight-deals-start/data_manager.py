import requests

SHEETY_ENDPOINT = "https://api.sheety.co/YOUR_PROJECT_ID/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.sheety_endpoint = SHEETY_ENDPOINT

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, )
        response.raise_for_status()
        data = response.json()
        return data["prices"]

    def update_iata_code(self, row_id, iata_code):
        update_endpoint = f"{self.sheety_endpoint}/{row_id}"
        new_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=update_endpoint, json=new_data,)
        response.raise_for_status()
        print(f"✅ Updated row {row_id} with IATA code: {iata_code}")
