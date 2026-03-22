import allure
import pytest
from tests.base_class import BaseClass
from utils.api_helper import DELETE


@allure.parent_suite('GitHub Repository Functionality')
@allure.suite('GitHub Delete Repo Suite')
@allure.sub_suite('GitHub Delete Repo Scenarios')
class TestGitHubDeleteRepo(BaseClass):
    """
    This class contains all test cases related to delete an organization repository of the GitHub
    """

    # sessions_object = sessions.BaseUrlSession(base_url='https://api.github.com')
    url = '/repos/{owner}/{repo}'
    valid_owner = 'org-ranjit-131'
    valid_token = 'Bearer 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'

    @allure.title('Delete valid public repo with token')
    @allure.severity(severity_level=allure.severity_level.BLOCKER)
    @allure.testcase(url="", name="TC-0005")
    @pytest.mark.smoke
    def test_delete_public_repo_with_token(self):
        """
        Delete valid public repo with token
        """
        path_params = {'owner': self.valid_owner, 'repo': 'repo_61430'}
        headers = {'Authorization': self.valid_token}
        response = DELETE(sessions_object=self.sessions_object, url=self.url.format(**path_params), headers=headers)
        # Validate the status code to be 204
        assert response.status_code == 204
