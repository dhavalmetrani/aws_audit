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
	volume_details = "ID, State, Size, Type, IOPS, Created, Availability Zone, Monthly $\n"
	volume_details_available = ""
	volume_details_inuse = ""
	volume_details_total = ""
	totalcost_available = 0
	totalcost_inuse = 0	

	cost = 1
	print "[INFO] Computing Elastic Block storage volumes..."

	ec2 = boto3.client(Constants.AWS_EC2)
	for ec2_region in ec2.describe_regions()['Regions']:
		region_name = ec2_region['RegionName']
		print "[INFO] Considering region: " + region_name
		rds = boto3.client(Constants.AWS_RDS, region_name)

		# ec2_region_obj = get_aws_resource(Constants.AWS_EC2, region_name)
		ec2_region_obj = boto3.resource(Constants.AWS_EC2, region_name)
		for volume in ec2_region_obj.volumes.all():
			if not volume.iops:
				cost = volume.size * Constants.EBS_PRICE[volume.volume_type]
			else:
				cost = volume.size * Constants.EBS_PRICE_GP2_IOPS + volume.iops * Constants.EBS_PRICE_IOPS

			if volume.state == Constants.AWS_VOLUMES_AVAILABLE:			
				volume_details_available += "%s, %s, %s, %s, %s, %s, %s, %s" %(volume.id, volume.state, volume.size, volume.volume_type, volume.iops, volume.create_time, volume.availability_zone, cost) + "\n"
				totalcost_available += cost
				print "Available Volume [%s]\t ==> \t %s" %(volume.id, cost)						
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

	print "Total Cost ==> %s" % totalcost_available
	write_to_file(volume_details + volume_details_total, output_file)
	print "[INFO] Done. Computing Elastic Block storage volumes..."

################################################


################################################
# Parse AWS RDS
################################################
def prepare_aws_rds_report(output_file):
	rds_details = "Engine, Id, DB, Class, Status, Created, AZ, Secondary AZ, Monthly $\n"
	totalcost = 0
	cost = 1
	print "[INFO] Computing RDS resources..."

	ec2 = boto3.client(Constants.AWS_EC2)
	for ec2_region in ec2.describe_regions()['Regions']:
		region_name = ec2_region['RegionName']
		print "[INFO] Considering region: " + region_name
		rds = boto3.client(Constants.AWS_RDS, region_name)
		for rds_instance in rds.describe_db_instances()["DBInstances"]:
			# print_json(rds_instance)		
			rds_engine = rds_instance["Engine"]
			rds_db_name = rds_instance["DBName"]
			rds_db_instance_id = rds_instance["DBInstanceIdentifier"]		
			rds_db_instance_class = rds_instance["DBInstanceClass"]
			rds_db_instance_status = rds_instance["DBInstanceStatus"]
			rds_instance_creation_time = rds_instance["InstanceCreateTime"]
			rds_primary_az = rds_instance["AvailabilityZone"]
			rds_multi_az = rds_instance["MultiAZ"]
			if rds_multi_az == True:
				rds_secondary_az = rds_instance["SecondaryAvailabilityZone"]

			cost = Constants.AWS_RDS_PRICE[rds_engine + rds_db_instance_class] * 24 * 30
			totalcost += cost
			print "RDS [%s] \t ==> \t%s" %(rds_db_instance_id, cost)
			# print totalcost
			
			rds_details += "%s, %s, %s, %s, %s, %s, %s, %s, %s" %(rds_engine, rds_db_name, rds_db_instance_id, rds_db_instance_class, rds_db_instance_status, rds_instance_creation_time, rds_primary_az, rds_secondary_az, cost) + "\n"
			
			# raw_input('Enter your input:')

	rds_details_total = ", , , , , , , , %s" %(totalcost) + "\n"

	print "Total Cost ==> %s" % totalcost	
	write_to_file(rds_details + rds_details_total, output_file)
	print "[INFO] Done. Computing RDS resources..."

################################################

