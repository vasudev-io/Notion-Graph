import os
import time
from notion_client import Client

# Initialize Notion client with your integration token
notion = Client(auth="secret_37RsVuHNkIx573FXkg4geRqXcmiBSlBH45QxmVEXIQ9")

# ID of the database you want to monitor
database_id = "ed228bfa2ece43f0a34a0aa95985a501"

def check_for_updates():
    try:
        response = notion.databases.query(database_id)
        for page in response['results']:
            # Assuming there's a checkbox property named 'RunVSCode'
            if page['properties']['RunVSCode']['checkbox']:
                # Open VSCode and reset the checkbox
                os.system("code")
                notion.pages.update(
                    page['id'],
                    properties={
                        "RunVSCode": {"checkbox": False}
                    }
                )
    except Exception as e:
        print(f"Error: {e}")

# Poll the Notion database every 60 seconds
while True:
    check_for_updates()
    time.sleep(60)