import subprocess
import json
import os
from tagupdate import compare_tags
from tagupdate import print_tags

jsonlist=['ec2objs.json', 'ec2tags.json']
jsonlist.extend(['elbobjs.json', 'elbtags.json'])
jsonlist.extend(['rdsobjs.json', 'rdstags.json'])
jsonlist.extend(['s3objs.json', 's3tags.json'])
updatelist='tagupdate.json'

ec2objsjson=jsonlist[0]
ec2tagsjson=jsonlist[1]
elbobjsjson=jsonlist[2]
elbtagsjson=jsonlist[3]
rdsobjsjson=jsonlist[4]
rdstagsjson=jsonlist[5]
s3objsjson=jsonlist[6]
s3tagsjson=jsonlist[7]

'''
ec2obsjson='ec2objs.json'
ec2tagsjson='ec2tags.json'
elbobjsjson='elbobj.json'
elbtagsjson='elbtags.json'
rdsobjsjson='rdsobjs.json'
rdstagsjson='rdstags.json'
s3objsjson='s3objs.json'
s3tagsjson='s3tags.json'
'''
###########################################################
#   Initalize Files
###########################################################
for filename in jsonlist:
    if os.path.exists(filename):
        os.remove(filename)
with open(updatelist, 'w') as outfile:
    json.dump({'Updates':[]}, outfile, indent = 4)

###########################################################
#   Retreive the JSON file describing all of the EC2
#   Instances from the selected environment.
###########################################################
print('aws ec2 describe-instances > ', ec2objsjson)
os.system('aws ec2 describe-instances > ' + ec2objsjson)
ec2json = open(ec2objsjson)
allec2s = json.load(ec2json)
if 'Reservations' in allec2s:
    for ec2 in allec2s['Reservations']:
        if 'Instances' in ec2:
            for instance in ec2['Instances']:
#                print(ec2['Instances'])
                print('aws ec2 describe-tags --filters "Name=resource-id,Values=', instance['InstanceId'], '" > ', ec2tagsjson)
                os.system('aws ec2 describe-tags --filters "Name=resource-id,Values=' + instance['InstanceId'] + '" > ' + ec2tagsjson)
                print('\n')
                compare_tags(updatelists 'EC2', ec2tagsjson, 'stdtags.json', 'ec2stdtags.json')
#                print_tags(ec2tagsjson)

###########################################################
#   Retreive the JSON file describing all of the ELB
#   Instances from the selected environment.
###########################################################
print('aws elb describe-load-balancers > ', elbobjsjson)
os.system('aws elb describe-load-balancers > ' + elbobjsjson)

elbjson = open(elbobjsjson)
allelbs = json.load(elbjson)
if 'LoadBalancerDescriptions' in allelbs:
    for elb in allelbs['LoadBalancerDescriptions']:
        if 'LoadBalancerName' in elb:
#            print(elb['LoadBalancerName'])
            print('aws elb describe-tags --load-balancer-names ', elb['LoadBalancerName'], ' >> ', elbtagsjson)
            os.system('aws elb describe-tags --load-balancer-names ' + elb['LoadBalancerName'] + ' >> ' + elbtagsjson)
            print('\n')
###########################################################
#   Retreive the JSON file describing all of the EC2
#   Instances from the selected environment.
###########################################################
print('aws rds describe-db-instances > ', rdsobjsjson)
os.system('aws rds describe-db-instances > ' + rdsobjsjson)
rdsjson = open(rdsobjsjson)
allrdss = json.load(rdsjson)
if 'DBInstances' in allrdss:
    for rds in allrdss['DBInstances']:
        if 'DBInstanceArn' in rds:
#            print(rds['DBInstanceArn'])
            print('aws rds list-tags-for-resource --resource-name ', rds['DBInstanceArn'], ' >> ', rdstagsjson)
            os.system('aws rds list-tags-for-resource --resource-name ' + rds['DBInstanceArn'] + ' >> ' + rdstagsjson)
            print('\n')
###########################################################
#   Retreive the JSON file describing all of the S3
#   Instances from the selected environment.
###########################################################
print('aws s3api list-buckets > ', s3objsjson)
os.system('aws s3api list-buckets > ' + s3objsjson)
s3json = open(s3objsjson)
alls3s = json.load(s3json)
if 'Buckets' in alls3s:
    for s3bucket in alls3s['Buckets']:
#        print(s3bucket['Name'])
        print('aws s3api get-bucket-tagging --bucket ', s3bucket['Name'], ' >> ', s3tagsjson)
        os.system('aws s3api get-bucket-tagging --bucket ' + s3bucket['Name'] + ' >> ' + s3tagsjson)
        print('\n')


#print(allelbs["LoadBalancerDescriptions"]["Subnets"])



#for line in elbjson.readlines():
#    print(line),
#retval = p.wait()
