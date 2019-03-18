from troposphere_builder.templates.template_service_vpc import TemplateServiceVPC


def create_from_template():
    metadata = {
        'development': {
            'DependsOn': [],
            'Environment': 'Development',
            'StackName': 'Development-VPC'
        },
        'experimental': {
            'DependsOn': [],
            'Environment': 'Experimental',
            'StackName': 'Experimental-VPC'
        },
        'production': {
            'DependsOn': [],
            'Environment': 'Production',
            'StackName': 'Production-VPC'
        },
    }

    for key in metadata.keys():
        with open(f'output/template_{key}.json', mode='w', encoding='UTF-8') as fp:
            template_service_vpc = TemplateServiceVPC()
            template_service_vpc.construct_template(Metadata=metadata[key])
            fp.write(str(template_service_vpc.cloud_formation)+'\n')


create_from_template()
