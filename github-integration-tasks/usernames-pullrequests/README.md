### Python Script that fetches the list of open full requests from a GitHub repository using the GitHub API, checks for errors, and prints the usernames of all users who have created pull requests.

For demo purposes, I have taken the Kubernetes official GitHub repository.

Below is the step-by-step explanation for the code:

```bash
import requests # Fetching pull requests from GitHub API
```

- This line imports the "requests" library, which is a popular Python package for making HTTP requests (like GET, POST, etc.) to web servers and APIs.

```bash
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls" # URL to fetch pull requests from the Kubernetes repository
```

- This sets the variable "url" to the GitHub API endpoint for listing pull requests in the kubernetes/kubernetes repository.
- The endpoint returns a JSON array, where each element represents a pull request.

```bash
response = requests.get(url) # Sending a GET request to the URL
```

- This sends an HTTP GET request to the specified URL using the requests library.
- The result is stored in the "response" object, which contains the server’s reply, including status code and data.

```bash
if response.status_code != 200: # Checking if the request was successful
    print("Failed to retrieve pull requests")
    exit()
```

- This checks if the HTTP status code of the response is not 200 (which means "OK" or success).
- If the status code is not 200, it prints an error message and exits the program.

```bash
output = response.json() # Parsing the JSON response
```

- This parses the response body as JSON and stores it in the variable output.
- "output" will be a list of dictionaries, each representing a pull request.

  ```bash
  if not output: # Checking if there are no pull requests
    print("No pull requests found")
    exit()
  ```

- This checks if the output list is empty (i.e., there are no pull requests).
- If empty, it prints a message and exits the program.

```bash
for i in range(len(output)): # Iterating through the list of pull requests
    print(output[i]['user']['login']) # Printing the username of the user who created the pull request
```

- This loops through each pull request in the output list using its index.
- For each pull request, it accesses the user field (which is a dictionary) and then the login field inside user, which contains the GitHub username of the person who created the pull request.
- It prints the username for each pull request.

## Summary:
This script fetches the list of open pull requests from the Kubernetes GitHub repository using the GitHub API, checks for errors, and prints the usernames of all users who have created pull requests.
