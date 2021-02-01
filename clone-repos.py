import os
import subprocess


BRANCH = os.getenv('BRANCH') or 'main'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


def get_repo_url(repo_name: str) -> str:
    return f'https://github.com/glo2003/{repo_name}/archive/{BRANCH}.zip'


def execute(command: list):
    subprocess.run(command, shell=True, check=True)


def get_download_repo_command(url: str, output_path: str) -> list:
    return f'curl -L -G --silent --fail --show-error -H "Authorization: token {GITHUB_TOKEN}" -o {output_path} {url}'


def get_unzip_command(zip_path: str):
    return f'unzip -q -o {zip_path} -d projects'


with open('repo-names.txt', 'r') as repo_names:
    for repo_name in repo_names.read().splitlines():
        url = get_repo_url(repo_name)
        output_path = f"{repo_name}.zip"
        download_command = get_download_repo_command(url, output_path)
        unzip_command = get_unzip_command(output_path)

        try:
            print(f"\nDownloading repo '{repo_name}/{BRANCH}'")
            execute(download_command)
            # print(f"Unzipping {output_path} to ./projects")
            # execute(unzip_command)
            print('Done')
        except Exception as e:
            pass
