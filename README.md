# Pulumiworkshop
 Public and Private network
 This code creates public and private instances from local using pulumi. No need to use console for creating instances
1. Create a new directory and run pulumi new aws-python 
2. Create a new subdirectory, Name it as VPC and run pulumi new aws-python
3. Copy the __main__.py code in vpc folder and upload it using pulumi up
4. Create a new subdirectory, Name it as EC2 and run pulumi new aws-python
5. Copy the __main__.py code in ec2 folder and upload it using pulumi up
6. Copy the __main__.py code in main folder and upload it using pulumi up
7. You will get public DNS as output
8. Now login to created instance in terminal using ssh with following command: ssh -i "key_file_name.pem" publicDNS address
Ex: ssh -i "Pulumi_Test.pem" ec2-user@ec2-52-14-67-180.us-east-2.compute.amazonaws.com
9.  Open a new terminal and copy the .pem file using scp with following command: scp -i "key_file_name.pem" key_file_name.pem publicDNS address:/home/ec2-user
Ex: scp -i "Pulumi_Test.pem" Pulumi_Test.pem ec2-user@ec2-52-14-67-180.us-east-2.compute.amazonaws.com:/home/ec2-user 
10. Now open previous terminal make the .pem file readable using chmod 400 filename.pem 
11. Now Login to private network using ssh and private DNS using following command: ssh -i filename.pem PrivateDNS
Ex: ssh -i Pulumi_Test.pem ip-10-31-1-109.us-east-2.compute.internal
