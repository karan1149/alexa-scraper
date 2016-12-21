import csv
import sys

with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile);
    alexaDict = {row[1]: row[0] for row in reader if row[0] < sys.argv[2] + 1};

print alexaDict;
