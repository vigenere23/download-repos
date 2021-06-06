import os
import subprocess
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-b --branch', metavar='<branch or tag>', help='Branch to clone', default='main')
args = parser.parse_args()


GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


def get_repo_url(repo_name: str) -> str:
    return f'https://github.com/glo2003/{repo_name}/archive/{args.branch}.zip'


def get_download_link(repo_url: str) -> str:
    return f'https://github.com/{repo_url}/archive/{args.branch}.zip'


def get_org_name(repo_name: str) -> str:
    return repo_name.split('/')[0]


def execute(command: list):
    subprocess.run(command, shell=True, check=True)


def get_download_repo_command(url: str, output_path: str) -> list:
    return f'curl -L -G --silent --fail --show-error -H "Authorization: token {GITHUB_TOKEN}" -o {output_path} {url}'


def get_unzip_command(zip_path: str):
    return f'unzip -q -o {zip_path} -d projects'


with open('repo-urls.txt', 'r') as repo_names:
    for repo_name in repo_names.read().splitlines():
        url = get_download_link(repo_name)
        org = get_org_name(repo_name)
        output_path = f"{org}.zip"
        download_command = get_download_repo_command(url, output_path)
        # unzip_command = get_unzip_command(output_path)

        try:
            print(f"\nDownloading repo '{repo_name}/{args.branch}'")
            execute(download_command)
            # print(f"Unzipping {output_path} to ./projects")
            # execute(unzip_command)
            print('Done')
        except Exception as e:
            pass
