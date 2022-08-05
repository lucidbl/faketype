import requests
import time

zyzz = {"authorization": "token"}

channel_id = input("Channel ID: ")

while True:
    faketype = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/typing", headers = zyzz)
    time.sleep(2.5)
    print(faketype)
