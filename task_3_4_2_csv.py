import csv
from collections import defaultdict
from datetime import datetime

with open('Crimes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    # в словаре crimeDict будут хранится объекты типа int, которые инициализируются нулем
    crimeDict = defaultdict(int)
    for row in reader:
        # в американском стандарте даты сначала идет месяц (%m) затем день (%d) и год (%Y)
        year = datetime.strptime(row['Date'], '%m/%d/%Y %I:%M:%S %p').year
        crimeType = row['Primary Type']
        if year == 2015:
            crimeDict[crimeType] += 1
    print(max(crimeDict, key=crimeDict.get))
