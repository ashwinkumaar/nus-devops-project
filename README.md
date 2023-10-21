# GitHub Action Workflow Documentation: Get Data from API and Create File

This GitHub Action workflow retrieves data from a specified API endpoint and saves it as both a JSON file and an HTML file in the main branch of the repository.


## Workflow Steps:

Checkout repository: Checks out the repository to provide the necessary context for subsequent operations.

Get data from API and create files:
Retrieves data from the specified API endpoint using the curl command.
Saves the data as a JSON file and converts it into an HTML format for improved readability.
Commits both the JSON and HTML files to the main branch automatically.

## Prerequisites:
Ensure the designated API endpoint is accessible and provides valid JSON data.
Verify that the stefanzweifel/git-auto-commit-action GitHub Action is configured for automated commits to the repository.

## Outcome:
Facilitates the retrieval and storage of API data in both JSON and HTML formats for better accessibility and readability.
Automates the process of committing the generated files to the main branch, ensuring efficient version control and management.
