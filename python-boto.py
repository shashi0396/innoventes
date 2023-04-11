import os
from urllib import response
import boto3
import pprint
from dotenv import load_dotenv

def ec2_add_security_group(decc, grp_name, vpc_id):
    ec2 = session.client('ec2')
    response = ec2.create_security_group(Description=desc, GroupName=grp_name, VpcId=vpc_id)
    return response

def ec2_add_security_group_rule(grp_id, proto, start_port, end_port, ip_range):
    ec2 = session.client('ec2')
    response = ec2.authorize_security_group_egress(
            GroupId=grp_id,
            IpPermissions=[{
                'IpProtocol': proto,
                'FromPort': start_port,
                'ToPort': end_port,
                'IpRanges': [{
                    'CidrIp': 0.0.0.0
                }]
            }])
    return response
