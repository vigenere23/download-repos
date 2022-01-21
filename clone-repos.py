import os
import subprocess
from pathlib import Path
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-b', '--branch', metavar='<branch or tag>', help='Branch to clone', default='main')
args = parser.parse_args()


GITHUB_TOKEN = os.getenv('CLONE_REPOS_GITHUB_TOKEN')


if not GITHUB_TOKEN:
    raise ValueError("Missing CLONE_REPOS_GITHUB_TOKEN environment variable.")


def get_repo_url(repo_name: str) -> str:
    return f'https://github.com/glo2003/{repo_name}/archive/{args.branch}.zip'


def get_download_link(repo_url: str) -> str:
    return f'https://github.com/{repo_url}/archive/{args.branch}.zip'


def get_org_name(repo_name: str) -> str:
    return repo_name.split('/')[0]


def execute(command: list):
    subprocess.run(command, shell=True, check=True)


def get_download_repo_command(url: str, output_path: str) -> list:
    return f"curl --location --fail --silent --show-error --output {output_path} --header 'Authorization: token {GITHUB_TOKEN}' {url}"


def get_unzip_command(zip_path: str):
    return f'unzip -q -o {zip_path} -d projects'


def main():
    output_dir = os.path.join(Path.cwd(), 'projects')
    os.makedirs(output_dir, exist_ok=True)

    print(f'Downloading repos from branch {args.branch}')

    with open('repo-urls.txt', 'r') as repo_names:
        for repo_name in repo_names.read().splitlines():
            url = get_download_link(repo_name)
            org = get_org_name(repo_name)
            output_path = os.path.join(output_dir, f"{org}.zip")
            
            download_command = get_download_repo_command(url, output_path)
            # unzip_command = get_unzip_command(output_path)

            try:
                print(f"\nDownloading repo '{repo_name}'")
                execute(download_command)
                # print(f"Unzipping {output_path} to ./projects")
                # execute(unzip_command)
                print('Done')
            except Exception as e:
                print(f'Could not download this repo')
                pass

if __name__ == '__main__':
    main()
