import unittest
import yaml
from os import remove
from gl_role_account_create.gl_role_account_create import CreateRoleAccount


class TestCreateRoleAccount(unittest.TestCase):

    def setUp(self):
        self.users_sls_contents = """
        accountz_passwd:
          ahoogen:
            uid: 10127
            gid: 10127
            password_hash: !
            status: removed
            shell: /bin/false
            home_directory: /home/ahoogen
            full_name: Austen Hoogen
            team: Software Dev Team
            pager_email: ""
            phone_number: ""

          c-rrobeal:
            uid: 10070
            gid: 10070
            password_hash: !
            status: removed
            shell: /bin/bash
            home_directory: /home/c-rrobeal
            full_name: Rafik Robeal
            team: Software Dev Contractor
            pager_email: ""
            phone_number: ""

          r-infraops-git:
            uid: 5041
            gid: 5041
            password_hash: !
            status: active
            shell: /bin/bash
            home_directory: /home/r-infraops-git
            full_name: InfraOps git
            team: ""
            pager_email: ""
            phone_number: ""
        """
        self.ssl_auth_contents = """
        accountz_ssh_auth:
          aargo:
            - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCt1nKLrEoea0mfFDgT1uxL4JxSB03U5ooklpSDMWxARzmaVjSDcQ3CyS/v2tELPaboCUpsu9qIZg6bep3q9pWGhOnlD4uY3zWUJmU4K7p01HCX+/JFdUCHosWRHJVsZM9/OutLINU6npztSaCEQRSmIfSpIOTCaIgJxliIUBDkGNgfakWsTzwoCLjbD8PDzSchJu2bmTnxJrAdB8wlcsuMQvakN0Ej3BdKIvdylahh01UfuiSSGwmjgovSKiVW0HAc5GZ9qZFKIclBaBs2k0xaMaP/6ojLngszKOnT2whHQGNC4YWKWsKueT/GQcVfQGv9IEKAI6hNuRcwBOfukvdH aargo@zulily.com

          adbarrett:
            - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKGp/JDHjvNU3RMH7GIZsnEevptWN02l5WNSpSQW2B5vgdk/lasAOD3B1bvFOAPimu1l7h39xE+tzcmZFCk1ERAR1r9la5/xIVKeZlwxesRo5dogv1q3orJPtAgim5CxYHftkybgOVdpXT7RFzXAa1Zj2HWs46wM0cTreX0xpSrDtIVECZlLYOvJbu1UkNvW8flcnnJrohswsVakDTTt29opOIw/8FqVelw9T+jguiPW9ywrFU+/EuJUiTTCWzchwy+0kI/EBC7w0x8qmNwJIsNCw3Hq/sgMN8prtEUb8ti61j9+aEsMrjH/Z3rymoeaQWnLAsKs67bavSIUIaVPzh adbarrett@zulily.com

          r-infraops-git:
            - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCJlrG43+2eJDNi3pkIph8PHCqJAoTRq1sRVZZ9tW0AXSXROOcxB1wLHFIx9iiBKNKqrxSRmFyKaWtvMjSqxL7e62Ll+QfjQGt8UyyiTVfWFx+aGy8YUil3OPej7UayOS3Izk6zwDUvRAjP41kIdZEP8oRTvRbUdo3j8sLIaSkF/yiYtqehSl2yZasQAOubLBbk4hq5sgLfmdyScb6J+zRn5SEwMHNufTbPQXArAeZa+zVA4y/zrCecPRIKfWCi6JadaZRS7DPa2Eyj1ShLVDqD7vIT4EyhAIkPFXam+MK641DyoNj9HSHv5FaAt6fSvQaH9PR/MCSSSdwgb6YT/Jx r-infraops-git@zulily.com
        """

        self.ssl_auth_filename = 'ssh_auth.sls'
        self.users_filename = 'users.sls'
        self.bad_users_filename = 'bad_users.sls'
        self.bad_ssl_auth_filename = 'bad_ssh_auth.sls'



        with file(self.users_filename, 'w') as f:
            f.write(self.users_sls_contents)
        with file(self.ssl_auth_filename, 'w') as f:
            f.write(self.ssl_auth_contents)

    def tearDown(self):
        remove(self.ssl_auth_filename)
        remove(self.users_filename)

    def test_import_users_sls(self):
        """
        Testing the import_users_sls() function
        """
        user = 'r-infraops-git'
        role_user = CreateRoleAccount(self.users_filename, self.ssl_auth_filename, user)
        expected = dict
        role_user.import_users_sls()
        actual = type(role_user.users)
        self.assertEqual(expected, actual, "Expected type {}. but got {},".format(expected, actual))

    def test_failed_users_sls(self):
        """
        Testing a failed import_users_sls() function
        """
        pass


    def test_import_ssh_sls(self):
        """
        Testing the import_ssh_sls function
        """
        user = 'r-infraops-git'
        role_user = CreateRoleAccount(self.users_filename, self.ssl_auth_filename, user)
        expected = dict
        role_user.import_ssh_sls()
        actual = type(role_user.ssh)
        self.assertEqual(expected, actual, "Expected type {}. but got {},".format(expected, actual))

    def test_failed_import_ssh_sls(self):
        pass

    def test_dict_creation(self):
        pass

    def test_failed_dict_creation(self):
        pass




