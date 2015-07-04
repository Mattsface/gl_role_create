
import yaml


class CreateRoleAccount(Object):
    def __init__(self, user_bag, gitlab_key=None):
        self.user_bag = user_bag
        self.gitlab_key = gitlab_key

    def import_databag(self):
        """
        convert the user_bag to a dictionary
        """
        with file(self.user_bag) as f:
            self.user_bag = yaml.load(self.user_bag)


    def check_type(self):
        """
        make sure the databag item is a role account
        :return: True of False
        """
        pass


    def convert_to_api(self):
        """


        :return:
        """


        ## TODO: Convert it a form the API can handle

    def send_to_gitlab(self):
        """


        :return:
        """

        ## TODO: Send it to the Gitlab


    def verify_create(self):
        """

        :return:
        """
        ## TODO: Make sure the account was created

