import os


BRANCH = os.getenv("BRANCH")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_url(repo_name):
    return f"https://{GITHUB_TOKEN}@github.com/glo2003/{repo_name}/archive/{BRANCH}.zip"


with open("repo-names.txt", 'r') as repo_names:
    for repo_name in repo_names.read().splitlines():
        url = get_url(repo_name)
        output_path = f"{repo_name}.zip"

        try:
            os.system(f"wget -L -O {output_path} {url} || rm -f {output_path}")
        except Exception:
            pass
