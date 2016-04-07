
class Constants:
	EBS_PRICE = {}
	EBS_PRICE["standard"] = 0.05
	EBS_PRICE["gp2"] = 0.10


	EBS_PRICE_IOPS = 0.065
	EBS_PRICE_GP2_IOPS = 0.125

	AWS_EC2 = "ec2"
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