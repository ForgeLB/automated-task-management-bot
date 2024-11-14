
import os
import requests
from dotenv import load_dotenv

load_dotenv()

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")

def create_monday_task(board_id, group_id, name, desc):
    url = "https://api.monday.com/v2"
    headers = {
        "Authorization": MONDAY_API_KEY
    }
    query = f'''
        mutation {{
            create_item (
                board_id: {board_id},
                group_id: "{group_id}",
                item_name: "{name}",
                column_values: "{{\\"text\\": \\"{desc}\\"}}"
            ) {{
                id
            }}
        }}
    '''
    
    response = requests.post(url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None