################################################
# Parse AWS RDS
################################################
def prepare_aws_rds_snapshot_report(output_file):	
	rds_snapshot_details = "DBInstanceIdentifier, DBSnapshotIdentifier, Engine, SnapshotCreateTime, Status, StorageType, AZ, AllocatedStorage, Monthly $\n"
	totalcost = 0
	cost = 1
	print "[INFO] Computing RDS snapshots..."

	ec2 = boto3.client(Constants.AWS_EC2)
	for ec2_region in ec2.describe_regions()['Regions']:
		region_name = ec2_region['RegionName']
		# print_json(ec2_region)
		print "[INFO] Considering region: " + region_name
		rds = boto3.client(Constants.AWS_RDS, region_name)
		for rds_snapshot in rds.describe_db_snapshots()["DBSnapshots"]:
			# print_json(rds_snapshot)

			rds_snapshot_db_id = rds_snapshot["DBInstanceIdentifier"]
			rds_snapshot_id = rds_snapshot["DBSnapshotIdentifier"]
			rds_snapshot_engine = rds_snapshot["Engine"]		
			rds_snapshot_creation_time = rds_snapshot["SnapshotCreateTime"]
			rds_snapshot_status = rds_snapshot["Status"]
			rds_snapshot_storage_type = rds_snapshot["StorageType"]
			rds_snapshot_az = rds_snapshot["AvailabilityZone"]
			rds_snapshot_storage = rds_snapshot["AllocatedStorage"]

			cost = Constants.AWS_EBS_SIZE * rds_snapshot_storage

			print "[INFO] RDS snapshot [%s]\t ==> %s" % (rds_snapshot_id, cost)
			totalcost += cost

			rds_snapshot_details += "%s, %s, %s, %s, %s, %s, %s, %s, %s" %(rds_snapshot_db_id, rds_snapshot_id, rds_snapshot_engine, rds_snapshot_creation_time, rds_snapshot_status, rds_snapshot_storage_type, rds_snapshot_az, rds_snapshot_storage, cost) + "\n"
		
	rds_snapshot_details_total = ", , , , , , , , %s" %(totalcost) + "\n"

	print "Total Cost ==> %s" % totalcost	
	write_to_file(rds_snapshot_details + rds_snapshot_details_total, output_file)
	print "[INFO] Done. Computing RDS snapshots..."

################################################


################################################
# Parse AWS EC2
################################################
def prepare_aws_ec2_report(output_file):
	ec2 = boto3.client(Constants.AWS_EC2)
	# ec2 = get_aws_resource(Constants.AWS_EC2)
	ec2_details = "Name, Id, Type, ImageId, LaunchTime, AZ, Public DNS, State, Monthly $\n"
	totalcost = 0
	cost = 1
	key_name = ""
	print "[INFO] Computing EC2 resources..."

	# for ec2_instance in ec2.instances.all():	

	for ec2_region in ec2.describe_regions()['Regions']:
		region_name = ec2_region['RegionName']
		print "[INFO] Considering region: " + region_name
		ec2_region_obj = boto3.client(Constants.AWS_EC2, region_name = region_name)
		for ec2_instance in ec2_region_obj.describe_instances()[Constants.AWS_EC2_RESERVATIONS]:
		# print_json(ec2_instance)
			for instance in ec2_instance[Constants.AWS_EC2_INSTANCES]:
				# print_json(instance)
				try:				
					key_name = instance[Constants.AWS_EC2_KEYNAME]
				except:
					key_name = ""
				instance_id = instance[Constants.AWS_EC2_INSTANCEID]
				instance_type = instance[Constants.AWS_EC2_INSTANCETYPE]
				image_id = instance[Constants.AWS_EC2_IMAGEID]
				launch_time = instance[Constants.AWS_EC2_LAUNCHTIME]
				availability_zone = instance[Constants.AWS_EC2_PLACEMENT][Constants.AWS_EC2_AVAILABILITYZONE]
				public_dns = instance[Constants.AWS_EC2_PUBLICDNSNAME]
				state = instance[Constants.AWS_EC2_STATE][Constants.AWS_EC2_NAME]
				if state == Constants.AWS_EC2_STATE_TERMINATED or state == Constants.AWS_EC2_STATE_STOPPED:
					continue
				try:
					tags = instance[Constants.AWS_EC2_TAGS]
				except:
					tags = key_name
				# platform = instance["Platform"]
				instance_count = 0
				try:
					instance_count = ACTUAL_INSTANCES[instance_type, availability_zone]
					ACTUAL_INSTANCES[instance_type,availability_zone] += 1
				except:
					ACTUAL_INSTANCES[instance_type, availability_zone] = 1

				cost = Constants.AWS_EC2_PRICE[instance_type] * 24 * 30
				totalcost += cost

				print "[EC2] Instance cost %s ==> %s" % (instance_id, cost)

				ec2_details += "%s, %s, %s, %s, %s, %s, %s, %s, %s " %(key_name, instance_id, instance_type, image_id, launch_time, availability_zone, public_dns, state, cost) + "\n"

	
	ec2_details_total = ", , , , , , , , %s" %(totalcost) + "\n"
	print "Total Cost ==> %s" % totalcost	
	write_to_file(ec2_details + ec2_details_total, output_file)
	print "[INFO] Done. Computing EC2 resources..."

################################################


