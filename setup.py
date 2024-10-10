import os
import json
import time
import subprocess
import sys


print("By using our software you agree to the TOS in our Discord channel https://discord.gg/rYF5DFcfY2")
user_id = input("Please enter your Discord User ID: ")

# Save user ID to config.json
config_data = {
    "owner_id": user_id
}
with open("config.json", "w") as config_file:
    json.dump(config_data, config_file)

print("User ID saved to config.json")
time.sleep(2)


