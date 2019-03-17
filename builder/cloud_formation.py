from troposphere import Template


class CloudFormation(object):
    """
    Formation:
        - Generate JSON format of AWS CloudFormation
    """
    def __init__(self):
        self.description = None
        self.metadata = None
        self.resources = []
        self.outputs = []
        self.template = Template()

    def __str__(self):
        self.template.set_description(self.description)
        self.template.set_metadata(self.metadata)
        self.template.add_resource(self.resources)
        self.template.add_output(self.outputs)
        return self.template.to_json()
