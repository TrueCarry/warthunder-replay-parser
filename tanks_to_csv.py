import csv
import os
import json

csvfile = open('vehicles.csv', 'w', newline='')
csvw = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

csvw.writerow([
  "vehicle",
  "economicRankArcade",
  "economicRankHistorical",
  "economicRankSimulation",
])

with open("wpcost.blkx", 'r') as f: # open in readonly mode
  data = json.load(f)
  for attribute, value in data.items():
      csvw.writerow([
        attribute,
        value['economicRankArcade'],
        value['economicRankHistorical'],
        value['economicRankSimulation'],
      ])

  # for player in data["players"]:
    # for vehicle in player["vehicles"]:
    #   csvw.writerow([
    #     filename.replace(".json", ""),
    #     player['player_id'],
    #     vehicle['vehicle'],
    #   ])

csvfile.close()