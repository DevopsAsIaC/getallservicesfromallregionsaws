from boto3.session import Session
import boto3
s = Session()

def get_all_regions():
	dynamodb_regions = s.get_available_regions('dynamodb')
	return dynamodb_regions

def get_all_services():
	services = s.get_available_services()
	return services
