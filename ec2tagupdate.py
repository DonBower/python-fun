#####################################################################################
# ec2tagupdate.py   - This script will scan all of the ec2 instances and for each   #
# instance, it will compare the list of tags to a known set of tags and value.      #
# There are four conditions that will be detected, one Positive, and three negitive #
# For the Positive condition, no action is required.                                #
# For the first negitive condition, an incorrect Tag Value, the value will be       #
# corrected.                                                                        #
# For the second negitive condition, a missing Tag, the Tag and Value will be added #
# For the third negitive condition, a superfluous Tag, the Tag will be removed.     #
#   2017-03-21  - Initial Release                                                   #
#               - Donald Bower                                                      #
#####################################################################################
#
#   Import Libraries
#
import boto
import boto.ec2
import json
print('Using Boto Version ',boto.Version, '\n')
#
#   Establish list of standard EC2 Tags
#
jdata = open("ec2stdtags.json")
stdtags = json.load(jdata)
'''
#   Let's ignore this debug for now...
print('List all standard tags\n')
#print(stdtags)
for eachtag in stdtags:
    print('{0:2}{1:20}{2:25}'.format(' ', eachtag, stdtags[eachtag]))
'''
#
#   Connect to AWS
#   Note: a future version will need to variablize the region.
#
conn = boto.ec2.connect_to_region('us-west-2')
reservations=conn.get_all_instances();
#
print('List all instances and tags\n')
#
#   Loop through each instance, and examime the tags.
#   Note: There is typacly only one reservation, but oh, well...
#
for reservation in reservations:
    #
    #   Examine each instance
    #
    for instance in reservation.instances:
#        print('\n')
        if 'Name' in instance.tags:
            print('{0:2}{1:20}{2:25}'.format('>', instance.id, instance.tags['Name']))
            thisInstanceName = instance.tags['Name']
        else:
            print('{0:2}{1:20}{2:25}'.format('>', instance.id, ''))
            thisInstanceName = instance.id
        #
        #   Examine each tag
        #
        removeTheseTags = []
        for tag in instance.tags:
            #
            #   Tags "Name" and "AIGName" are instance specific, and ignored.
            #
            if tag not in ["Name", "AIGName"]:
                #
                #   For existing tags that are in the standard list, confirm their values
                #
                if tag in stdtags:
                    #
                    #   True is a correct match.
                    #
                    if instance.tags[tag] == stdtags[tag]:
                        print('{0:2}{1:20}{2:25}{3:50}'.format(' ', thisInstanceName, tag, instance.tags[tag]))
                    #
                    #   Value needs updating
                    #
                    else:
                            print('{0:2}{1:20}{2:25}{3:50}'.format(' ', thisInstanceName, tag, instance.tags[tag]))
                            print('{0:2}{1:20}{2:25}{3:50}'.format('>', 'Update tag Value', '', stdtags[tag]))
                            instance.add_tag(tag, stdtags[tag])
                #
                #   For existing tags that are NOT in the standard list, memorize them, for later deletion.
                #
                else:
#                    print('{0:2}{1:20}{2:25}{3:50}'.format('-', thisInstanceName, tag, instance.tags[tag]))
                    removeTheseTags.append(tag)
            #
            #   These tags are instance specific.
            #
#            else:
#                print('{0:2}{1:20}{2:25}{3:50}'.format('=', thisInstanceName, tag, instance.tags[tag]))
        #
        #   Now Loop through the standard tags, to make sure none are missing
        #
        for eachtag in stdtags:
            if eachtag not in instance.tags:
#                print('{0:2}{1:20}{2:25}{3:50}'.format('+', thisInstanceName, eachtag, stdtags[eachtag]))
                print('{0:2}{1:20}{2:25}{3:50}'.format('+', 'Add missing tag ', eachtag, stdtags[eachtag]))
                instance.add_tag(eachtag, stdtags[eachtag])
        #
        #   Now Loop through the list of superfluous tags, and remove them.
        #
        for badTag in removeTheseTags:
            print('{0:2}{1:20}{2:25}{3:50}'.format('-', 'Remove tag ', badTag, ''))
            instance.remove_tag(badTag)
        print('\n')
