#
#   Import Libraries
#
import json
import os
obj_tags='tagupdate.json'
objjdata = open(obj_tags)
objtags = json.load(objjdata)
print('Go!')
'''
for updates in objtags:
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
'''
