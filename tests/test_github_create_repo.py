import json
import random
import requests
from test_data.repo_payload import Payloads


class TestGithubCreateRepo():

    # Create public repo from file
    def test_github_create_public_repo(self):
        url = 'https://api.github.com/orgs/{org}/repos'
        path_params = {'org' : 'org-ranjit-131'}
        headers = {'Authorization' : 'Bearer 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'}

        # Read the json file
        payload_file = open('/Users/ranjitprasad/Documents/TestAutomation/API_Automation/API_Automation_Framework/test_data/create_repo.json')
        # Extract the contents as json
        payload = json.load(payload_file)
        # Close the file
        payload_file.close()
        print('JSON Payload Before :', payload)

        # Generate a random number between 1 to 100000
        random_number = random.randrange(start=1, stop=100000)
        # Concatenate this random number with a "repo_" prefix Ex : repo_234567
        repo_name = f'repo_{random_number}'
        payload['name'] = repo_name
        print('JSON Payload After :', payload)

        response = requests.post(url=url.format(**path_params), headers=headers, json=payload)
        # Validate the status code to be 201
        assert response.status_code == 201
        # Validate repo name
        respone_body = response.json()
        assert respone_body['name'] == repo_name

    # Create private repo from class
    def test_github_create_private_repo(self):
        url = 'https://api.github.com/orgs/{org}/repos'
        path_params = {'org' : 'org-ranjit-131'}
        headers = {'Authorization' : 'Bearer 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'}

        payload = Payloads.get_repo_payload()
        print('JSON Payload Before :', payload)

        # Generate a random number between 1 to 100000
        random_number = random.randrange(start=1, stop=100000)
        # Concatenate this random number with a "repo_" prefix Ex : repo_234567
        repo_name = f'repo_{random_number}'
        payload['name'] = repo_name
        print('JSON Payload After :', payload)

        response = requests.post(url=url.format(**path_params), headers=headers, json=payload)
        # Validate the status code to be 201
        assert response.status_code == 201
        # Validate repo name
        response_body = response.json()
        assert  response_body['name'] == repo_name
