from boto3.session import Session
import boto3

class GenUtils:

	@staticmethod
	def get_all_regions():
		s = Session()
		dynamodb_regions = s.get_available_regions('dynamodb')
		return dynamodb_regions
