import os


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TAG = os.getenv("TAG")


def get_url(repo_name):
    return f"https://github.com/glo2003/{repo_name}/archive/{TAG}.zip"


with open("repo-names.txt", 'r') as repo_names:
    for repo_name in repo_names.readlines():
        url = get_url(repo_name)
        os.system(f"wget --header='Authorization: token {GITHUB_TOKEN}' {url}")
