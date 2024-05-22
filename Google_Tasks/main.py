import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks"]

creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

def get_task_list():
  try:
      service = build("tasks", "v1", credentials=creds)

      # Call the Tasks API to get task lists
      results = service.tasklists().list(maxResults=10).execute()
      results_list = results.get("items", [])

      if not results_list:
          print("No task lists found.")
      task_lists = []
      for task_list in results_list:
          task_lists.append((task_list['title'],task_list['id']))
      return task_lists
  except HttpError as err:
      print(err)

def create_task():
    try:
        service = build("tasks", "v1", credentials=creds)
    except Exception as i:
        print(f"{i}")

    task_list = get_task_list()
    for name,id in task_list:
        if name.title() == "Faculty":
            with open("tasks.json",encoding='utf-8') as outfile:
                a = json.load(outfile)
                for i,item in enumerate(a):
                    print(item)
                    created_task = service.tasks().insert(tasklist=id, body=item).execute()
                    print(created_task)
create_task()
