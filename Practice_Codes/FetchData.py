import csv 
import requests

def get_university_data():
    university = input("Enter University: ")
    country = input("Enter Country: ")

    url = f"https://geo.bmapsbd.com/bk/v2/autocomplete?text={university}&country={country}"

    try:
        response = requests.get(url)
        status = response.status_code
        # print(status)
        data = response.json()
        # print(data)
        extracted_data = []
        for item in data.get("places", []):
            country = item.get("country", "N/A")
            country_code = item.get("country_code", "N/A")
            address = item.get("address", "N/A")
            location = item.get("location", [])
            if isinstance(location, list) and len(location) == 2:
                lat, lon = location 
            else:
                lat, lon = "N/A", "N/A"

            extracted_data.append([country, country_code, address, lat, lon])

        fileName = "university_data.csv"
        with open(fileName, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Country", "Country Code", "Address", "Latitude", "Longitude"])
            writer.writerows(extracted_data)
        print(f"Data Saved to {fileName}")

    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    get_university_data()