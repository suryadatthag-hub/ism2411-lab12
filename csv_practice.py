# ISM2411 Lab 12 - Suryadattha Gottimukkala
import csv
from datetime import datetime

# Exercise 1: Open the supplied CSV from the repository root.
# Exercise 2: Print all raw rows, including the header.
print("Exercise 2: Raw rows")
with open("data/sales.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Store and skip the header.
print("\nExercise 3: Header and data")
with open("data/sales.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    rows = list(reader)
    for row in rows:
        print(row)
print(f"Original data rows: {len(rows)}")

# Exercise 4: Convert strings and calculate revenue.
print("\nExercise 4: Order totals")
total_revenue = 0
orders = []
for row in rows:
    product = row[0].strip()
    price = float(row[1])
    quantity = int(row[2])
    total = round(price * quantity, 2)
    total_revenue += total
    orders.append([product, price, quantity, total])
    print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
total_revenue = round(total_revenue, 2)
print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5: Write only orders with totals strictly above $100.
written = 0
with open("data/cleaned.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for product, price, quantity, total in orders:
        if total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            written += 1
print(f"\nExercise 5: Wrote {written} of {len(rows)} original rows.")

# Exercise 6: Calculate the same totals with named columns.
# Prefer csv.reader for simple files with a known column order.
# Prefer DictReader for readable column names or changing column positions.
print("\nExercise 6: DictReader totals")
dict_revenue = 0
with open("data/sales.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"].strip()
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = round(price * quantity, 2)
        dict_revenue += total
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
dict_revenue = round(dict_revenue, 2)
print(f"DictReader total revenue: ${dict_revenue:.2f}")
assert dict_revenue == total_revenue, "Reader totals do not match"

# Exercise 7: Accumulate repeated products and sort by name.
summary = {}
with open("data/sales.csv", newline="", encoding="utf-8-sig") as file:
    for row in csv.DictReader(file):
        product = row["product"].strip()
        revenue = round(float(row["price"]) * int(row["quantity"]), 2)
        summary[product] = summary.get(product, 0) + revenue
print("\nExercise 7: Revenue by product")
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Append exactly one entry per script execution.
with open("data/run_log.txt", "a", encoding="utf-8") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")
print("\nExercise 8: Appended one entry to data/run_log.txt")
