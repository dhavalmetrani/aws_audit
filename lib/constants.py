
class Constants:
	# Monthly price for EBS volumes
	EBS_PRICE = {}
	EBS_PRICE["standard"] = 0.05
	EBS_PRICE["gp2"] = 0.10


	EBS_PRICE_IOPS = 0.065
	EBS_PRICE_GP2_IOPS = 0.125


	# Hourly price for RDS instances:
	RDS_MYSQL = "mysql"
	RDS_PRICE = {}
	RDS_PRICE[RDS_MYSQL + "db.t1.micro"] = 0.050
	RDS_PRICE[RDS_MYSQL + "db.m1.small"] = 0.110
	RDS_PRICE[RDS_MYSQL + "db.m1.medium"] = 0.230
	RDS_PRICE[RDS_MYSQL + "db.m1.large"] = 0.460
	RDS_PRICE[RDS_MYSQL + "db.m1.xlarge"] = 0.930
	RDS_PRICE[RDS_MYSQL + "db.m2.xlarge"] = 0.660
	RDS_PRICE[RDS_MYSQL + "db.m2.2xlarge"] = 1.320
	RDS_PRICE[RDS_MYSQL + "db.m2.4xlarge"] = 2.640


	RDS_PRICE[RDS_MYSQL + "db.t2.micro"]	= 0.017
	RDS_PRICE[RDS_MYSQL + "db.t2.small"]	= 0.034
	RDS_PRICE[RDS_MYSQL + "db.t2.medium"]	= 0.068
	RDS_PRICE[RDS_MYSQL + "db.t2.large"]	= 0.136
	RDS_PRICE[RDS_MYSQL + "db.m4.large"]	= 0.175
	RDS_PRICE[RDS_MYSQL + "db.m4.xlarge"]	= 0.350
	RDS_PRICE[RDS_MYSQL + "db.m4.2xlarge"]	= 0.700
	RDS_PRICE[RDS_MYSQL + "db.m4.4xlarge"]	= 1.401
	RDS_PRICE[RDS_MYSQL + "db.m4.10xlarge"]	= 3.502
	RDS_PRICE[RDS_MYSQL + "db.m3.medium"] = 0.090
	RDS_PRICE[RDS_MYSQL + "db.m3.large"]	= 0.185
	RDS_PRICE[RDS_MYSQL + "db.m3.xlarge"]	= 0.370
	RDS_PRICE[RDS_MYSQL + "db.m3.2xlarge"]	= 0.740
	
	RDS_PRICE[RDS_MYSQL + "db.r3.large"]	= 0.240
	RDS_PRICE[RDS_MYSQL + "db.r3.xlarge"]	= 0.475
	RDS_PRICE[RDS_MYSQL + "db.r3.2xlarge"]	= 0.945
	RDS_PRICE[RDS_MYSQL + "db.r3.4xlarge"]	= 1.890
	RDS_PRICE[RDS_MYSQL + "db.r3.8xlarge"]	= 3.780


	AWS_EC2 = "ec2"
	AWS_EC2_VOLUME = "ec2_volumes"
	AWS_RDS = "rds"
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