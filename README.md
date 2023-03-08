# Download repos action

A simple Github Action to bulk-download repos.

## Usage

```yaml
name: Run

on:
  # If using the action with a manual dispatched workflow in another repo
  workflow_dispatch:
    inputs:
      ref:
        description: Ref (refs/heads/BRANCH, refs/tags/TAG, SHA)
        required: true
        default: refs/branch/main

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      # If listing repo URLs in a txt file, else just use a space-delimited list when calling the action
      - id: preparation
        run: echo "repos=$(cat repos.txt | tr '\n' ' ')" >> $GITHUB_OUTPUT

      - uses: vigenere23/download-repos@main
        with:
          output-dir: repos
          repos: ${{ steps.preparation.outputs.repos }}
          access-token: ${{ secrets.PAT }}
          ref: ${{ github.event.inputs.ref }}

      # If you want to download them locally
      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: repos
          path: repos # Must match the "output-dir" input
```
