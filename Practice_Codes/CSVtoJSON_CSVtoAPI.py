'''
import csv
import json

with open('Uttarkhan_DESCO_Data.csv', 'r') as f:
    # print(f.read())
    # reader = csv.reader(f)
    reader = csv.DictReader(f)
    # for row in reader:
    #     print(row)

    data = []
    for row in reader:
        entry = {
            'address': row['address'],
            'lat-long': {
                'latitude': row['latitude'],
                'longitude': row['longitude']
            },
            'st-makepoint': row['st_makepoint']
        }
        data.append(entry)

# for item in data:
#     print(item)

# print(json.dumps(data, indent=4))

with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)
print("JSON file export successfully...")

'''

from fastapi import FastAPI, Query
import csv
from typing import List, Optional

app = FastAPI()

def read_csv():
    with open('Uttarkhan_DESCO_Data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:
            entry = {
                'address': row['address'],
                'lat-long': {
                    'latitude': float(row['latitude']),
                    'longitude': float(row['longitude'])
                },
                'st-makepoint': row['st_makepoint']
            }
            data.append(entry)
    return data

@app.get("/address", response_model=List[dict])
async def get_address(
    lat: Optional[float] = Query(None, description="Latitude to filter addresses"),
    long: Optional[float] = Query(None, description="Longitude to filter addresses")
):
    data = read_csv()

    if lat is not None and long is not None:
        filtered_data = [
            item for item in data
            if item['lat-long']['latitude'] == lat and item['lat-long']['longitude'] == long
        ]
        return filtered_data

    return data

@app.get("/address/range", response_model=List[dict])
async def get_address_by_range(
    min_lat: Optional[float] = Query(None, description="Minimum latitude"),
    max_lat: Optional[float] = Query(None, description="Maximum latitude"),
    min_long: Optional[float] = Query(None, description="Minimum longitude"),
    max_long: Optional[float] = Query(None, description="Maximum longitude")
):
    data = read_csv()

    filtered_data = [
        item for item in data
        if (min_lat is None or item['lat-long']['latitude'] >= min_lat)
        and (max_lat is None or item['lat-long']['latitude'] <= max_lat)
        and (min_long is None or item['lat-long']['longitude'] >= min_long)
        and (max_long is None or item['lat-long']['longitude'] <= max_long)
    ]

    return filtered_data
