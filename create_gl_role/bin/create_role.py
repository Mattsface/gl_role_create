#!/usr/bin/python
from create_gl_role.gl_role_account_create.gl_role_account_create import CreateRoleAccount
import ConfigParser
import argparse
import getpass
import os
import git
import sys
from gitlab import *


def main():
    args = parse_arguments()
    config = import_config()

    pillar_periodic = config.get('repo', 'pillar_periodic')
    gitlab_token = config.get('gitlab', 'token')
    gitlab_url = config.get('gitlab', 'url')
    role_account_name = args.account_name
    password = args.password
    if args.account_email:
        email = args.account_email
    else:
        email = None

    assert os.path.isdir(pillar_periodic)

    try:
        repo = git.cmd.Git(pillar_periodic)
        repo.pull()
    except:
        e = sys.exc_info()[0]
        print "Failed to pull down changes to pillar_periodic, error: {}".format(e)

    ssh_path = os.path.join(pillar_periodic, "core/accountz/ssh_auth.sls")
    user_path = os.path.join(pillar_periodic, "core/accountz/users.sls")

    # Okay lets create this account
    gl_connection = CreateRoleAccount(user_path, ssh_path, account_name=role_account_name,
                                      account_password=password, account_email=email, gitlab_key=gitlab_token,
                                      gitlab_url=gitlab_url)

    gl_connection.convert_to_api()
    role_user_id = gl_connection.send_to_gitlab()
    if gl_connection.verify_create(role_user_id):
        print "{} Role user successfully created".format(role_account_name)
    else:
        print "{} Role user not created".format(role_account_name)


def parse_arguments():
    """
    collect command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store', dest='account_name', required=True, help="Name of the role account you want to create")
    parser.add_argument('-p', action='store', dest='password', required=True, help="Password for role account")
    parser.add_argument('-e', action='store', dest='account_email', help="Role account email, defaults to account_name@zulily.com")
    args = parser.parse_args()
    return args


def import_config():
    """
    import config file
    """
    config = ConfigParser.ConfigParser()
    user = getpass.getuser()
    config_ini = "/home/{}/.create_role/config.ini".format(user)
    try:
        config.readfp(open(config_ini))
        return config
    except IOError:
        print "Unable to open config file, place it in ~/.create_role/config.ini"
        sys.exit(1)


if __name__ == "__main__":
    main()