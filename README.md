# plex_discord_notifier

A Python script that automatically sends Discord notifications whenever new items are added to your Plex watchlist.

## Requirements

- Python 3
- The requests library (install with `pip install requests`)
- The plexapi library (install with `pip install plexapi`)
- A Plex Media Server
- A Discord webhook

## Setup

1. Get your Plex Token: Instructions can be found on Plex's support site: [Finding an Authentication Token (X-Plex-Token)](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)
2. Create a Discord Webhook: Instructions are available on Discord's support site: [Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
3. Edit the script:
   - Replace `<plex token>` with your actual Plex token.
   - Replace `<webhook url>` with your Discord webhook URL.
   - Replace `<Username>` and `<Password>` with your Plex account credentials.

## Usage

1. Make sure your Plex Media Server is running.
2. Run the script: `python plex_watchlist_notifier.py`

## How it Works

- The script connects to your Plex Media Server using your Plex token.
- It retrieves your initial watchlist.
- The script enters a loop:
  - It periodically fetches an updated version of your watchlist.
  - It compares the updated watchlist to the previous version to identify newly added items.
  - For each new item, it sends a notification to your Discord channel via the webhook.

## Customization

- You can change the `PLEX_URL` if your Plex server isn't running locally.
- You can adjust the `time.sleep(30)` value to control how frequently the script checks for changes.
