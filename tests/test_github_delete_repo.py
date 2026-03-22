import requests


class TestGithubDeleteRepo():

    # Test Scenario 1 - Delete public repo with token
    def test_delete_public_repo_with_token(self):
        url = ' https://api.github.com/repos/{owner}/{repo}'
        path_params = {'owner': 'org-ranjit-131', 'repo': 'repo_733785'}
        headers = {'Authorization': 'Bearer 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'}

        response = requests.delete(url=url.format(**path_params), headers=headers)

        print('Response Status Code :', response.status_code)
        # Validate the status code to be 204
        assert response.status_code == 204
