
################################################
import smtplib
import traceback
import os

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
def send_email(sender = 'dhaval.metrani@autodesk.com', receivers = ['dhaval.metrani@autodesk.com']):

	message = """From: From Dhaval Metrani <dhaval.metrani@autodesk.com>
	To: To Dhaval Metrani <dhaval.metrani@autodesk.com>
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


