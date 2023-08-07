import requests

api_key = "3c272c2c7b3c6ebbc2c6d06971c3813e72c11a25"
headers = {"Authorization": f"W-Token {api_key}"}
endpoint_url = "https://api.wheniwork.com/2/users"

# Make the GET request
response = requests.get(endpoint_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Process the data as needed
    print(data)
else:
    print("Error: Request failed with status code", response.status_code)
    print(' dont know whats happening')
    
