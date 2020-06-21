import json
import csv

with open('/Users/olgabuchel/Downloads/all_canada_hr (1).json') as json_file:
    data = json.load(json_file)
    with open('Canada_names.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["HR_UID","ENGNAME"])
        for el in data["features"]:
            print(el["properties"])
            spamwriter.writerow([el["properties"]['HR_UID'], el["properties"]['ENGNAME']])
