import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

#
#   Try This
#
if 'SecurityGroups' in data:
    print('{0:15}{1:30}{2:50}'.format("GroupId", "Name", "Description"))
    for SecGrp in data['SecurityGroups']:
        print('{0:15}{1:30}{2:50}'.format(SecGrp['GroupId'], SecGrp['GroupName'], SecGrp['Description']))
#        if 'Tags' in SecGrp:
#            print('\t{0:15}{1:30}'.format('Key', 'Value'))
#            for Tag in SecGrp['Tags']:
#                print('\t{0:15}{1:30}'.format(Tag['Key'], Tag['Value']))
#        else:
#            print('\tNo Tags Found!')
if 'Reservations' in data:
    print('{0:20}{1:20}{2:15}'.format("ReservationId", "InstanceId", "AMI"))
    for Reservation in data['Reservations']:
        if 'Instances' in Reservation:
            for Instance in Reservation['Instances']:
                print('{0:20}{1:20}{2:15}'.format(Reservation['ReservationId'], Instance['InstanceId'], Instance['ImageId']))
                if 'Tags' in Instance:
                    print('\t{0:15}{1:30}'.format('Key', 'Value'))
                    for Tag in Instance['Tags']:
                        print('\t{0:15}{1:30}'.format(Tag['Key'], Tag['Value']))

        else:
            print('No Instances Found!')

jdata.close()
