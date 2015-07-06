
import yaml


class CreateRoleAccount:
    def __init__(self, user_bag, gitlab_key=None):
        self.user_bag = user_bag
        self.gitlab_key = gitlab_key

    def import_databag(self):
        """
        convert the user_bag to a dictionary
        """
        with file(self.user_bag) as f:
            self.user_bag = yaml.load(f)


    def check_type(self):
        """
        make sure the databag item is a role account
        :return: True or False, if false exceptions
        """
        pass


    def convert_to_api(self):z
        """


        """
        pass

        ## TODO: Convert it a form the API can handle

    def send_to_gitlab(self):
        """


        :return: True or False, if false exception
        """
        pass
        ## TODO: Send it to the Gitlab


    def verify_create(self):
        """

        :return: True or False, if false exception
        """
        pass
        ## TODO: Make sure the account was created

