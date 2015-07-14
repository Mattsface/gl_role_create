Create a Role account a Gitlab Server


## Setup
Create a directory in your users home directory named .create_role and place a config.ini file in it

The config.ini file needs to look something like this

[repo]
pillar_periodic = /home/mspah/git/pillar_periodic

[gitlab]
token = slsdfk039402340
url = https://gitlab.corp.zulily.com

## Examples

create_role.py -h
usage: create_role.py [-h] -a ACCOUNT_NAME -p PASSWORD [-e ACCOUNT_EMAIL]

optional arguments:
  -h, --help        show this help message and exit
  -a ACCOUNT_NAME   Name of the role account you want to create
  -p PASSWORD       Password for role account
  -e ACCOUNT_EMAIL  Role account email, defaults to account_name@zulily.com
