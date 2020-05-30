#!/usr/bin/env python3

import sys
import requests
import boto3

# permissions on script must be owned by root with mode 0755
'''
AuthorizedKeysCommand /usr/local/bin/get_ssm_keys.py %u
AuthorizedKeysCommandUser nobody
'''

# IAM policy dependency
'''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:Describe*",
                "ssm:Get*",
                "ssm:List*"
            ],
            "Resource": "arn:aws:ssm:us-east-1:<account-id>:parameter/ssh/*"
        }
    ]
}
'''

def get_region():
    r = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
    response_json = r.json()
    return response_json.get('region')


def get_ssm_keys(user):
    ssm_path = '/ssh/' + user
    c = boto3.client('ssm', region_name=get_region())
    r = c.get_parameter(Name=ssm_path)
    keys = r['Parameter']['Value'].split(',')
    if not keys:
        return
    for key in keys:
        yield key


if __name__ == '__main__':

    if not len(sys.argv) == 2:
        print("Please supply a user")
        sys.exit(1)
    try:
        keys = get_ssm_keys(sys.argv[1])
    except Exception as error:
        sys.exit(error)
    else:
        for key in keys:
            print(key)
