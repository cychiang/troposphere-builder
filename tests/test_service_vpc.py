import unittest
import json
from troposphere_builder.templates.template_service_vpc import TemplateServiceVPC
from troposphere import ec2, Output, Ref


class TestTemplateServiceVPC(unittest.TestCase):
    """Test template_service_vpc.py"""

    def test_create_template_service_vpc(self):
        """Test result from template_service_vpc.cloud_formation"""
        template_service_vpc = TemplateServiceVPC()
        self.assertEqual(
            str(template_service_vpc.cloud_formation),
            json.dumps(dict({"Resources": {}}), indent=4,
                       sort_keys=True, separators=(',', ': '))
        )

    def test_construct_default_template_service_vpc(self):
        """
        Test result from template_service_vpc.construct_template() with default value.
        Default values:
          - Description: "Service VPC"
          - Metadata: {
                "DependsOn": [],
                "Environment": "Development",
                "StackName": "Development-VPC"
            }
        """
        template_service_vpc = TemplateServiceVPC()
        template_service_vpc.construct_template()
        self.assertEqual(
            str(template_service_vpc.cloud_formation),
            json.dumps(dict(
                {
                    "Description": "Service VPC",
                    "Metadata": {
                        "DependsOn": [],
                        "Environment": "Development",
                        "StackName": "Development-VPC"
                    },
                    "Outputs": {
                        "InternetGateway": {
                            "Value": {
                                "Ref": "InternetGateway"
                            }
                        },
                        "VPCID": {
                            "Value": {
                                "Ref": "VPC"
                            }
                        }
                    },
                    "Resources": {
                        "InternetGateway": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-InternetGateway"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::InternetGateway"
                        },
                        "VPC": {
                            "Properties": {
                                "CidrBlock": "10.0.0.0/16",
                                "EnableDnsHostnames": "true",
                                "EnableDnsSupport": "true",
                                "InstanceTenancy": "default",
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-ServiceVPC"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::VPC"
                        },
                        "VpcGatewayAttachment": {
                            "Properties": {
                                "InternetGatewayId": {
                                    "Ref": "InternetGateway"
                                },
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::VPCGatewayAttachment"
                        },
                        "VpcNetworkAcl": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-NetworkAcl"
                                    }
                                ],
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::NetworkAcl"
                        },
                        "VpcNetworkAclInboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "false",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "PortRange": {
                                    "From": "443",
                                    "To": "443"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 100
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        },
                        "VpcNetworkAclOutboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "true",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 200
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        }
                    }
                }
            ), indent=4, sort_keys=True, separators=(',', ': '))
        )

    def test_construct_custom_template_service_vpc(self):
        """
        Test result from template_service_vpc.construct_template() with custom values
        Custom values:
          - Description: "My Service VPC"
          - Metadata: {
                "DependsOn": [],
                "Environment": "Production",
                "StackName": "Production-VPC"
            }
        """
        template_service_vpc = TemplateServiceVPC()
        template_service_vpc.construct_template(
            Metadata={
                'DependsOn': [],
                'Environment': 'Production',
                'StackName': 'Production-VPC'
            },
            Description='My Service VPC'
        )
        self.assertEqual(
            str(template_service_vpc.cloud_formation),
            json.dumps(dict(
                {
                    "Description": "My Service VPC",
                    "Metadata": {
                        "DependsOn": [],
                        "Environment": "Production",
                        "StackName": "Production-VPC"
                    },
                    "Outputs": {
                        "InternetGateway": {
                            "Value": {
                                "Ref": "InternetGateway"
                            }
                        },
                        "VPCID": {
                            "Value": {
                                "Ref": "VPC"
                            }
                        }
                    },
                    "Resources": {
                        "InternetGateway": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Production"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Production-InternetGateway"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::InternetGateway"
                        },
                        "VPC": {
                            "Properties": {
                                "CidrBlock": "10.0.0.0/16",
                                "EnableDnsHostnames": "true",
                                "EnableDnsSupport": "true",
                                "InstanceTenancy": "default",
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Production"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Production-ServiceVPC"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::VPC"
                        },
                        "VpcGatewayAttachment": {
                            "Properties": {
                                "InternetGatewayId": {
                                    "Ref": "InternetGateway"
                                },
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::VPCGatewayAttachment"
                        },
                        "VpcNetworkAcl": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Production"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Production-NetworkAcl"
                                    }
                                ],
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::NetworkAcl"
                        },
                        "VpcNetworkAclInboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "false",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "PortRange": {
                                    "From": "443",
                                    "To": "443"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 100
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        },
                        "VpcNetworkAclOutboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "true",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 200
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        }
                    }
                }
            ), indent=4, sort_keys=True, separators=(',', ': '))
        )

    def test_add_resource_default_template_service_vpc(self):
        """
        Test result from template_service_vpc.construct_template() with additional resource
        add InternetGateway resource:
        ec2.InternetGateway(
            'AdditionalInternetGateway',
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': 'Additional'
                },
                {
                    'Key': 'Name',
                    'Value': 'Additional-InternetGateway'
                }
            ]
        )
        """
        template_service_vpc = TemplateServiceVPC()
        template_service_vpc.construct_template()
        template_service_vpc.add_resource(
            ec2.InternetGateway(
                'AdditionalInternetGateway',
                Tags=[
                    {
                        'Key': 'Environment',
                        'Value': 'Additional'
                    },
                    {
                        'Key': 'Name',
                        'Value': 'Additional-InternetGateway'
                    }
                ]
            )
        )
        self.assertEqual(
            str(template_service_vpc.cloud_formation),
            json.dumps(dict(
                {
                    "Description": "Service VPC",
                    "Metadata": {
                        "DependsOn": [],
                        "Environment": "Development",
                        "StackName": "Development-VPC"
                    },
                    "Outputs": {
                        "InternetGateway": {
                            "Value": {
                                "Ref": "InternetGateway"
                            }
                        },
                        "VPCID": {
                            "Value": {
                                "Ref": "VPC"
                            }
                        }
                    },
                    "Resources": {
                        "InternetGateway": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-InternetGateway"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::InternetGateway"
                        },
                        "AdditionalInternetGateway": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Additional"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Additional-InternetGateway"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::InternetGateway"
                        },
                        "VPC": {
                            "Properties": {
                                "CidrBlock": "10.0.0.0/16",
                                "EnableDnsHostnames": "true",
                                "EnableDnsSupport": "true",
                                "InstanceTenancy": "default",
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-ServiceVPC"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::VPC"
                        },
                        "VpcGatewayAttachment": {
                            "Properties": {
                                "InternetGatewayId": {
                                    "Ref": "InternetGateway"
                                },
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::VPCGatewayAttachment"
                        },
                        "VpcNetworkAcl": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-NetworkAcl"
                                    }
                                ],
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::NetworkAcl"
                        },
                        "VpcNetworkAclInboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "false",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "PortRange": {
                                    "From": "443",
                                    "To": "443"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 100
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        },
                        "VpcNetworkAclOutboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "true",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 200
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        }
                    }
                }
            ), indent=4, sort_keys=True, separators=(',', ': '))
        )

    def test_add_output_default_template_service_vpc(self):
        """
        Test result from template_service_vpc.construct_template() with additional output
        add InternetGateway output:
        Output(
            'Additional-VPCID',
            Value=Ref('VPC')
        )
        """
        template_service_vpc = TemplateServiceVPC()
        template_service_vpc.construct_template()
        template_service_vpc.add_output(
            Output(
                'VPCID2',
                Value=Ref('VPC')
            )
        )
        self.assertEqual(
            str(template_service_vpc.cloud_formation),
            json.dumps(dict(
                {
                    "Description": "Service VPC",
                    "Metadata": {
                        "DependsOn": [],
                        "Environment": "Development",
                        "StackName": "Development-VPC"
                    },
                    "Outputs": {
                        "InternetGateway": {
                            "Value": {
                                "Ref": "InternetGateway"
                            }
                        },
                        "VPCID": {
                            "Value": {
                                "Ref": "VPC"
                            }
                        },
                        "VPCID2": {
                            "Value": {
                                "Ref": "VPC"
                            }
                        }
                    },
                    "Resources": {
                        "InternetGateway": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-InternetGateway"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::InternetGateway"
                        },
                        "VPC": {
                            "Properties": {
                                "CidrBlock": "10.0.0.0/16",
                                "EnableDnsHostnames": "true",
                                "EnableDnsSupport": "true",
                                "InstanceTenancy": "default",
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-ServiceVPC"
                                    }
                                ]
                            },
                            "Type": "AWS::EC2::VPC"
                        },
                        "VpcGatewayAttachment": {
                            "Properties": {
                                "InternetGatewayId": {
                                    "Ref": "InternetGateway"
                                },
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::VPCGatewayAttachment"
                        },
                        "VpcNetworkAcl": {
                            "Properties": {
                                "Tags": [
                                    {
                                        "Key": "Environment",
                                        "Value": "Development"
                                    },
                                    {
                                        "Key": "Name",
                                        "Value": "Development-NetworkAcl"
                                    }
                                ],
                                "VpcId": {
                                    "Ref": "VPC"
                                }
                            },
                            "Type": "AWS::EC2::NetworkAcl"
                        },
                        "VpcNetworkAclInboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "false",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "PortRange": {
                                    "From": "443",
                                    "To": "443"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 100
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        },
                        "VpcNetworkAclOutboundRule": {
                            "Properties": {
                                "CidrBlock": "0.0.0.0/0",
                                "Egress": "true",
                                "NetworkAclId": {
                                    "Ref": "VpcNetworkAcl"
                                },
                                "Protocol": "6",
                                "RuleAction": "allow",
                                "RuleNumber": 200
                            },
                            "Type": "AWS::EC2::NetworkAclEntry"
                        }
                    }
                }
            ), indent=4, sort_keys=True, separators=(',', ': '))
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
