import json
import random
import allure
import pytest
from requests_toolbelt import sessions
from test_data.repo_payload import Payloads
from tests.base_class import BaseClass
from utils.api_helper import POST
from utils.generic_utils import get_random_repo_name


@allure.parent_suite('GitHub Repository Functionality')
@allure.suite('GitHub Create Repo')
@allure.sub_suite('GitHub Create Repo Scenario')
class TestGithubCreateRepo(BaseClass):
    """
    This class contains all test cases related to create an organization repository of the GitHub
    """

    # sessions_object = sessions.BaseUrlSession(base_url='https://api.github.com')
    url = '/orgs/{org}/repos'
    org = 'org-ranjit-131'
    valid_token = 'Bearer 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'

    @allure.tag('Smoke Scenario')
    @pytest.mark.smoke
    def test_github_create_public_repo(self):
        """
        Create public repo from file
        """
        path_params = {'org' : self.org}
        headers = {'Authorization' : self.valid_token}

        # Read the json file
        payload_file = open('/Users/ranjitprasad/Documents/TestAutomation/API_Automation/API_Automation_Framework/test_data/create_repo.json')
        # Extract the contents as json
        payload = json.load(payload_file)
        # Close the file
        payload_file.close()
        print('JSON Payload Before : ', payload)

        # Util function to get a random repo name
        repo_name = get_random_repo_name()
        payload['name'] = repo_name
        print('JSON Payload After : ', payload)

        # response = self.sessions_object.post(url=self.url.format(**path_params), headers=headers, json=payload)
        response = POST(sessions_object=self.sessions_object, url=self.url.format(**path_params), headers=headers, payload=payload)
        # Validate the status code to be 201
        assert response.status_code == 201
        # Validate repo name
        response_body = response.json()
        assert response_body['name'] == repo_name

    @pytest.mark.p1
    def test_github_create_private_repo(self):
        """
        Create private repo from class
        """
        path_params = {'org' : self.org}
        headers = {'Authorization' : self.valid_token}

        payload = Payloads.get_repo_payload()
        print('JSON Payload Before :', payload)

        # Util function to get a random repo name
        repo_name = get_random_repo_name()
        payload['name'] = repo_name
        print('JSON Payload After :', payload)

        # response = self.sessions_object.post(url=self.url.format(**path_params), headers=headers, json=payload)
        response = POST(sessions_object=self.sessions_object, url=self.url.format(**path_params), headers=headers, payload=payload)
        # Validate the status code to be 201
        assert response.status_code == 201
        # Validate repo name
        response_body = response.json()
        assert response_body['name'] == repo_name