################################################
# Parse AWS EC2 reserved instance report
################################################
def prepare_aws_ec2_reserved_report(output_file):
	ec2 = boto3.client(Constants.AWS_EC2)
	# ec2 = get_aws_resource(Constants.AWS_EC2)
	ec2_details = "InstanceType, InstanceCount, ProductDescription, ReservedInstancesId, AvailabilityZone, Duration (days), End, State, OfferingType\n"

	# reserved_report = "InstanceType, AvailabilityZone, ReserveCount, Actual Count, End, OfferingType\n"

	totalcost = 0
	cost = 1
	key_name = ""
	print "[INFO] Computing EC2 resources..."

	# for ec2_instance in ec2.instances.all():	

	for ec2_region in ec2.describe_regions()['Regions']:
		region_name = ec2_region['RegionName']
		print "[INFO] Considering region: " + region_name
		ec2_region_obj = boto3.client(Constants.AWS_EC2, region_name = region_name)
		
		for ec2_instance in ec2_region_obj.describe_reserved_instances()[Constants.AWS_EC2_RESERVED_INSTANCES]:
			# print_json(ec2_instance)
			print "[INFO] Considering reserved instance %s " % (ec2_instance["ReservedInstancesId"])

			instance_type = ec2_instance[Constants.AWS_EC2_INSTANCETYPE]
			instance_count = ec2_instance["InstanceCount"]
			instance_description = ec2_instance["ProductDescription"]
			instance_id = ec2_instance["ReservedInstancesId"]
			instance_az = ec2_instance["AvailabilityZone"]
			instance_duration = ec2_instance["Duration"]/(24*60*60)
			instance_end = ec2_instance["End"]
			instance_state = ec2_instance["State"]
			instance_offering_type = ec2_instance["OfferingType"]

			if instance_state == "retired": 
				continue

			RESERVED_INSTANCES[instance_type, instance_az] = instance_count

	# 			cost = Constants.AWS_EC2_PRICE[instance_type] * 24 * 30
	# 			totalcost += cost

	# 			print "[EC2] Instance cost %s ==> %s" % (instance_id, cost)

			ec2_details += "%s, %s, %s, %s, %s, %s, %s, %s, %s" %(instance_type, instance_count, instance_description, instance_id, instance_az, instance_duration, instance_end, instance_state, instance_offering_type) + "\n"
			# reserved_report += "%s, %s, %s, %s, %s, %s" %(instance_type, instance_az, instance_count, ACTUAL_INSTANCES[instance_type + instance_az], instance_end, instance_offering_type) + "\n"

	
	# ec2_details_total = ", , , , , , , , %s" %(totalcost) + "\n"
	# print "Total Cost ==> %s" % totalcost	
	write_to_file(ec2_details, output_file)
	print "[INFO] Done. Computing reserved EC2 resources..."

################################################



################################################
# Parse AWS EC2 reserved instance report
################################################
def prepare_aws_ec2_reserved_actual_report(output_file):
	reserved_report = "InstanceType, AvailabilityZone, ReserveCount, Actual Count\n"
	print "[INFO] Computing EC2 resources..."
	parsed = False

	# print RESERVED_INSTANCES.items()
	# print ACTUAL_INSTANCES

	# for key_tuple_reserved in RESERVED_INSTANCES.keys():
	# 	print key_tuple_reserved

	for key_tuple_actual in ACTUAL_INSTANCES.keys():
		parsed = False
		# print key_tuple_actual	
		for key_tuple_reserved in RESERVED_INSTANCES.keys():
			if key_tuple_actual == key_tuple_reserved:
				# print key_tuple_actual
				parsed = True
				reserved_report += "%s, %s, %s, %s" %(key_tuple_actual[0], key_tuple_actual[1], RESERVED_INSTANCES[key_tuple_actual[0], key_tuple_actual[1]], ACTUAL_INSTANCES[key_tuple_actual[0], key_tuple_actual[1]]) + "\n"
		# 	else:
		# 		reserved_report += "%s, %s, %s, %s" %(key_tuple_actual[0], key_tuple_actual[1], "0", ACTUAL_INSTANCES[key_tuple_actual[0], key_tuple_actual[1]]) + "\n"

		if not parsed:
			reserved_report += "%s, %s, %s, %s" %(key_tuple_actual[0], key_tuple_actual[1], "0", ACTUAL_INSTANCES[key_tuple_actual[0], key_tuple_actual[1]]) + "\n"

	# for 
	
	# reserved_report += "%s, %s, %s, %s, %s, %s" %(instance_type, instance_az, instance_count, ACTUAL_INSTANCES[instance_type + instance_az], instance_end, instance_offering_type) + "\n"

	# write_to_file(ec2_details, output_file)
	write_to_file(reserved_report, output_file)
	print "[INFO] Done. Computing reserved EC2 resources..."

################################################