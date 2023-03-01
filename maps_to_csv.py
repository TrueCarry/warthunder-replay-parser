import csv
import os
import json

csvfile = open('maps.csv', 'w', newline='')
csvw = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

csvw.writerow([
  "map",
  "level", #data['level'],
  "mission_file", #data['mission_file'],
  "mission_name", #data['mission_name'],
  "time_of_day", #data['time_of_day'],
  "weather", #data['weather'],
  "time_of_battle_ts", #data['time_of_battle_ts'],
  "time_of_battle", #data['time_of_battle'],
  "num_players", #data['num_players'],
])

for filename in os.listdir("results/"):
   with open(os.path.join("results/", filename), 'r') as f: # open in readonly mode
      data = json.load(f)
      csvw.writerow([
        filename.replace(".json", ""),
        data['level'],
        data['mission_file'],
        data['mission_name'],
        data['time_of_day'],
        data['weather'],
        data['time_of_battle_ts'],
        data['time_of_battle'],
        data['num_players'],
      ])

csvfile.close()