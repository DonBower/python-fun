#
#   Import Libraries
#
import boto
import boto.ec2
print('Using Boto Version ',boto.Version, '\n')

import json

jdata = open("newstdtags.json")
stdtags = json.load(jdata)
'''
print('List all standard tags\n')
#print(stdtags)
for eachtag in stdtags:
    print('{0:2}{1:20}{2:25}'.format(' ', eachtag, stdtags[eachtag]))
'''
conn = boto.ec2.connect_to_region('us-west-2')
reservations=conn.get_all_instances();

print('List all instances and tags\n')
#
#   Loop through each instance, and examime the tags.
for reservation in reservations:
    for instance in reservation.instances:
        if 'Name' in instance.tags:
            print('{0:2}{1:20}{2:25}'.format('>', instance.id, instance.tags['Name']))
            thisInstanceName = instance.tags['Name']
        else:
            print('{0:2}{1:20}{2:25}'.format('>', instance.id, ''))
            thisInstanceName = instance.id
        print('\n')

        for tag in instance.tags:
            if tag in stdtags:
                if instance.tags[tag] == stdtags[tag]:
                    print('{0:2}{1:20}{2:25}{3:50}'.format('X', thisInstanceName, tag, instance.tags[tag]))
                else:
                    print('{0:2}{1:20}{2:25}{3:50}'.format('/', thisInstanceName, tag, instance.tags[tag]))
            else:
                print('{0:2}{1:20}{2:25}{3:50}'.format('-', thisInstanceName, tag, instance.tags[tag]))
#
#   Now Loop through the standard tags, to make sure none are missing
#
        for eachtag in stdtags:
            if eachtag not in instance.tags:
                print('{0:2}{1:20}{2:25}{3:50}'.format('+', thisInstanceName, eachtag, stdtags[eachtag]))
