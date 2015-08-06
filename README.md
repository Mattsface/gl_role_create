Create a Role account on a Gitlab Server using Salt user and SSH sls files


## Setup
Create a directory in your users home directory named .create_role and place a config.ini file in it

The config.ini file needs to look something like this
```
[repo]
pillar_periodic = /home/mspah/git/pillar_periodic

[gitlab]
token = slsdfk039402340
url = https://gitlab.corp.zulily.com
```
## Examples
```
usage: create_role.py [-h] (-r RANDOM_PASSWORD_LENGTH | -p PASSWORD) -a
                      ACCOUNT_NAME [-e ACCOUNT_EMAIL]

optional arguments:
  -h, --help            show this help message and exit
  -r RANDOM_PASSWORD_LENGTH
                        Length of random password to be created
  -p PASSWORD           Password for role account
  -a ACCOUNT_NAME       Name of the role account you want to create
  -e ACCOUNT_EMAIL      Role account email, defaults to
                        account_name@zulily.com

To create a role account for r-infraopts-git:
    $ create_role.py -a r-infraops-git -p pD3fv3425f

To Create a role account for r-infraops-git that uses an email:
    $ create_role.py -a r-infraops-git -p pD3fv3425f -e infraops@zulily.com

To Create a role account for r-infraops-git that uses a random password of length 15 and an email
    $create_role.py -a r-infraops-git -r 15 -e infraops@zulily.com
```