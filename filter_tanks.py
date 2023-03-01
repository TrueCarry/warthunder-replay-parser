import replays_scraper
import download_replay
import parse_replay
import json


# for ()
# download the html
# pages = replays_scraper.download_pages(100, cookies)

# scrape replay data from html
f = open("replays.json", "r")
# print(f.read())
replays = json.loads(f.read())
tank_replays = []
# for page in pages:
# 	replays += replays_scraper.parse_page(page)
for replay in replays:
  if replay['gamemode'] == 'Realistic battles' and replay['vehicles'] == 'Tank' :
    tank_replays.append(replay)
    # print('ok')
# print(json.dumps(tank_replays, indent=4))
wf = open("tank_replays.json", 'w')
wf.write(json.dumps(tank_replays, indent=4))
wf.close()

# download the files of the last replay
# download_replay.download_replay(replays[-1]["id"])

# get the hexadecimal id (= folder name)
# replay_id_hex = download_replay._get_hex_id(replays[-1]["id"])

# parse the replay
# print(parse_replay.parse_replay("replays/" + replay_id_hex))