#!/usr/bin/env python2.7
from __future__ import print_function
from fabric import operations, context_managers
import pprint
import json
import os
import sys
import subprocess

this_dir = os.path.dirname(os.path.realpath(__file__))
os.environ['AWS_CONFIG_FILE'] = os.path.join(this_dir, 'config')
os.environ['LC_CTYPE'] = 'en_EN.UTF-8'


def _describe(command=None):
    all_instances = []
    with context_managers.hide('running'):
        instances = json.loads(operations.local(command, capture=True))
    # to_show = ('InstanceId', 'Tags', 'PublicDnsName', 'PrivateIpAddress')
    # print instances
    for instance in instances['Reservations']:
        if isinstance(instance.get('Instances'), list):
            current_instance = instance.get('Instances')[0]
            all_instances = all_instances + [current_instance]
    #         for attribute in to_show:
    # #            pprint(attribute)
    #             yield(current_instance.get(attribute))
    return all_instances


def describe(region=None):
    regions = [
        'us-east-1',
        'ap-northeast-1',
        'sa-east-1',
        'ap-southeast-1',
        'ap-southeast-2',
        'us-west-2',
        # 'us-gov-west-1',
        'us-west-1',
        'eu-west-1']
#       'fips-us-gov-west-1')
    servers = {}
    # import pdb; pdb.set_trace()
    pprint.PrettyPrinter(indent=4)
    if region:
        if region != 'all':
            regions = [region]
    for current_region in regions:
            command = 'aws --output json --region %s ec2 describe-instances' % (current_region)
            print('###Scan of Region %s ###' % current_region)
            servers[current_region] = _describe(command)

    return servers


def find_instance_by_name(servers, name):
    pprint.PrettyPrinter(indent=4)
    names_ips = []
    for region, servers_in_region in servers.iteritems():
        for server in servers_in_region:
            for tag in server.get('Tags'):
                if tag.get('Key') == 'Name':
                    server_name = tag.get('Value')
                    server_ip = server.get('PublicIpAddress')
                    if name in tag.get('Value'):
                        print(server_name, server_ip)
                        if server_ip:
                            names_ips.append((server_name, server_ip))

    if len(names_ips) == 1:
        print("Connecting to admin@%s" % names_ips[0][1])
        subprocess.call(['ssh', "admin@%s" % names_ips[0][1]], shell=False)
    else:
        print(names_ips[:])
    # else:
    #     print("No server found with the string %s in the name" % name)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        servers = describe(sys.argv[1])
    else:
        servers = describe()

    find_instance_by_name(servers, 'edit')
