#
#   Import Libraries
#
import json
import os
obj_tags='tagupdate.json'
obj_type='EC2'
thisInstanceName='i-0e2cc660fa725c142'
#objjdata = open(obj_tags)
#objtags = json.load(objjdata)
print('Go!')
with open('tagupdate.json', 'w') as outfile:
    json.dump({'Updates':[]}, outfile, indent = 4)

updtags = {}
updateTheseTags = {"AMI": "ami-d969ceb9"}
addTheseTags = {"CBD": "0031-0670-6222"}
removeTheseTags = {"I_am_a_bad_tag": "yep-very-bad"}
#    updtags = {obj_type: [thisInstanceName]}
#    updtags = {obj_type: ['obj_id': thisInstanceName]}
updtags['obj_type'] = obj_type
updtags['obj_id'] = thisInstanceName
updtags['updateTheseTags'] = updateTheseTags
updtags['addTheseTags'] = addTheseTags
updtags['removeTheseTags'] = removeTheseTags
print(updtags)

with open('tagupdate.json', 'r') as outfile:
    existingFile=json.load(outfile)
existingFile['Updates'].append(updtags)
with open('tagupdate.json', 'w') as outfile:
    json.dump(existingFile, outfile, indent = 4)

with open('tagupdate.json', 'r') as outfile:
    existingFile=json.load(outfile)
existingFile['Updates'].append(updtags)
with open('tagupdate.json', 'w') as outfile:
    json.dump(existingFile, outfile, indent = 4)

with open('tagupdate.json', 'r') as outfile:
    existingFile=json.load(outfile)
existingFile['Updates'].append(updtags)
with open('tagupdate.json', 'w') as outfile:
    json.dump(existingFile, outfile, indent = 4)
