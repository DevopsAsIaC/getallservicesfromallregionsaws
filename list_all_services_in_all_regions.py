import boto3
import GenUtils

regions= GenUtils.get_all_regions()
services=GenUtils.get_all_services()
print (boto3.Session().get_credentials().access_key)
print (boto3.Session().get_credentials().secret_key)
for region in regions:
	for service in services:
		print(service,region)
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
                 	   			print(instance["InstanceId"])
		elif (service == "s3"):
			print("list s3 for s3" )	
		else:
			print("TODO ", service)
