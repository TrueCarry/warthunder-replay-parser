import csv
import os
import json

csvfile = open('players.csv', 'w', newline='')
csvw = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

csvw.writerow([
  "map",
  "player_id",
  "vehicle",
])

for filename in os.listdir("results/"):
   with open(os.path.join("results/", filename), 'r') as f: # open in readonly mode
      data = json.load(f)
      for player in data["players"]:
        for vehicle in player["vehicles"]:
          csvw.writerow([
            filename.replace(".json", ""),
            player['player_id'],
            vehicle['vehicle'],
          ])

csvfile.close()