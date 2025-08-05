# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("example@domain.com", "<API_Token>")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Order entry fails when selecting supplier.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10000"
    },
    "project": {
      "key": "<>"
    },
    "reporter": {
      "id": "<>"
    },
    "summary": "Main order flow broken"
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
