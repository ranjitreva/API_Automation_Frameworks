import requests


class TestGithubGetRepo:

    # Test Scenario 1 - Get a valid public repo without token
    def test_get_public_repo_without_token(self):
        url = 'https://api.github.com/repos/{owner}/{repo}'
        path_params = {'owner': 'org-ranjit-131', 'repo': 'repo_may_14_05'}  # Use repo public not private
        response = requests.get(url=url.format(**path_params))
        # Validate the status code to be 200
        assert response.status_code == 200
        # Extract the response body
        response_body = response.json()
        # Validate name and owner
        actual_name = response_body['name']
        assert actual_name == 'repo_may_14_05'
        assert response_body['owner']['login'] == 'org-ranjit-131'


    # Test Scenario 2 - Get a valid public repo with token
    def test_get_public_repo_with_token(self):
        url = 'https://api.github.com/repos/{owner}/{repo}'
        path_params = {'owner': 'org-ranjit-131', 'repo': 'repo_may_14_05'}  # Use repo public not private
        headers = {'Authorization' : 'Bearer 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'}  # Add Bearer before the token
        response = requests.get(url=url.format(**path_params, headers=headers))
        # Assert the status code to be 200
        assert response.status_code == 200
        # Extract the response body
        response_body = response.json()
        # Validate name and owner
        actual_name = response_body['name']
        assert actual_name == 'repo_may_14_05'
        assert response_body['owner']['login'] == 'org-ranjit-131'


    # Test Scenario 3 - Get a valid public repo invalid owner without token
    def test_get_public_repo_invalid_owner_without_token(self):
        url = 'https://api.github.com/repos/{owner}/{repo}'
        path_params = {'owner': 'org-ranjit-1311', 'repo': 'repo_may_14_05'}  # Use repo public not private, Give the wrong org_name
        response = requests.get(url=url.format(**path_params))
        # Assert the status code to be 404
        assert response.status_code == 404
        # Extract the response body
        response_body = response.json()
        # Validate error response
        assert response_body['message'] == 'Not Found'
