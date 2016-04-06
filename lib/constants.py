
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

	OUTPUT_FOLDER = "output"
	OUTPUT_FILE = "output.csv"
	OUTPUT_FORMAT = ".csv"