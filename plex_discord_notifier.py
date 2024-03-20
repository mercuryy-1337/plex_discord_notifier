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

# Configuration for multiple users
user_configs = [
    {'username': '<username here>', 'password': '<password here>'},
    {'username': '<username here>', 'password': '<password here>'},
    # ... Add more users as needed
]

initial_watchlist = {} 

# Initialize watchlists for each user
for user_config in user_configs:
    account = MyPlexAccount(user_config['username'], user_config['password'])
    initial_watchlist[user_config['username']] = account.watchlist(sort='watchlistedAt') 

# Monitor for changes
print('Monitoring changes to watchlists...')
while True:
    for user_config in user_configs:
        account = MyPlexAccount(user_config['username'], user_config['password'])
        current_watchlist = account.watchlist(sort='watchlistedAt')

        # Compare to find new items
        new_item_titles = [item.title for item in current_watchlist if item.title not in [item.title for item in initial_watchlist[user_config['username']]]]

        for title in new_item_titles:
            print(f"New item added to {user_config['username']}'s watchlist: {title}")
            send_dc_notification(user_config['username'], title)

        # Update the initial watchlist for this user
        initial_watchlist[user_config['username']] = current_watchlist 

    time.sleep(30)  # Check every 20 seconds