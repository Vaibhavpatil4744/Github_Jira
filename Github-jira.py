# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://vaibhavpatil123.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF0ZkNCsK3sm0hXMe_iLw4M3WEakA-NEOwXk9qbnmoHF99IVfUbKTZw4Jy3jIUi633CWllQ74EqqIwXozIa_0_Qvaio3ZqWaWz1vX9w-MEkq9pCcGL65bEYQJndDz6j42WUb4G1rJpOA4B1NfQ21DfK17guW8OQfNV9bzvjR3KTu9U=D162D061"

    auth = HTTPBasicAuth("", API_TOKEN)

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
        "project": {
           "key": "AB"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
