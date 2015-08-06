import yaml
from gitlab import *


class CreateRoleAccount(object):
    def __init__(self, users_sls, ssh_sls, **options):
        self.users = users_sls
        self.ssh = ssh_sls
        self.account_name = options.get('account_name')
        self.gitlab_key = options.get('gitlab_key')
        self.gitlab_url = options.get('gitlab_url')
        self.account_email = options.get('account_email')
        self.account_password = options.get('account_password')
        self.new_user = {}

    def import_users_sls(self):
        """
        convert the users_sls to a dictionary
        """

        with file(self.users, 'r') as f:
            self.users = yaml.load(f)

        if not isinstance(self.users, dict):
            self.users = None

    def import_ssh_sls(self):
        """
        convert the ssh_auth.sls to a dictionary
        """

        with file(self.ssh, 'r') as f:
            self.ssh = yaml.load(f)

        if not isinstance(self.ssh, dict):
            self.ssh = None

    def convert_to_api(self):
        """
        Use self.ssh and self.users to create an object to send to the Gitlab API
        """
        self.import_ssh_sls()
        self.import_users_sls()

        if self.ssh is not None and self.users is not None:
            try:
                uid = self.users['accountz_passwd'][self.account_name]['uid']

                if uid > 9999 or uid < 5000:
                    raise AttributeError

                self.new_user['username'] = self.account_name
                self.new_user['name'] = self.account_name
                self.new_user['password'] = self.account_password

                if self.account_email is not None:
                    self.new_user['email'] = self.account_email
                else:
                    self.new_user['email'] = self.account_name + '@zulily.com'

                if self.ssh['accountz_ssh_auth'][self.account_name]:
                    self.new_user['ssh-key'] = self.ssh['accountz_ssh_auth'][self.account_name][0]

            except KeyError:
                raise KeyError("Unable to find Username in accountz")
            except AttributeError:
                raise AttributeError("UID is not in the correct role account range")
        else:
            raise StandardError('Username or ssh key not found for user: {}'.format(self.account_name))

    def send_to_gitlab(self):
        """
        Send user data to gitlab role account create
        """

        try:
            gl = self.connect_to_gitlab_api()

            new_role_user = gl.User({'username': self.new_user['username'], 'name': self.new_user['name'],
                                     'password': self.new_user['password'], 'email': self.new_user['email'],
                                     'project_limit': '0', 'is_admin': False, 'can_create_group': False})
            new_role_user.save()
            print self.new_user['ssh-key']
            new_ssh_key = new_role_user.Key({'title': 'ssh key', 'key': self.new_user['ssh-key']})
            new_ssh_key.save()

            return new_role_user.id
        except Exception as e:
            raise StandardError("Unable to create Gitlab User because {}".format(e))

    def connect_to_gitlab_api(self):
        try:
            gl = Gitlab(self.gitlab_url, self.gitlab_key, ssl_verify=False)
            gl.auth()

            return gl
        except Exception as e:
            raise StandardError("Unable to connect to Gitlab API because {}".format(e))

    def verify_create(self, user_id):
        """
        lets make sure the new role user exists on the system
        """
        try:
            gl = self.connect_to_gitlab_api()
            user = gl.User(user_id)

            if user is not None:
                ret = True
            else:
                ret = False

            return ret
        except Exception as e:
            raise StandardError("Unable to locate created Gitlab Role User".format(e))










