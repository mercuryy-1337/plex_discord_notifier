import requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
import time

# plex and discord parameters 
PLEX_URL = 'http://localhost:32400/' #default plex url when running the script locally, can be changed though
PLEX_TOKEN = '<plex token>'  
DISCORD_WEBHOOK = '<webhook url>'  # Discord webhook url

def send_dc_notification(username, title):
    """Sends a notification to the configured Discord webhook"""
    data = {
        "content": f"**{username}** added **{title}** to their watchlist!"
    }
    requests.post(DISCORD_WEBHOOK, json=data)

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)
account = MyPlexAccount('<Username>','<Password>') 

initial_watchlist = account.watchlist(sort='watchlistedAt') # retrieve user's watchlist, sorted by the most recently added item

# Printing the most recently added item just to test something
if initial_watchlist:
    print(initial_watchlist[-1])
else:
    print('watchlist is empty')

# Monitor for changes
while True:
    current_watchlist = account.watchlist(sort='watchlistedAt')

    # Compare to find new items
    new_item_titles = [item.title for item in current_watchlist if item.title not in [item.title for item in initial_watchlist]]

    for title in new_item_titles:
        print(f"New item added to watchlist: {title}")
        send_dc_notification(account.username, title)

    # Update the initial watchlist
    initial_watchlist = current_watchlist 

    time.sleep(30)  # Check every 30 seconds
