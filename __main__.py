import pulumi

# Get the stack references for stackA and stackB
stack_vpc = pulumi.StackReference("Leeluworkshop/workshopvpc/vpc")
stack_ec2 = pulumi.StackReference("Leeluworkshop/workshopec2/ec2")

# Get the exported output values from stackA and stackB
vpcid = stack_vpc.get_output("vpc_id")
publicsubnetID=stack_vpc.get_output("public_subnet_id")
privatesubnetID=stack_vpc.get_output("private_subnet_id")

publicip = stack_ec2.get_output("public-instance-public-ip")
privateip = stack_ec2.get_output("private-instance-private-ip")
publicDNS = stack_ec2.get_output("public-DNS")
privateDNS = stack_ec2.get_output("private-DNS")

# Use the output values
pulumi.export("VPCid", vpcid)
pulumi.export("publicsubnetID", publicsubnetID)
pulumi.export("privatesubnetID", privatesubnetID)
pulumi.export("publicip", publicip)
pulumi.export("privateip",privateip)
pulumi.export("publicDNS",publicDNS)
pulumi.export("privateDNS",privateDNS)