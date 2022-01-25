# GVE_Devnet_WebexMeetingsParticipantOS
Python script that creates a report containing a list of participants per meeting and the OS that each participant is using to join the meeting. 


## Contacts
* Max Acquatella
* Gerardo Chaves

## Solution Components
* Webex Meetings
* Python

## Requirements
Cisco Webex Administrator Token (can be the temporary token obtained from https://developer.webex.com/docs/getting-started)


## Installation/Configuration
Install python 3.6 or later

Set up a virtual environment (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Install requirements.txt

Main script: main.py

## Usage

Run main.py from your command line:

```
python3 main.py
```

The code should generate a .csv file in the same project folder. This file will contain information similar to this: 

![/IMAGES/image1.png](/IMAGES/image1.png)


## Limitations
The script makes use of the following webex API endpoint:

```html
https://analytics.webexapis.com/v1/meeting/qualities
```

Please see more here: 
 
https://developer.webex.com/docs/api/v1/meeting-qualities

This endpoint has a 5 min rate limit interval, which might throw a 429 error if run multiple times. 
This code should signal if the 5 min interval has been reached. 

Also, the report will cover the past 7 days of meetings for the given organization. 


# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.