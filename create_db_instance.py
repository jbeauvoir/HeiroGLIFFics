#!/usr/bin/env python

'''
This script creates a database instance. 
Necessary items:
- Name/Identifier for the instance 
- username for the admin or root account
- a password for the admin account
- class/type the instance will be created as
- database engine that the instance will use
- amount of storage the instance will allocate for the db
'''

import boto3

rds = boto3.client('rds')
try:
     response = rds.create_db_instance(
        DBInstanceIdentifier='dbserver',
        MasterUsername='dbadmin',
        MasterUserPassword='abcdefg123456789',
        DBInstanceClass='db.t2.micro',
        Engine='mariadb',
        AllocatedStorage=5)
     print response
except Exception as error:
    print error
