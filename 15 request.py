import requests

username = input("Enter GitHub username: ")

language = input("Enter programming language (e.g., Python): ")


url = f"https://api.github.com/users/{username}/repos"


response = requests.get(url)

if response.status_code == 200:
    user_repos = response.json()


    filtered_repos = [
        repo for repo in user_repos if repo["language"] == language]

    if len(filtered_repos) == 0:
        print(f"\nNo {language} projects found for {username}.\n")
    else:
        print(f"\n{language} Projects by {username}:\n")

        for repo in filtered_repos:
            print(f"Name: {repo['name']}")
            print(f"URL: {repo['html_url']}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
