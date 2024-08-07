#!/usr/bin/env python

import json
import boto3

def get_inventory():
    # Initialize the boto3 EC2 client
    ec2 = boto3.client('ec2', region_name='us-west-1')  # Specify your AWS region

    # Describe EC2 instances
    response = ec2.describe_instances()
    
    # Initialize inventory dictionary
    inventory = {
        'all': {
            'hosts': [],
            'vars': {}
        },
        '_meta': {
            'hostvars': {}
        }
    }
    
    # Specify the SSH key file and user (if applicable)
    ssh_key_file = '/path/to/your/my-key.pem'  # Path to your SSH private key file
    ssh_user = 'ubuntu'  # SSH username
    
    # Iterate over reservations and instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Use the Public DNS name as the host if available
            public_dns = instance.get('PublicDnsName', instance['InstanceId'])
            
            # Add host to inventory
            inventory['all']['hosts'].append(public_dns)
            
            # Define host variables
            inventory['_meta']['hostvars'][public_dns] = {
                'ansible_host': instance.get('PublicIpAddress', instance['InstanceId']),
                'ansible_ssh_private_key_file': ssh_key_file,
                'ansible_user': ssh_user
            }

    return inventory

if __name__ == '__main__':
    print(json.dumps(get_inventory(), indent=2))
