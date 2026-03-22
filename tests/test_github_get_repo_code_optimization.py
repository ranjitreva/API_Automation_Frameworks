import allure
import pytest
from requests_toolbelt import sessions
from string_constants import MiscellaneousStringConstants
from tests.base_class import BaseClass
from utils.api_helper import GET

@allure.parent_suite('GitHub Repository Functionality')
@allure.suite('Github Get Repo Suite')
@allure.sub_suite('Github Get Repo Scenarios')
class TestGithubGetRepo(BaseClass):
    """
    This class contains all test cases related to Get a repository of the GitHub
    """

    # sessions_object = sessions.BaseUrlSession(base_url='https://api.github.com')
    url = '/repos/{owner}/{repo}'
    valid_owner = 'org-ranjit-131'
    valid_repo = 'repo_may_14_05'
    valid_token = 'Bearer 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'

    @allure.title('Get valid public repo without token')
    @allure.severity(severity_level=allure.severity_level.BLOCKER)
    @allure.testcase(url='', name='TC-00001')
    @pytest.mark.smoke
    @pytest.mark.p2
    def test_get_public_repo_without_token(self):
        """
        Test Scenario 1 - Get a valid public repo without token
        """
        path_params = {MiscellaneousStringConstants.OWNER : self.valid_owner, MiscellaneousStringConstants.REPO : self.valid_repo}  # Use repo public not private
        # response = self.sessions_object.get(url=self.url.format(**path_params))
        response = GET(sessions_object=self.sessions_object, url=self.url.format(**path_params), headers=None)
        # Assert the status code to be 200
        assert response.status_code == 200
        # Extract the response body
        response_body = response.json()
        # Validate name and owner
        actual_name = response_body['name']
        assert actual_name == self.valid_repo
        assert response_body['owner']['login'] == self.valid_owner

    @pytest.mark.p2
    def test_get_public_repo_with_token(self):
        """
        Test Scenario 2 - Get a valid public repo with token
        """
        path_params = {MiscellaneousStringConstants.OWNER : self.valid_owner, MiscellaneousStringConstants.REPO : self.valid_repo}  # Use repo public not private
        headers = {MiscellaneousStringConstants.AUTHORIZATION : self.valid_token}  # Add Bearer before the token
        # response = self.sessions_object.get(url=self.url.format(**path_params), headers=headers)
        response = GET(sessions_object=self.sessions_object, url=self.url.format(**path_params), headers=headers)
        # Validate the status code to be 200
        assert response.status_code == 200
        # Extract the response body
        response_body = response.json()
        # Validate name and owner
        actual_name = response_body['name']
        assert actual_name == self.valid_repo
        assert response_body['owner']['login'] == self.valid_owner


    @allure.title('Get valid public repo invalid owner without token')
    @allure.severity(severity_level=allure.severity_level.MINOR)
    @allure.issue(url='', name='Bug-000012')
    @allure.tag('Smoke Scenario')
    @pytest.mark.smoke
    def test_get_public_repo_invalid_owner_without_token(self):
        """
        Test Scenario 3 - Get a valid public repo invalid owner without token
        """
        path_params = {'owner': 'org-ranjit-1311', MiscellaneousStringConstants.REPO : self.valid_repo}  # Use repo public not private, Give the wrong org_name
        # response = self.sessions_object.get(url=self.url.format(**path_params))
        response = GET(sessions_object=self.sessions_object, url=self.url.format(**path_params), headers=None)
        # Assert the status code to be 404
        assert response.status_code == 404
        # Extract the response body
        response_body = response.json()
        # Validate error response
        assert response_body['message'] == 'Not Found'
