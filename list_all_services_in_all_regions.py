mport boto3
import GenUtils

#regions= GenUtils.get_all_regions()
services=GenUtils.get_all_services()

for service in services:
        available_regions = boto3.Session().get_available_regions(service)
        for region in available_regions:
                #print(service,region)
                bclient = boto3.client(service, region_name=region)
                if (service == 'ec2'):
                        try:
                                response = bclient.describe_instances()
                        except:
                                print ("no"+ service +"in region " + region  )
                                continue
                        for reservation in response["Reservations"]:
                                for instance in reservation["Instances"]:
                                        if instance['State']['Name'] == 'running':
                                                print(region,service, instance["InstanceId"])
                elif (service == "rds"):
                        try:
                                paginator = bclient.get_paginator('describe_db_instances').paginate()
                                for page in paginator:
                                        for dbinstance in page['DBInstances']:
                                                print(region,service,"{DBInstanceClass}".format(**dbinstance))
                        except:
                                print ("no rds instances",region)


                else:
                        continue
