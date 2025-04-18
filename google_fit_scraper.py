import os
import pandas as pd
import time
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/fitness.activity.read"]

now = int(time.time() * 1000)  # current time
start_time = now - 7 * 86400000 # week ago

def get_google_fit_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("fitness", "v1", credentials=creds)

def fetch_steps():
    service = get_google_fit_service()
    data_source = "derived:com.google.step_count.cumulative:com.google.android.gms:merge_step_deltas"    
    
    start_time_millis = int(pd.Timestamp.now().floor("D").timestamp() * 1000) - 7 * 86400000
    end_time_millis = int(pd.Timestamp.now().timestamp() * 1000)

    request = service.users().dataset().aggregate(
        userId="me",
        body={
            "aggregateBy": [{"dataTypeName": "com.google.step_count.delta"}],
            "bucketByTime": {"durationMillis": 86400000},  # breakdown by day
            "startTimeMillis": start_time_millis,
            "endTimeMillis": end_time_millis,
        },
    )
    response = request.execute()

    for dataset in response['bucket']:
        for point in dataset['dataset'][0]['point']:
            if 'intVal' in point['value'][0]:
                 steps = point['value'][0]['intVal']  # steps
        else:
            steps = 0  # if there are no steps

    steps_data = []
    for bucket in response.get("bucket", []):
        date = pd.to_datetime(int(bucket["startTimeMillis"]) / 1000, unit="s").date()
        steps = bucket.get("dataset", [])[0].get("point", [])
        step_count = sum(int(point["value"][0]["intVal"]) for point in steps) if steps else 0
        steps_data.append({"Date": date, "Steps": step_count})

    return pd.DataFrame(steps_data)

# Requesting steps and saving
df_steps = fetch_steps()
df_steps.to_csv("google_fit_steps.csv", index=False)
df_steps.to_excel("google_fit_steps.xlsx", index=False, engine="openpyxl")
print("The step data is saved!")
print(df_steps.head())
