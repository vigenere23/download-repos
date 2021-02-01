import os
import subprocess


BRANCH = os.getenv("BRANCH")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_repo_url(repo_name: str) -> str:
    return f"https://github.com/glo2003/{repo_name}/archive/{BRANCH}.zip"


def execute(command: list):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = proc.communicate()

    if stderr is not None:
        raise Exception(stderr)

    return stdout


def download_repo_command(url: str, output_path: str) -> list:
    return ['wget', '-L', f'--header=\"Authorization: token {GITHUB_TOKEN}\"', '-O', output_path, url]


with open("repo-names.txt", 'r') as repo_names:
    for repo_name in repo_names.read().splitlines():
        url = get_repo_url(repo_name)
        output_path = f"{repo_name}.zip"
        command = download_repo_command(url, output_path)

        try:
            print(f"\nDownloading repo '{repo_name}/{BRANCH}'")
            print(execute(command))
            print(f"Done")
        except Exception as e:
            print(f"Could not get repo '{repo_name}/{BRANCH}'")
            print(e)
            os.remove(output_path)
