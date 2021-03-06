#!/usr/bin/python
from create_gl_role.gl_role_account_create.gl_role_account_create import CreateRoleAccount
import ConfigParser
import argparse
import getpass
import os
import git
import random
import sys
import string
from gitlab import *


def main():
    args = parse_arguments()
    config = import_config(args.config_file)

    pillar_periodic = config.get('repo', 'pillar_periodic')
    gitlab_token = config.get('gitlab', 'token')
    gitlab_url = config.get('gitlab', 'url')
    role_account_name = args.account_name

    if args.account_email:
        email = args.account_email
    else:
        email = None

    if args.password:
        password = args.password
    else:
        password = generate_random_password(args.random_password_length)

    try:
        assert os.path.isdir(pillar_periodic)
    except:
        print "Unable to located pillar_periodic directory"
        sys.exit(1)

    try:
        repo = git.cmd.Git(pillar_periodic)
        repo.pull()
    except:
        e = sys.exc_info()[0]
        print "Failed to pull down changes to pillar_periodic, error: {}".format(e)
        sys.exit(1)

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
        try:
            print "The random password is {}".format(password)
        except:
            pass
    else:
        print "{} Role user not created".format(role_account_name)


def parse_arguments():
    """
    collect command line arguments
    """
    parser = argparse.ArgumentParser()
    password_group = parser.add_mutually_exclusive_group(required=True)
    password_group.add_argument('-r', action='store', dest='random_password_length', type=int, help="Length of random password to be created")
    password_group.add_argument('-p', action='store', dest='password', help="Password for role account")
    parser.add_argument('-a', action='store', dest='account_name', required=True, help="Name of the role account you want to create")
    parser.add_argument('-e', action='store', dest='account_email', help="Role account email, defaults to account_name@zulily.com")
    parser.add_argument('-c', action='store', dest='config_file', help="Location of config.ini")

    args = parser.parse_args()
    return args


def import_config(config_ini=None):
    """
    import config file
    """
    config = ConfigParser.ConfigParser()
    user = getpass.getuser()

    if config_ini is None:
        config_ini = "/home/{}/.create_role/config.ini".format(user)
    try:
        config.readfp(open(config_ini))
        return config
    except IOError:
        print "Unable to open config file, place it in ~/.create_role/config.ini"
        sys.exit(1)


def generate_random_password(length):
    """
    Create a random password based on length and return it
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    random.seed = (os.urandom(1024))
    password = ''.join(random.choice(characters) for i in xrange(length))

    return password

if __name__ == "__main__":
    main()