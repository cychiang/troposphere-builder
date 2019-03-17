from .cloud_formation import CloudFormation


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
