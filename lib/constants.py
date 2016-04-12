
class Constants:
	# Monthly price for EBS volumes
	EBS_PRICE = {}
	EBS_PRICE["standard"] = 0.05
	EBS_PRICE["gp2"] = 0.10


	EBS_PRICE_IOPS = 0.065
	EBS_PRICE_GP2_IOPS = 0.125


	# Hourly price for RDS instances:
	AWS_RDS_MYSQL = "mysql"
	AWS_RDS_PRICE = {}
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.t1.micro"] = 0.050
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m1.small"] = 0.110
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m1.medium"] = 0.230
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m1.large"] = 0.460
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m1.xlarge"] = 0.930
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m2.xlarge"] = 0.660
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m2.2xlarge"] = 1.320
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m2.4xlarge"] = 2.640


	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.t2.micro"]	= 0.017
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.t2.small"]	= 0.034
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.t2.medium"]	= 0.068
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.t2.large"]	= 0.136
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m4.large"]	= 0.175
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m4.xlarge"]	= 0.350
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m4.2xlarge"]	= 0.700
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m4.4xlarge"]	= 1.401
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m4.10xlarge"]	= 3.502
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m3.medium"] = 0.090
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m3.large"]	= 0.185
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m3.xlarge"]	= 0.370
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.m3.2xlarge"]	= 0.740
	
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.r3.large"]	= 0.240
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.r3.xlarge"]	= 0.475
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.r3.2xlarge"]	= 0.945
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.r3.4xlarge"]	= 1.890
	AWS_RDS_PRICE[AWS_RDS_MYSQL + "db.r3.8xlarge"]	= 3.780


	AWS_EC2_STATE_PENDING = "pending"
	AWS_EC2_STATE_RUNNING = "running"
	AWS_EC2_STATE_SHUTTING_DOWN = "shutting-down"
	AWS_EC2_STATE_TERMINATED = "terminated"
	AWS_EC2_STATE_STOPPING = "stopping"
	AWS_EC2_STATE_STOPPED = "stopped"

	AWS_EC2_INSTANCE_STATE = {}
	AWS_EC2_INSTANCE_STATE[AWS_EC2_STATE_PENDING] = 0
	AWS_EC2_INSTANCE_STATE[AWS_EC2_STATE_RUNNING] = 1
	AWS_EC2_INSTANCE_STATE[AWS_EC2_STATE_SHUTTING_DOWN] = 3
	AWS_EC2_INSTANCE_STATE[AWS_EC2_STATE_TERMINATED] = 4
	AWS_EC2_INSTANCE_STATE[AWS_EC2_STATE_STOPPING] = 6
	AWS_EC2_INSTANCE_STATE[AWS_EC2_STATE_STOPPED] = 8

	AWS_EC2_RESERVATIONS = "Reservations"
	AWS_EC2_RESERVED_INSTANCES = "ReservedInstances"
	AWS_EC2_INSTANCES = "Instances"
	AWS_EC2_KEYNAME = "KeyName"
	AWS_EC2_INSTANCEID = "InstanceId"
	AWS_EC2_INSTANCETYPE = "InstanceType"
	AWS_EC2_IMAGEID	 = "ImageId"
	AWS_EC2_LAUNCHTIME = "LaunchTime"
	AWS_EC2_AVAILABILITYZONE = "AvailabilityZone"
	AWS_EC2_PUBLICDNSNAME = "PublicDnsName"
	AWS_EC2_STATE = "State"
	AWS_EC2_NAME = "Name"
	AWS_EC2_TAGS = "Tags"
	AWS_EC2_PLACEMENT = "Placement"

	AWS_EC2_PRICE = {}

	AWS_EC2_PRICE["t2.nano"] =  0.0065
	AWS_EC2_PRICE["t2.micro"] = 0.013
	AWS_EC2_PRICE["t2.small"] = 0.026
	AWS_EC2_PRICE["t2.medium"] = 0.052
	AWS_EC2_PRICE["t2.large"] = 0.104
	AWS_EC2_PRICE["m4.large"] =  0.12
	AWS_EC2_PRICE["m4.xlarge"] = 0.239
	AWS_EC2_PRICE["m4.2xlarge"] = 0.479
	AWS_EC2_PRICE["m4.4xlarge"] =  0.958
	AWS_EC2_PRICE["m4.10xlarge"] =  2.394
	AWS_EC2_PRICE["m3.medium"] =  0.067
	AWS_EC2_PRICE["m3.large"] = 0.133
	AWS_EC2_PRICE["m3.xlarge"] = 0.266
	AWS_EC2_PRICE["m3.2xlarge"] = 0.532
	AWS_EC2_PRICE["c4.large"] =  0.105
	AWS_EC2_PRICE["c4.xlarge"] =  0.209
	AWS_EC2_PRICE["c4.2xlarge"] = 0.419
	AWS_EC2_PRICE["c4.4xlarge"] = 0.838
	AWS_EC2_PRICE["c4.8xlarge"] = 1.675
	AWS_EC2_PRICE["c3.large"] =  0.105
	AWS_EC2_PRICE["c3.xlarge"] =  0.21
	AWS_EC2_PRICE["c3.2xlarge"] = 0.42
	AWS_EC2_PRICE["c3.4xlarge"] = 0.84
	AWS_EC2_PRICE["c3.8xlarge"] = 1.68
	AWS_EC2_PRICE["g2.2xlarge"] = 0.65
	AWS_EC2_PRICE["g2.8xlarge"] = 2.6
	AWS_EC2_PRICE["r3.large"] =  0.166
	AWS_EC2_PRICE["r3.xlarge"] =  0.333
	AWS_EC2_PRICE["r3.2xlarge"] = 0.665
	AWS_EC2_PRICE["r3.4xlarge"] = 1.33
	AWS_EC2_PRICE["r3.8xlarge"] = 2.66
	AWS_EC2_PRICE["i2.xlarge"] =  0.853
	AWS_EC2_PRICE["i2.2xlarge"] = 1.705
	AWS_EC2_PRICE["i2.4xlarge"] = 3.41
	AWS_EC2_PRICE["i2.8xlarge"] = 6.82
	AWS_EC2_PRICE["d2.xlarge"] =  0.69
	AWS_EC2_PRICE["d2.2xlarge"] =  1.38
	AWS_EC2_PRICE["d2.4xlarge"] =  2.76
	AWS_EC2_PRICE["d2.8xlarge"] =  5.52

	AWS_EC2_PRICE["m1.small"] =  0.044
	AWS_EC2_PRICE["m1.medium"] =  0.087
	AWS_EC2_PRICE["m1.large"] =  0.175
	AWS_EC2_PRICE["m1.xlarge"] = 0.35
	AWS_EC2_PRICE["c1.medium"] =  0.13
	AWS_EC2_PRICE["c1.xlarge"] = 0.52
	AWS_EC2_PRICE["cc2.8xlarge"] = 2
	AWS_EC2_PRICE["cg1.4xlarge"] = 2.1
	AWS_EC2_PRICE["m2.xlarge"] = 0.245
	AWS_EC2_PRICE["m2.2xlarge"] = 0.49
	AWS_EC2_PRICE["m2.4xlarge"] = 0.98
	AWS_EC2_PRICE["cr1.8xlarge"] = 3.5
	AWS_EC2_PRICE["hi1.4xlarge"] = 3.1
	AWS_EC2_PRICE["hs1.8xlarge"] = 4.6
	AWS_EC2_PRICE["t1.micro"] = 0.02


	AWS_EBS_SIZE = 0.095

	AWS_EC2 = "ec2"
	AWS_EC2_RI = "ec2_reserved_instances"
	AWS_EC2_RAI = "ec2_reserved_actual_instances"
	AWS_EC2_VOLUME = "ec2_volumes"
	AWS_RDS = "rds"
	AWS_RDS_SNAPSHOTS = "rds_snapshots"
	AWS_PROFILE_DEFAULT = "default"

	AWS_VOLUMES_ALL = "all"
	AWS_VOLUMES_AVAILABLE = "available"
	AWS_VOLUMES_INUSE = "inuse"
	AWS_VOLUMES_TO_CONSIDER = "volumes_to_consider"

	AWS_PROFILES = "aws_profiles"
	AWS_PROFILE_ID = "id"
	AWS_PROFILE = "aws_profile"

	OUTPUT_FOLDER = "output"
	OUTPUT_FILE = "output.csv"
	OUTPUT_FORMAT = ".csv"