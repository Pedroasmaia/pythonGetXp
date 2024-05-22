import os.path
import pprint as pp
from datetime import datetime,timezone,timedelta
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

tasks_list = get_task_list()

def get_tasks_of_today(tasks_list):
    now = datetime.now(timezone.utc)
    now = str(now.strftime("%Y-%m-%d"))
    try:
        service = build("tasks","v1",credentials=creds)
    except Exception as err:
        print(err)
    for name,id in tasks_list:
        try:
          tasks = service.tasks().list(tasklist=id,showCompleted=False).execute()
          now = '2024-06-15'
          for task in tasks['items']:
            # print(task['due'][:10])
            if task['due'][:10] == now:
              print(task['title'])
              print(task['status'])
        except Exception as i:
            print(i)
get_tasks_of_today(tasks_list)