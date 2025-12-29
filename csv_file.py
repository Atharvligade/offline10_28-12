import csv
import os

os.makedirs("city", exist_ok=True)

files = {
    "Pune": open("city/Pune.csv", "w", newline=""),
    "Mumbai": open("city/Mumbai.csv", "w", newline=""),
    "Nashik": open("city/Nashik.csv", "w", newline=""),
    "Thane": open("city/Thane.csv", "w", newline="")
}

headers = ["city", "car_id", "brand", "model", "year", "price_lakh"]

writers = {}
for city, f in files.items():
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writers[city] = writer

with open("car_details_by_city.csv", "r") as fp:
    reader = csv.DictReader(fp)

    for row in reader:
        city = row["city"]
        if city in writers:
            writers[city].writerow(row)

for f in files.values():
    f.close()
