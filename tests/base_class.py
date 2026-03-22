import configparser
import os.path
import pytest
from requests_toolbelt import sessions


class BaseClass:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        config_object = configparser.ConfigParser()
        # Fetch current file directory [API_Automation_Framework/tests]
        current_path = os.path.dirname(__file__)
        print('CURRENT PATH : ', current_path)

        # Move one level above to the framework folder [API_Automation_Framework]
        project_path = current_path + '/..'
        print('PROJECT PATH : ', project_path)

        # Now the current directory is the framework project path. Concatenate the config.ini to the project path
        config_object.read(project_path + '/config.ini')

        env = config_object.get('Global', 'ENV')
        baseurl = config_object.get(env, 'BASE_URL')
        print('Base URL : ' , baseurl)

        # self.sessions_object = sessions.BaseUrlSession(base_url='https://api.github.com')
        self.sessions_object = sessions.BaseUrlSession(base_url=baseurl)
