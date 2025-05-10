import requests
import os
import json

# Configuration
REPO = "satyamecom/my-website"
BRANCH = "main"
LAST_COMMIT_FILE = "/home/ubuntu/last_commit.txt"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") 

def get_latest_commit():
    url = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["sha"]

def read_last_commit():
    if not os.path.exists(LAST_COMMIT_FILE):
        return None
    with open(LAST_COMMIT_FILE, 'r') as f:
        return f.read().strip()

def write_last_commit(sha):
    with open(LAST_COMMIT_FILE, 'w') as f:
        f.write(sha)

def main():
    latest_commit = get_latest_commit()
    last_commit = read_last_commit()

    if latest_commit != last_commit:
        print("New commit found. Deploying...")
        os.system("/home/ubuntu/deploy_code.sh")
        write_last_commit(latest_commit)
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()
