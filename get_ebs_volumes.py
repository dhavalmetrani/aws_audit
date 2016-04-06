
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
	parser.add_argument("-ap", "--aws-profile", help="Provide name of AWS profile")	
	# parser.add_argument("-o", "--output-file", help="Provide path to output file")	
	# parser.add_argument("-ac", "--aws-config", help="Provide name of json file containing AWS configs")
	args = parser.parse_args()
	aws_profile = args.aws_profile

	if not aws_profile:
		aws_profile = Constants.AWS_PROFILE_DEFAULT
	# if not output_file:
	# 	output_file = Constants.OUTPUT_FILE

	output_file = aws_profile + Constants.OUTPUT_FORMAT


	print "[INFO] Using AWS profile: " + aws_profile

	use_profile(aws_profile)

	now = datetime.datetime.now()
	output_folder = "./" + Constants.OUTPUT_FOLDER + "/" + "%s" % now
	create_folder(output_folder)
	output_file = os.path.join(output_folder, output_file)
	
	
	# prepare_aws_ebs_volume_report(output_file, volumes=Constants.AWS_VOLUMES_ALL)
	# prepare_aws_ebs_volume_report(output_file, volumes=Constants.AWS_VOLUMES_INUSE)
	prepare_aws_ebs_volume_report(output_file, volumes=Constants.AWS_VOLUMES_AVAILABLE)

	print "[INFO] Done. Output: " + output_file
	# print volume_details

	send_email()



################################################
if __name__ == "__main__":
	main(sys.argv[1:])
################################################