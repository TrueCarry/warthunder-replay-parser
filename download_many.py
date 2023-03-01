import replays_scraper
import download_replay
import parse_replay
import json
import shutil
import os.path
import sys

skip = int(sys.argv[1])


# for ()
# download the html
# pages = replays_scraper.download_pages(100, cookies)

# scrape replay data from html
f = open("tank_replays.json", "r")
# print(f.read())
replays = json.loads(f.read())
tank_replays = []
# for page in pages:
# 	replays += replays_scraper.parse_page(page)
i = -1
for replay in replays:
  i = i + 1
  if skip > i:
    print("skip arg")
    continue
  
  print("do i", i)

  replay_id_hex = download_replay._get_hex_id(replay["id"])
  if os.path.isfile("results/" + replay_id_hex + ".json"):
    print("skip")
    continue

  files = download_replay.download_replay(replay["id"])

  data = parse_replay.parse_replay(files) # "replays/" + replay_id_hex)
  wf = open("results/" + replay_id_hex + ".json", 'w')
  wf.write(json.dumps(data, indent=4))
  wf.close()
   # shutil.rmtree("replays/" + replay_id_hex)
  # print()
    # print('ok')
# print(json.dumps(tank_replays, indent=4))
# download the files of the last replay
# download_replay.download_replay(replays[-1]["id"])

# get the hexadecimal id (= folder name)


# parse the replay
