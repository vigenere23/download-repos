# Clone repos

A simple script to clone repos.

## Important notice

The attached Github Actions workflow will **not** work directly in the organization. You will need to fork it to your personal account first, or run it locally.

## Setup

1. Make sure to fill the `repo-urls.txt` file with the repos you want to download. 
2. Create a Personal Access Token with at least read access.
3. Create an environment variable `GITHUB_TOKEN` with your PAT as value.
4. Make sure to have Python 3 installed

### Running

```
python clone-repos.py -b <branch or tag>
```

### Github actions

**Make sure to call your PAT `PERSONAL_TOKEN`.**

A Github Action workflow is available to quickly download zipped repos (instead of relying on your slow Internet connection). Simply go to Actions, then select the `Clone repos` action and manually trigger it. Make sure to enter the right branch/tag name.
