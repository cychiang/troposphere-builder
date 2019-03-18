from troposphere_builder.cloud_formation_builder import CloudFormationBuilder
from troposphere import ec2, Ref, Output


class TemplateServiceVPC(object):
    def __init__(self):
        """init CloudFormationBuilder"""
        self.builder = CloudFormationBuilder()
        """init description and metadata"""
        self.description = None
        self.metadata = None
        """init resources"""
        self.internet_gateway = None
        self.vpc = None
        self.vpc_gateway_attachment = None
        self.vpc_network_acl = None
        self.inbound_rule = None
        self.outbound_rule = None
        """init outputs"""
        self.output_internet_gateway = None
        self.output_vpc_id = None

    def construct_template(self, **kwargs):
        """
        :param kwargs: See below
        :keyword Arguments:
            * *Description* (``str``) --
              Add description to the CloudFormation
            * *Metadata* (``dict``) --
              Add metadata to the CloudFormation
        """
        self.description = kwargs.get('Description', 'Service VPC')
        self.metadata = kwargs.get('Metadata', {
            'DependsOn': [],
            'Environment': 'Development',
            'StackName': 'Development-VPC'
        })

        self.__set_description()
        self.__set_metadata()
        self.__set_resources()
        self.__set_outputs()

    def __set_description(self):
        self.builder.configure_description(self.description)

    def __set_metadata(self):
        self.builder.configure_metadata(self.metadata)

    def __set_resources(self):
        self.resources = []
        """Configure InternetGateway"""
        self.internet_gateway = ec2.InternetGateway(
            'InternetGateway',
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': f'{self.metadata["Environment"]}'
                },
                {
                    'Key': 'Name',
                    'Value': f'{self.metadata["Environment"]}-InternetGateway'
                }
            ]
        )
        """Configure VPC"""
        self.vpc = ec2.VPC(
            'VPC',
            CidrBlock='10.0.0.0/16',
            EnableDnsHostnames=True,
            EnableDnsSupport=True,
            InstanceTenancy='default',
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': f'{self.metadata["Environment"]}'
                },
                {
                    'Key': 'Name',
                    'Value': f'{self.metadata["Environment"]}-ServiceVPC'
                }
            ]
        )
        """Configure VpcGatewayAttachment"""
        self.vpc_gateway_attachment = ec2.VPCGatewayAttachment(
            'VpcGatewayAttachment',
            InternetGatewayId=Ref(self.internet_gateway),
            VpcId=Ref(self.vpc)
        )
        """Configure VpcNetworkAcl"""
        self.vpc_network_acl = ec2.NetworkAcl(
            'VpcNetworkAcl',
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': f'{self.metadata["Environment"]}'
                },
                {
                    'Key': 'Name',
                    'Value': f'{self.metadata["Environment"]}-NetworkAcl'
                }
            ],
            VpcId=Ref(self.vpc)
        )
        """Configure VpcNetworkAclInboundRule"""
        self.inbound_rule = ec2.NetworkAclEntry(
            'VpcNetworkAclInboundRule',
            CidrBlock='0.0.0.0/0',
            Egress=False,
            NetworkAclId=Ref(self.vpc_network_acl),
            PortRange=ec2.PortRange(
                From='443',
                To='443'
            ),
            Protocol='6',
            RuleAction='allow',
            RuleNumber=100
        )
        """Configure VpcNetworkAclOutboundRule"""
        self.outbound_rule = ec2.NetworkAclEntry(
            'VpcNetworkAclOutboundRule',
            CidrBlock='0.0.0.0/0',
            Egress=True,
            NetworkAclId=Ref(self.vpc_network_acl),
            Protocol='6',
            RuleAction='allow',
            RuleNumber=200
        )
        """Append all resources to list"""
        self.resources.append(self.internet_gateway)
        self.resources.append(self.vpc)
        self.resources.append(self.vpc_gateway_attachment)
        self.resources.append(self.vpc_network_acl)
        self.resources.append(self.inbound_rule)
        self.resources.append(self.outbound_rule)
        """Configure builder with resources"""
        self.builder.configure_resources(self.resources)

    def __set_outputs(self):
        self.outputs = []
        """Configure Output InternetGateway"""
        self.output_internet_gateway = Output(
            'InternetGateway',
            Value=Ref(self.internet_gateway)
        )
        """Configure Output VPCID"""
        self.output_vpc_id = Output(
            'VPCID',
            Value=Ref(self.vpc)
        )
        """Append all resources to list"""
        self.outputs.append(self.output_internet_gateway)
        self.outputs.append(self.output_vpc_id)
        """Configure builder with outputs"""
        self.builder.configure_outputs(self.outputs)

    def add_resource(self, resource):
        """Add additional resource to the builder"""
        self.builder.add_resource(resource)

    def add_output(self, output):
        """Add additional output to the builder"""
        self.builder.add_output(output)

    @property
    def cloud_formation(self):
        return self.builder.cloud_formation
