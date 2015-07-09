import yaml


class CreateRoleAccount:
    def __init__(self, users, ssh, account_name, account_email=None, gitlab_key=None):
        self.users = users
        self.ssh = ssh
        self.account_name = account_name
        self.gitlab_key = gitlab_key
        self.account_email = account_email
        self.new_user = {}


    def import_users_sls(self):
        """
        convert the users_sls to a dictionary
        :returns
        """

        with file(self.users) as f:
            self.users = yaml.load(f)

        if not isinstance(self.users, dict):
            self.users = None

    def import_ssh_sls(self):
        """
        convert the ssh_auth.sls to a dictionary
        :returns
        """

        with file(self.ssh) as f:
            self.ssh = yaml.load(f)

        if not isinstance(self.ssh, dict):
            self.ssh = None

    def convert_to_api(self):
        """
        Use self.ssh and self.users to create an object to send to the Gitlab API

        """
        self.import_ssh_sls()
        self.import_users_sls()


        if self.ssh is not None or self.users is not None:
            pass
        else:
            raise StandardError('Username or ssh key not found for user: {}'.format(self.account_name))


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











