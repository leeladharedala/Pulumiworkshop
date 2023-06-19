import pulumi
import pulumi_aws as aws
from pulumi_aws import ec2

Stack_vpc=pulumi.StackReference(f"Leeluworkshop/workshopvpc/vpc")
vpcid=Stack_vpc.get_output("vpc_id")
publicsubnetIDs=Stack_vpc.get_output("public_subnet_id")
privatesubnetIDs=Stack_vpc.get_output("private_subnet_id")

# Create a security group for the public EC2 instance
public_sg = ec2.SecurityGroup(
    "public-security-group",
    vpc_id=vpcid,
    ingress=[
        ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=22,
            to_port=22,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ],
    egress=[
        ec2.SecurityGroupEgressArgs(
            protocol="-1",
            from_port=0,
            to_port=0,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ]
)

# Create a security group for the private EC2 instance
private_sg = ec2.SecurityGroup(
    "private-security-group",
    vpc_id=vpcid,
)

# Allow inbound SSH traffic from the public security group to the private security group
ec2.SecurityGroupRule(
    "private-ssh-rule",
    type="ingress",
    security_group_id=private_sg.id,
    source_security_group_id=public_sg.id,
    protocol="tcp",
    from_port=22,
    to_port=22,
)

# Create a public EC2 instance
public_instance = ec2.Instance(
    "public-instance",
    instance_type="t2.micro",
    ami="ami-0e820afa569e84cc1",
    associate_public_ip_address="True",
    key_name="Pulumi_Test",
    subnet_id=publicsubnetIDs,
    vpc_security_group_ids=[public_sg.id],
)

# Create a private EC2 instance
private_instance = ec2.Instance(
    "private-instance",
    instance_type="t2.micro",
    ami="ami-0e820afa569e84cc1",
    key_name="Pulumi_Test",
    subnet_id=privatesubnetIDs,
    vpc_security_group_ids=[private_sg.id],
)

# Export the public IP address of the public instance
pulumi.export("public-instance-public-ip",public_instance.public_ip)

#Export public DNS
pulumi.export("public-DNS",public_instance.public_dns)

# Export the private IP address of the private instance
pulumi.export("private-instance-private-ip", private_instance.private_ip)

# Export private DNS
pulumi.export("private-DNS",private_instance.private_dns)
