#!/usr/bin/env python
'''
This script creates an ec2 micro instance.
'''


import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-25110f45',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')

print instance[0].id
