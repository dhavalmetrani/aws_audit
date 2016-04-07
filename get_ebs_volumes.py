
################################################
__author__ = "Dhaval Mertani"
__copyright__ = "Copyright 2016"
__credits__ = ["Dhaval Metrani"]
__license__ = "License"
__version__ = "1.0.0"
__maintainer__ = "Dhaval Metrani"
__email__ = "dhavalmetrani@gmail.com"
__status__ = "Prototype"
################################################



################################################
import argparse, sys
import datetime, os
################################################
import boto3
# import botocore.session
################################################
from lib.constants import *
from lib.aws_util import *
from lib.util import *
################################################


################################################
def main(argv):

	parser = argparse.ArgumentParser()
	# parser.add_argument("-ap", "--aws-profile", help="Provide name of AWS profile")	
	# parser.add_argument("-o", "--output-file", help="Provide path to output file")	
	parser.add_argument("-ac", "--aws-config", help="Provide name of json file containing AWS configs")
	args = parser.parse_args()
	aws_config = args.aws_config
	error_msg = ""

	if not aws_config:
		error_msg = "[ERROR] Please pass value for config file."
	elif not file_exists(aws_config):
		error_msg = "[ERROR] File %s does not exist." % aws_config
		# aws_config = Constants.AWS_config_DEFAULT
	# if not output_file:
	# 	output_file = Constants.OUTPUT_FILE
	if error_msg:
		print error_msg
		sys.exit(1)


	print "[INFO] Using AWS config: " + aws_config

	json_data = load_json(aws_config)

	output_folder = create_output_folder()

	# print json_data['ebs_volumes'][0]['aws_profile']
	# print json_data['ebs_volumes'][1]['aws_profile']

	parse_aws_profiles(json_data, output_folder)

	# # prepare_aws_ebs_volume_report(output_file, volumes=Constants.AWS_VOLUMES_ALL)
	# # prepare_aws_ebs_volume_report(output_file, volumes=Constants.AWS_VOLUMES_INUSE)
	# prepare_aws_ebs_volume_report(output_file, volumes=Constants.AWS_VOLUMES_AVAILABLE)

	# print "[INFO] Done. Output: " + output_file
	# # print volume_details

	send_email()
################################################

################################################
# Create output folser
################################################
def create_output_folder():
	now = datetime.datetime.now()
	output_folder = "./" + Constants.OUTPUT_FOLDER + "/" + "%s" % now
	create_folder(output_folder)
	return output_folder

################################################


################################################
# Parse EBS volumes
################################################
def parse_aws_profiles(json_data, output_folder):
	for aws_profile_entry in json_data[Constants.AWS_PROFILES]:
		aws_profile_id = aws_profile_entry[Constants.AWS_PROFILE_ID]
		aws_profile = aws_profile_entry[Constants.AWS_PROFILE]
		volumes_to_consider = aws_profile_entry[Constants.AWS_VOLUMES_TO_CONSIDER]
		print "Processing for profile: " + aws_profile_id

		if use_profile(aws_profile):
			output_file = aws_profile_id
			output_file = os.path.join(output_folder, output_file)
			prepare_aws_ebs_volume_report(output_file + "-" + Constants.AWS_EC2_VOLUME + Constants.OUTPUT_FORMAT, volumes_to_consider)
			prepare_aws_rds_report(output_file + "-" + Constants.AWS_RDS + Constants.OUTPUT_FORMAT)

			print "[INFO] Done. Output: " + output_folder
		else:
			print "[ERROR] AWS profile %s does not exist. Skipping. " %aws_profile
################################################

################################################
if __name__ == "__main__":
	main(sys.argv[1:])
################################################