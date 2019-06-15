import csv
d = {}
csv_path = "data.csv"
with open(csv_path, "r") as f_obj:
    reader = csv.DictReader(f_obj)
    for i in reader:
       print(i)
print(d)