#!/usr/bin/env python
'''
This prorgam will list the current instances running.

'''
import boto3

ec2 = boto3.resource('ec2') # Create an EC2 resource

# Loop to acquire and print all instance ID and state
for instance in ec2.instances.all():
    print instance.id, instance.state

