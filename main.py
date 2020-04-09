import sys

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]
    response = requests.get(f"https://api.github.com/users/{username}/events")

    if response.status_code == 200:
        content = response.json()
        print(content[0]["created_at"])
    else:
        print(f"{response.status_code} - {response.json()['message']}")

