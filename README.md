# HeiroGLIFFics
Automating AWS With Python and Boto3

A special thanks to Michael J who presented an awesome tutorial on how to make these scripts. If you would like to check out his tutorial visit https://linuxacademy.com/howtoguides/posts/show/topic/14209-automating-aws-with-python-and-boto3. Also thanks to fstab@github for the docker-aws-cli repo (https://github.com/fstab/docker-aws-cli).

________________________________________________________________________________________________________________
AWS Identity and Access Management (IAM):
IAM enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. For more documentation go to https://aws.amazon.com/iam/.

I have given the IAM user AmazonRDSFullAccess, AmazonS3FullAccess, and AmazonEC2FullAccess.
________________________________________________________________________________________________________________

These scripts allow you to:
- Create, delete, list, and put files into a bucket 
- Create, terminate, and list running instances
- Create, delete, and list database instances (only the instance)

The Future:
There's a nice skeletal modal here: buckets, instances, database instances. With all these elements I would like to:
- spin up the instances with key pairs; currently they do not have any and require a username and password, which is very unsecure
- Learn more about CloudTrail Services to make monitoring easier
- Learn more about Continous Integration with platforms like Jenkins
- Find a good way to utilize Docker containers on my instances
- Somehow implement AWS SNS using the boto3 library
