import pulumi
import pulumi_aws as aws

# Create a new VPC
vpc = aws.ec2.Vpc("my-vpc",
    cidr_block="10.31.0.0/16",
    enable_dns_support=True,
    enable_dns_hostnames=True)

# Create a Internet gateway within VPC
internetgateway = aws.ec2.InternetGateway("internetgateway",
    vpc_id=vpc.id
    )

# Attach gateway to route
route = aws.ec2.RouteTable("route",
    vpc_id=vpc.id,
    routes=[
        aws.ec2.RouteTableRouteArgs(
            cidr_block="0.0.0.0/0",
            gateway_id=internetgateway.id,
        )])

# Create a public subnet within the VPC
public_subnet = aws.ec2.Subnet("public-subnet",
    vpc_id=vpc.id,
    cidr_block="10.31.0.0/24",
    availability_zone="us-east-2a",
    )

# Create a private subnet within the VPC
private_subnet = aws.ec2.Subnet("private-subnet",
    vpc_id=vpc.id,
    cidr_block="10.31.1.0/24",
    availability_zone="us-east-2a")

# Associate public subnet to route
route_table_association_public = aws.ec2.RouteTableAssociation("routeTableAssociationpublic",
    subnet_id=public_subnet.id,
    route_table_id=route.id)

# Associate private subnet to route
route_table_association_private = aws.ec2.RouteTableAssociation("routeTableAssociationprivate",
    subnet_id=private_subnet.id,
    route_table_id=route.id)

pulumi.export("vpc_id", vpc.id)
pulumi.export("public_subnet_id", public_subnet.id)
pulumi.export("private_subnet_id", private_subnet.id)
pulumi.export("route id",route.id)
