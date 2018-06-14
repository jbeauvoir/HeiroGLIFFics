#!/usr/bin/env python
'''
This script will terminate an instance based upon a given instance ID.
'''

import sys
import boto3

ec2 = boto3.resource('ec2')


for instance_id in sys.argv[1:]:
    # Use the ID to get a connection to the instance from the EC2
    # resource.
    instance = ec2.Instance(instance_id)
    # terminate the instance
    response = instance.terminate()
    print response
