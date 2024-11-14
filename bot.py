
import os
import requests
from dotenv import load_dotenv
from trello_integration import create_trello_task
from monday_integration import create_monday_task

# Load environment variables
load_dotenv()

# Select which platform to use
def main():
    print("Welcome to Automated Task Management Bot")
    platform = input("Enter 'Trello' or 'Monday' to select the platform: ").strip().lower()

    if platform == "trello":
        board_id = input("Enter the Trello board ID: ")
        list_id = input("Enter the Trello list ID where tasks will be added: ")
        task_name = input("Enter the task name: ")
        description = input("Enter the task description: ")
        result = create_trello_task(board_id, list_id, task_name, description)
        print("Trello Task Created:", result)
        
    elif platform == "monday":
        board_id = input("Enter the Monday.com board ID: ")
        group_id = input("Enter the group ID where tasks will be added: ")
        task_name = input("Enter the task name: ")
        description = input("Enter the task description: ")
        result = create_monday_task(board_id, group_id, task_name, description)
        print("Monday Task Created:", result)
        
    else:
        print("Invalid platform selected. Please enter 'Trello' or 'Monday'.")

if __name__ == "__main__":
    main()
