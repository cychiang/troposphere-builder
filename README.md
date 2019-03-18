# troposphere_builder
The `troposphere_builder` is a template builder on top of the troposphere. It can help developer to create and manage there own CloudFormation templates much easier.

# Installation
Install package locally.
```bash
git clone git@github.com:cychiang/troposphere-builder.git
cd troposphere-builder
pip install -e .
```

# How to use
```python
from troposphere_builder.templates.template_service_vpc import TemplateServiceVPC

template_service_vpc = TemplateServiceVPC()
template_service_vpc.construct_template()
print(template_service_vpc.cloud_formation.__str__())

```
The example output of the code above:
```json
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
```
