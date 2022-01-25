'''
Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

'''

import requests
import datetime as dt
import csv


# --- Paste token here
token = ''


# --- Get list of Meeting IDs
def get_list_of_meeting_ids(_token):
    url1 = "https://webexapis.com/v1/meetings?meetingType=meeting"
    headers1 = {'Authorization': f'Bearer {_token}'}
    response_meeting_ids = requests.request("GET", url1, headers=headers1, data="")
    if response_meeting_ids.status_code == 200:
        return response_meeting_ids.json()
    elif response_meeting_ids.status_code == 401:
        return "Status 401 - Wrong Token"


# print(get_list_of_meeting_ids(token))


# --- Generates list of Meeting IDs
list_of_meetings = []
response1 = get_list_of_meeting_ids(token)
if response1 != "Status 401 - Wrong Token":
    for meeting_id in response1['items']:
        print(meeting_id['id'])
        list_of_meetings.append(meeting_id['id'])
print(f'List of Meetings: {list_of_meetings}')


# --- Gets the user information from each meeting
def get_os(_meeting_id, _token):
    url2 = f"https://analytics.webexapis.com/v1/meeting/qualities?meetingId={_meeting_id}"
    headers2 = {'Authorization': f'Bearer {_token}'}
    response_get_os = requests.request("GET", url2, headers=headers2, data="", verify=False)
    if response_get_os.status_code == 200:
        return response_get_os.json()
    elif response_get_os.status_code == 429:
        return 429
    elif response_get_os.status_code == 500:
        return 500
    else:
        return "Error"


# --- Generates the .csv report
with open(f'Meeting_Report_{dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv', 'w', newline='') as f:
    writer = csv.writer((f))
    writer.writerow(['Meeting ID', 'User Name', 'User Email', 'OS Type', 'OS Version'])
    for meeting_id in list_of_meetings:
        meeting_information = get_os(meeting_id, token)
        if meeting_information != 429 and meeting_information != "Error" and meeting_information != 500:
            # print(meeting_information)
            print('Processing Meeting')
            for user in meeting_information['items']:
                # print(user)
                writer.writerow(([user['meetingInstanceId'], user['webexUserName'], user['webexUserEmail'], user['osType'], user['osVersion']]))
                # print(f'Information for Meeting ID: {meeting_id}')
        elif meeting_information == 429:
            print("Try again after 5 minutes")
            writer.writerow(['API Call Error'])
        elif meeting_information == 500:
            print("Certificate Error")
            writer.writerow(['API Call Error - Type 500'])
        elif meeting_information == "Error":
            print("Error")
        else:
            pass