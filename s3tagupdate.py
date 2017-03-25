#####################################################################################
# rdstagupdate.py   - This script will scan all of the rds instances and for each   #
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
import boto.s3
import json
print('Using Boto Version ',boto.Version, '\n')
#
#   Establish list of standard EC2 Tags
#
jdata = open("s3stdtags.json")
stdtags = json.load(jdata)
#
#   Connect to AWS
#   Note: a future version will need to variablize the region.
#
conn = boto.s3.connect_to_region('us-west-2')
instances=conn.get_all_buckets();
#
print('List all instances and tags\n')
#
#   Loop through each instance, and examime the tags.
#
for instance in instances:
#        print('\n')
    print(instance.name)
    tags=conn.list_tags_for_resource(instance.id)
#    print(tags)
'''
    if 'Name' in instance.Tags:
        print('{0:2}{1:20}{2:25}'.format('>', instance.id, instance.Tags['Name']))
        thisInstanceName = instance.Tags['Name']
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
#                            instance.add_tag(tag, stdtags[tag])
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
#                instance.add_tag(eachtag, stdtags[eachtag])
    #
    #   Now Loop through the list of superfluous tags, and remove them.
    #
    for badTag in removeTheseTags:
        print('{0:2}{1:20}{2:25}{3:50}'.format('-', 'Remove tag ', badTag, ''))
#            instance.remove_tag(badTag)
    print('\n')
'''
