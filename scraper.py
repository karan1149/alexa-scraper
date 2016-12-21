import csv
import sys

with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile);
    alexaDict = {row[1]: int(row[0]) for row in reader if int(row[0]) < int(sys.argv[2]) + 1};

print alexaDict;
