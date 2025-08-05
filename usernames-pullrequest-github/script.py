import requests # Fetching pull requests from GitHub API

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls" # URL to fetch pull requests from the Kubernetes repository

response = requests.get(url) # Sending a GET request to the URL
if response.status_code != 200: # Checking if the request was successful
    print("Failed to retrieve pull requests")
    exit()

output = response.json() # Parsing the JSON response
if not output: # Checking if there are no pull requests
    print("No pull requests found")
    exit()

for i in range(len(output)): # Iterating through the list of pull requests
    print(output[i]['user']['login']) # Printing the username of the user who created the pull request
