import json
import requests
from datetime import datetime

response = requests.get("https://api.covid19api.com/summary")
response.raise_for_status()
country_data = response.json()["Countries"]
today = datetime.today().strftime('%Y-%m-%d')

def delete_keys(country):
    del country["ID"]
    del country["Slug"]
    del country["Premium"]
    del country["NewRecovered"]
    del country["TotalRecovered"]
    country["Date"] = country["Date"][:10]
    return country

cleaned_country = list(map(delete_keys, country_data))

with open(f"data.json", "w") as fout:
    json.dump(cleaned_country, fout)
    fout.write("\n")
    print("API response written to data.json")

