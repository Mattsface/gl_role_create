from setuptools import setup, find_packages

setup(name='gl_role_account_create',
      version='0.1.0',
      description='CLI to create a Gitlab Role account from a Role account user data bag item',
      author='Matthew Spah',
      author_email='spahmatther@gmail.com',
      scripts=['gl_role_account_create/bin/create_role.py'],
      packages=find_packages(),
      install_requires=['pyyaml',
                        'python-gitlab'],
      dependency_links=[
          "git+ssh://git@github.com:gpocentek/python-gitlab.git#python-gitlab"
      ],
      zip_safe=False)
