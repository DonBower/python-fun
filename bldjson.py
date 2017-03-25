import json
data = {}
innerlist1 = {}
innerlist2 = {}
innerlist3 = {}
innerlist4 = {}

#outerloop =[]
innerlist1['Key'] = 'key1'
innerlist1['Value'] = 'value1'
innerlist2['Key'] = 'key2'
innerlist2['Value'] = 'value2'
innerlist3['Key'] = 'key3'
innerlist3['Value'] = 'value3'
innerlist4['Key'] = 'key4'
innerlist4['Value'] = 'value4'
data['Tags'] = [innerlist1, innerlist2, innerlist3, innerlist4]
data['Instance'] = 'Instance1'

print(data)
lookforkey = 'Key3'
mytags = data['Tags']

if lookforkey in mytags:
    foundvalue = mytags.get(lookforkey)
    print(foundvalue)
else:
    print('can not find ', lookforkey,  ' in ',  mytags)

with open('jsondata.json', 'w') as outfile:
     json.dump(data, outfile, sort_keys = True, indent = 4,
               ensure_ascii = True)
