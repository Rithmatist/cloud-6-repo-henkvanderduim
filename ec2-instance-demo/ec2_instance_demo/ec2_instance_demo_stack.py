# from aws_cdk import App
#from aws_cdk import (
#        core,
#    aws_ec2 as ec2,
#)
import aws_cdk as core
from aws_cdk import aws_ec2 as ec2

vpcID="<VPC-ID>"
instanceName="webserver-1"
instanceType="t2.micro"
amiName="amzn2-ami-hvm-2.0.20200520.1-x86_64-gp2"


class Ec2InstanceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        # lookup existing VPC
        vpc = ec2.Vpc.from_lookup(
            self,
            "vpc",
            vpc_id=vpcID,
        )
        
        # create a new security group
        sec_group = ec2.SecurityGroup(
            self,
            "sec-group-allow-ssh",
            vpc=vpc,
            allow_all_outbound=True,
        )

        # add a new ingress rule to allow port 22 to internal hosts
        sec_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('10.0.0.0/16'),
            description="Allow SSH connection", 
            connection=ec2.Port.tcp(22)
        )

        # define a new ec2 instance
        ec2_instance = ec2.Instance(
            self,
            "ec2-instance",
            instance_name=instanceName,
            instance_type=ec2.InstanceType(instanceType),
            machine_image=ec2.MachineImage().lookup(name=amiName),
            vpc=vpc,
            security_group=sec_group,
        )
