#!/usr/bin/env python

import json
import boto3
import os

def get_inventory(region_name='us-west-1'):
    try:
        # Initialize the boto3 EC2 client
        ec2 = boto3.client('ec2', region_name=region_name)

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
        ssh_key_file = os.path.expanduser('~/.ssh/ansible-new.pem')  # Expand user directory
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
    except Exception as e:
        print(f"Error: {e}")
        return {}

if __name__ == '__main__':
    region = os.getenv('AWS_REGION', 'us-west-1')
    print(json.dumps(get_inventory(region), indent=2))
