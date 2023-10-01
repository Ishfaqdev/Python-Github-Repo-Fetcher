from github import Github

# Replace "YOUR_TOKEN" with your GitHub personal access token
token = "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"
g = Github(token)

# GitHub username of the user you want to showcase projects from
username = "waqasbcs"
user = g.get_user(username)

# Get the user's repositories
user_repos = user.get_repos()

# Filter and display Python projects
print(f"Python Projects by {username}:\n")
for repo in user_repos:
    if repo.language == "Python":
        print(f"Name: {repo.name}")
        print(f"URL: {repo.html_url}\n")
