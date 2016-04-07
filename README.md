# AWS Auditor
User story: 

I. Write a tool which would: 
1. For every AWS root account, have baseline for number of EC2 instances, RDS instances, EBS volumes, etc.
2. Get the number of instances for EC2, RDS, EBS, etc.
3. Based on the price of EC2, RDS, S3, etc, get the total cost of existing resources.
4. Get the number of redundant instances for these services.
5. Based on this, get the cost of redundant instances per month.


{
	"aws_profiles":
	[
		{
			"id":"spsdev",
			"aws_profile":"spsdev-aws_paas_auditor_readonly",
			"volumes_to_consider":"available",
			"_comments":"available, inuse, all"
		},
		{
			"id":"a360",
			"aws_profile":"a360-aws_paas_auditor_readonly",
			"volumes_to_consider":"available",
			"_comments":"available, inuse, all"
		},
		{
			"id":"default",
			"aws_profile":"default",
			"volumes_to_consider":"available" 
		}
	]
}