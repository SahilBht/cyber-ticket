import json

with open("service_request_data.json", "r") as f:
    data = json.load(f)

import requests
from requests.auth import HTTPBasicAuth

issues = {
    "change": 10005,
	"Incident": 10001,
	"Post-incident review": 10002,
	"Problem": 10006,
	"Service request": 10003,
	"Service request with approvals": 10004,
	"Task": 10007,
	"Sub-task": 10008
}

# Replace these with your Jira server details
jira_url = "https://sahilbht.atlassian.net/rest/api/2/issue"


# Get user input
username = data["name"]
password = data["api_token"]

# Data for the new issue
summary = data["subject"]
description = data["description"]

issue_type_id = issues[data["issue"]]


# Data for the new issue
issue_data = {
    "fields": {
        "project": {"key": "XS"},
        "summary": summary,
        "description": description,
        "issuetype": {"id": issue_type_id},  # Change this to the appropriate issue type
    }
}

# Make the API request
response = requests.post(
    jira_url,
    json=issue_data,
    auth=HTTPBasicAuth(username, password),
    headers={"Content-Type": "application/json"},
)

# Check the response
if response.status_code == 201:
    print("Issue created successfully!")
    issue_key = response.json()["key"]
    print(f"Issue key: {issue_key}")
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.text)

# ATATT3xFfGF0vls896K0Qw9tO8Iwio_vI6EFyBmOHN7zrcSfQkbo1dzvrAo1cvsCpG1GH1ekFIo57gb8lrbsQdqucrXsaC5FXfpNhoz9mawSSHcPcusvf_SO26GRsFRV_Ym5OHJrqDMjbQw0ZL9Oz4-KDMjJLUq3Ma14j92_qUYR9KJPC_Qt9Zs=D4CCC68F