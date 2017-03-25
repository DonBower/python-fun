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
import json
def compare_tags(obj_type, obj_tags, std_tags, type_tags):
#
#   Establish list of Tags
#
    tsttags = {}
    print('Compare ' + obj_tags + ' to ' + std_tags + ' and ' + type_tags)
    objjdata = open(obj_tags)
    objtags = json.load(objjdata)
    if obj_type == 'EC2':
#        thisInstanceName=objtags.tags['ResourceId']
        if 'Tags' in objtags:
            for tags in objtags['Tags']:
                if 'ResourceId' in tags:
                    thisInstanceName=tags['ResourceId']
                if 'Key' in tags and 'Value' in tags:
                    thistagkey = tags['Key']
                    thistagvalue = tags['Value']
                    tsttags[thistagkey] = thistagvalue
#
#    print('\n These are the tags we are going to examime\n')
#    for eachtag in tsttags:
#        print('{0:2}{1:20}{2:25}'.format(' ', eachtag, tsttags[eachtag]))
#
#   Join the type tags to the standard tags for reference
#
    stdjdata = open(std_tags)
    stdtags = json.load(stdjdata)

    typjdata = open(type_tags)
    typtags = json.load(typjdata)
    #
    #   Merge the type tags into the standard tags
    #
    #print('List all standard tags\n')
    #print(stdtags)
    for eachtag in typtags:
        stdtags[eachtag] = typtags[eachtag]
#    print('\n These are the reference tags\n')
#    for eachtag in stdtags:
#        print('{0:2}{1:20}{2:25}'.format(' ', eachtag, stdtags[eachtag]))
    #
    #   Examine each tag
    #
    removeTheseTags = {}
    updateTheseTags = {}
    addTheseTags = {}
    for tag in tsttags:
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
                if tsttags[tag] == stdtags[tag]:
                    print('{0:2}{1:20}{2:25}{3:50}'.format(' ', thisInstanceName, tag, tsttags[tag]))
                #
                #   Value needs updating
                #
                else:
                    print('{0:2}{1:20}{2:25}{3:50}'.format(' ', thisInstanceName, tag, tsttags[tag]))
                    print('{0:2}{1:20}{2:25}{3:50}'.format('>', 'Update tag Value', '', stdtags[tag]))
                    updateTheseTags[tag] = stdtags[tag]
            #
            #   For existing tags that are NOT in the standard list, memorize them, for later deletion.
            #
            else:
                print('{0:2}{1:20}{2:25}{3:50}'.format('-', thisInstanceName, tag, tsttags[tag]))
                removeTheseTags[tag] = tsttags[tag]
    #
    #   Now Loop through the standard tags, to make sure none are missing
    #
    for eachtag in stdtags:
        if eachtag not in tsttags:
            print('{0:2}{1:20}{2:25}{3:50}'.format('+', 'Add missing tag ', eachtag, stdtags[eachtag]))
            addTheseTags[eachtag] = stdtags[eachtag]

    if os.path.getsize('tagupdate.json') > 0:
        with open('tagupdate.json', 'a') as outfile:
            outfile.write(',\n')


    updtags = {}
#    updtags = {obj_type: [thisInstanceName]}
#    updtags = {obj_type: ['obj_id': thisInstanceName]}
    updtags['obj_type'] = obj_type
    updtags['obj_id'] = thisInstanceName
    updtags['updateTheseTags'] = updateTheseTags
    updtags['addTheseTags'] = addTheseTags
    updtags['removeTheseTags'] = removeTheseTags
    with open('tagupdate.json', 'a') as outfile:
        json.dump(updtags, outfile, indent = 4)
#        outfile.write(',\n')

def print_tags(obj_tags):
    objjdata = open(obj_tags)
    objtags = json.load(objjdata)
    print('Go!')
    for updates in objtags['Updates']:
#        print('\n')
#        print(updates)
#        print('\n')
        if 'obj_type' in updates:
            print(updates['obj_type'])
        if 'obj_id' in updates:
            thisInstanceName = updates['obj_id']
            print(thisInstanceName)
        if 'removeTheseTags' in updates:
            for update in updates['removeTheseTags']:
                print('{0:2}{1:20}{2:25}{3:50}'.format('-', thisInstanceName, update, updates['removeTheseTags'][update]))
        if 'updateTheseTags' in updates:
            for update in updates['updateTheseTags']:
                print('{0:2}{1:20}{2:25}{3:50}'.format('=', thisInstanceName, update, updates['updateTheseTags'][update]))
        if 'addTheseTags' in updates:
            for update in updates['addTheseTags']:
                print('{0:2}{1:20}{2:25}{3:50}'.format('+', thisInstanceName, update, updates['addTheseTags'][update]))

#    for obj_type in objtags:
#        print(obj_type)
#        thisInstanceName = obj_type['obj_id']
