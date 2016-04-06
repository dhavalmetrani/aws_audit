################################################
import smtplib
import traceback
import os
import os.path
import json

################################################

################################################
# Write content to file
################################################
def write_to_file(content, file_name):
	text_file = open(file_name, "w")
	text_file.write(content)
	text_file.close()
################################################

################################################
# Send email message
################################################
def send_email(sender = 'dhavalmetrani@gmail.com', receivers = ['dhavalmetrani@gmail.com']):

	message = """From: From Dhaval Metrani <dhavalmetrani@gmail.com>
	To: To Dhaval Metrani <dhavalmetrani@gmail.com>
	Subject: AWS Audit report
	AWS Audit report is ready.
	"""

	try:
		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message)         
		print "Successfully sent email"
	except:
		print "[WARNING]: Unable to send email."
		# traceback.print_exc()

################################################


################################################
# Create folder
################################################
def create_folder(folder_path):
	os.makedirs(folder_path)
################################################


################################################
# Check if file exists
################################################
def file_exists(file_path):	
	return os.path.isfile(file_path) 
################################################


################################################
# load json file
################################################
def load_json(file_path):	
	with open(file_path) as data_file:
		data = json.load(data_file)
	return data
################################################

