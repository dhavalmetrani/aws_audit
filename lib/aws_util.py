################################################
import boto3
from lib.constants import *
from lib.util import *
################################################


################################################
# Specify AWS profile to use
################################################
def use_profile(aws_profile=Constants.AWS_PROFILE_DEFAULT):
	try:
		boto3.setup_default_session(profile_name=aws_profile)
	except:		
		# boto3.setup_default_session(profile_name=Constants.AWS_PROFILE_DEFAULT)
		return False
	return True
################################################


################################################
# Get AWS Resource
################################################
def get_aws_resource(aws_resource=Constants.AWS_EC2):
	try:
		aws_resource_obj = boto3.resource(aws_resource)
	except:
		aws_resource_obj = None
	return aws_resource_obj
################################################


################################################
# Get AWS EBS volume report
################################################
def prepare_aws_ebs_volume_report(output_file, volumes=Constants.AWS_VOLUMES_AVAILABLE):
	ec2 = get_aws_resource(Constants.AWS_EC2)
	volume_details = "ID, State, Size, Type, IOPS, Created, Availability Zone, Monthly $\n"
	volume_details_available = ""
	volume_details_inuse = ""
	volume_details_total = ""
	totalcost_available = 0
	totalcost_inuse = 0	

	cost = 1
	print "[INFO] Computing resources..."

	for volume in ec2.volumes.all():
		if not volume.iops:
			# print "No IOPS"
			cost = volume.size * Constants.EBS_PRICE[volume.volume_type]
		else:
			cost = volume.size * Constants.EBS_PRICE_GP2_IOPS + volume.iops * Constants.EBS_PRICE_IOPS
			# print "IOPS"

		if volume.state == Constants.AWS_VOLUMES_AVAILABLE:			
			volume_details_available += "%s, %s, %s, %s, %s, %s, %s, %s" %(volume.id, volume.state, volume.size, volume.volume_type, volume.iops, volume.create_time, volume.availability_zone, cost) + "\n"
			totalcost_available += cost
		else:
			volume_details_inuse += "%s, %s, %s, %s, %s, %s, %s, %s" %(volume.id, volume.state, volume.size, volume.volume_type, volume.iops, volume.create_time, volume.availability_zone, cost) + "\n"
			totalcost_inuse += cost

	if volumes == Constants.AWS_VOLUMES_ALL:
		# print "[INFO] Consider all volumes."
		volume_details_total = ", , , , , , , %s" %(totalcost_available + totalcost_inuse) + "\n"
		volume_details = volume_details + volume_details_available + volume_details_inuse		
	elif volumes == Constants.AWS_VOLUMES_AVAILABLE:
		# print "[INFO] Consider available volumes only."
		volume_details_total = ", , , , , , , %s" %(totalcost_available) + "\n"
		volume_details = volume_details + volume_details_available		
	else:
		# print "[INFO] Consider inuse volumes only."
		volume_details_total = ", , , , , , , %s" %(totalcost_inuse) + "\n"
		volume_details = volume_details + volume_details_inuse



	write_to_file(volume_details + volume_details_total, output_file)
################################################