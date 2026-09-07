import csv

INPUT = "tiobe-4.csv"
OUTPUT = "tiobe-4-wide.csv"

languages = ["C", "C#", "Java", "Rust"]

data = {}

with open(INPUT, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        date = row["date"]
        language = row["language"]
        rating = row["rating"]

        data.setdefault(date, {})
        data[date][language] = rating

with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["date", *languages])

    for date in sorted(data):
        writer.writerow([
            date,
            *(data[date].get(language, "") for language in languages)
        ])

print(f"Wrote {OUTPUT}")
