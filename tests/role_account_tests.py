import unittest
import gl_role_account_create

class TestCreateRoleAccount(unittest.TestCase):

    def setUp(self):
        user1 =  {
            "type": "role",
            "system": false,
            "id": "r-vxp-git",
            "password": "!!",
            "uid": "534",
            "gid": [ "nobody" ],
            "groups": [ ],
            "comment": "VXP git role account,,,",
            "home": "/home/r-vxp-git",
            "shell": "/bin/bash",
            "config_git": "true",
            "ssh_keys":
            [
            "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1dT4/LQdxxLntE/CPyxWpqQL+hXSYV6AwdZzULsrhGta2AYEfROPs3pvgXRiYwXSj1USqTCsVcZJ8v/iPp9LaXj8iLGlERWh0bRqijRe53Bw96RvQKJq1ap3VekpjOgHAVOvnXxYz/BHRnr7uzjcYEdm3DHn+5cIB/eWMWdsgvsQ5BLrcITP/u+ofLEayXL+FEC/PexI2C1cXlAz98l9wvB4O0GhgLjQTQDJ1B0g5Cepr/369x5IRNQD/hCX0FHu8O+09tFxiwcWUcHB3MbB4bkuwTvV1Q78xneORwjterpExj5tFeKYKMXL6+h6ewYL5TO/uvvIBmd2TbajJMKMF r-vxp-git@zulily.com"
            ],
            "access": [ ]
        }
        user2 = {
            "type": "person",
            "system": false,
            "id": "mspah",
            "password": "$6$Ki.Jd4FB$njmz8j7a0xbop06RcOdbAmp4mgDjsQs6yn05cCjRLJkliTAO6HCAWIl24ChH.VxkY1g36brn7uIzHkpHri1XS1",
            "uid": "1200",
            "gid": [ "www-coop" ],
            "groups": [ ],
            "comment": "Matt Spah,Software Dev Team,,",
            "home": "/home/mspah",
            "shell": "/bin/bash",
            "config_git": "true",
            "ssh_keys":
            [
            "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABBwCUrhV7fANUeM1OErZrm/5K193XHEHdcUjxKol/cdijjeUA4mraLMaqga4XU7aU4PVMmgIY7dn8nKP8JOIagxjLXe62/cblnS2Sd2Iv+HghcIENN/k5EXJVAIfOyRpGLlzDe7P4cxeDMlOzTsC9pdxiuYjd4ilh8uLwwpS596AC9CoU229aLva4hZoVrV+/rxR/73vRPqWmBX0lJ+d0MuAZiiwy07+WZquY3bP/CdByzxE7aRRGTXe4vYNIhOSlgj70wPiVlMGziQfaCM4hhLO3qHrxL0WKaSpzIEOM1Y4zpTlo9/NROJrPdwF6iQ3YseIxUkFdk9KJ0vkxeZTSGnV1npbDDOfb mspah@zulily.com"
            ],
            "access": [ "sysadmin" ]
        }


    def test_import_databag(self):
        account = CreateRoleAccount(user1)

    def test_failed_import_databag(self):
        pass

    def test_dict_creation(self):
        pass

    def test_failed_dict_creation(self):
        pass




