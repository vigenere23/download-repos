import os
import subprocess
from pathlib import Path
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('--ref', metavar='refs/tags/TAG, refs/heads/BRANCH, SHA', help='Ref to clone.', default='refs/heads/main')
parser.add_argument('--repos', required=True, metavar='OWNER/REPO', help='Repos to clone.', nargs='*')
parser.add_argument('-o', '--output', required=True, metavar='DIR', help='Output dir.')
args = parser.parse_args()


GITHUB_TOKEN = os.getenv('CLONE_REPOS_GITHUB_TOKEN')


if not GITHUB_TOKEN:
    raise ValueError("Missing CLONE_REPOS_GITHUB_TOKEN environment variable.")


def get_download_link(repo_url: str) -> str:
    return f'https://github.com/{repo_url}/archive/{args.ref}.zip'


def get_org_name(repo_name: str) -> str:
    return repo_name.split('/')[0]


def execute(command: list):
    subprocess.run(command, shell=True, check=True)


def get_download_repo_command(url: str, output_path: str) -> list:
    return f"curl --location --fail --silent --show-error --output {output_path} --header 'Authorization: token {GITHUB_TOKEN}' {url}"


def main():
    output_dir = os.path.join(Path.cwd(), args.output)
    os.makedirs(output_dir, exist_ok=True)

    print(f'Downloading repos from ref {args.ref} to {output_dir}')

    for repo_name in args.repos:
        url = get_download_link(repo_name)
        org = get_org_name(repo_name)
        output_path = os.path.join(output_dir, f"{org}.zip")
        
        download_command = get_download_repo_command(url, output_path)

        try:
            print(f"\nDownloading repo '{repo_name}' from URL '{url}'")
            execute(download_command)
            print('Done')
        except Exception:
            print(f"Could not download repo '{repo_name}'")
            pass

if __name__ == '__main__':
    main()
