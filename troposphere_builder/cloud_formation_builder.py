from troposphere import Template


class CloudFormation(object):
    """
    CloudFormation:
      -
      - Generate AWS CloudFormation result in JSON format
    """
    def __init__(self):
        self.description = None
        self.metadata = None
        self.resources = []
        self.outputs = []

    def __str__(self):
        template = Template()
        template.set_description(self.description)
        template.set_metadata(self.metadata)
        template.add_resource(self.resources)
        template.add_output(self.outputs)
        return template.to_json()


class CloudFormationBuilder(object):
    """
    CloudFormationBuilder:
      - Configure the CloudFormation and add additional resource/output to CloudFormation
    """
    def __init__(self):
        self.cloud_formation = CloudFormation()

    def configure_description(self, description):
        self.cloud_formation.description = description

    def configure_metadata(self, metadata):
        self.cloud_formation.metadata = metadata

    def configure_outputs(self, outputs):
        self.cloud_formation.outputs = outputs

    def configure_resources(self, resources):
        self.cloud_formation.resources = resources

    def add_output(self, output):
        self.cloud_formation.outputs.append(output)

    def add_resource(self, resource):
        self.cloud_formation.resources.append(resource)
