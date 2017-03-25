#near the top
from tagupdate import compare_tags

jsonlist=['ec2objs.json', 'ec2tags.json']
jsonlist.extend(['elbobjs.json', 'elbtags.json'])
jsonlist.extend(['rdsobjs.json', 'rdstags.json'])
jsonlist.extend(['s3objs.json', 's3tags.json'])
ec2objsjson=jsonlist[0]
ec2tagsjson=jsonlist[1]
elbobjsjson=jsonlist[2]
elbtagsjson=jsonlist[3]
rdsobjsjson=jsonlist[4]
rdstagsjson=jsonlist[5]
s3objsjson=jsonlist[6]
s3tagsjson=jsonlist[7]


compare_tags('EC2', ec2tagsjson, 'stdtags.json', 'ec2stdtags.json')
