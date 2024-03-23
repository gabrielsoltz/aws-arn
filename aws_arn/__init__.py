try:
    from data import aws_arn_data
except ModuleNotFoundError:
    from aws_arn.data import aws_arn_data


def list_services():
    for i in aws_arn_data:
        print(i)
    print("Total number of services: ", len(aws_arn_data))


def list_sub_services():
    count_resources = 0
    for i in aws_arn_data.values():
        for j in i:
            print(j)
            count_resources += 1
    print("Total number of resources: ", count_resources)


def list_sub_services_for_service(service):
    for i in aws_arn_data[service]:
        print(i)


def list_asff_resources():
    for services in aws_arn_data:
        for sub_services in aws_arn_data[services]:
            if aws_arn_data[services][sub_services]["asff_name"] != "":
                print(aws_arn_data[services][sub_services]["asff_name"])


def generate_markdown_table():
    headers = [
        "Service",
        "Resource",
        "ARN Format",
        "ID Name",
        "ID Regexp",
        "ASFF Name",
        "CloudFormation",
        "Terraform",
    ]
    table = [headers]

    for service, resources in aws_arn_data.items():
        for resource, attributes in resources.items():
            arn_format = "`" + attributes.get("arn_format", "") + "`"
            id_regexp = "`" + str(attributes.get("id_regexp", "")) + "`"
            row = [
                service,
                resource,
                arn_format,
                attributes.get("id_name", ""),
                id_regexp,
                attributes.get("asff_name", ""),
                attributes.get("cloudformation", ""),
                attributes.get("terraform", ""),
            ]
            table.append(row)

    table_str = "| " + " | ".join(headers) + " |\n"
    table_str += "|-" + "-|-".join(["--" for _ in headers]) + "-|\n"

    for row in table[1:]:
        table_str += "| " + " | ".join([str(item) for item in row]) + " |\n"

    return table_str


def generate_arn(
    resource_id,
    service,
    sub_service,
    region,
    account,
    partition,
):
    try:
        arn = aws_arn_data[service][sub_service]["arn_format"].format(
            partition=partition, region=region, account=account, resource_id=resource_id
        )
    except KeyError as e:
        raise KeyError(
            "Invalid resource {} or sub resource type {}".format(service, sub_service)
        )
    return arn


def generate_arn_from_terraform(
    resource_id,
    terraform,
    region,
    account,
    partition,
):
    if not validate_terraform(terraform):
        raise ValueError("Invalid Terraform resource: {}".format(terraform))
    service, sub_service = get_service_from_terraform(terraform)
    arn = generate_arn(resource_id, service, sub_service, region, account, partition)
    return arn


def generate_arn_from_cloudformation(
    resource_id,
    cloudformation,
    region,
    account,
    partition,
):
    if not validate_cloudformation(cloudformation):
        raise ValueError("Invalid CloudFormation resource: {}".format(cloudformation))
    service, sub_service = get_service_from_cloudformation(cloudformation)
    arn = generate_arn(resource_id, service, sub_service, region, account, partition)
    return arn


def generate_arn_from_asff(
    resource_id,
    asff_resource,
    region,
    account,
    partition,
):
    if not validate_asff(asff_resource):
        raise ValueError("Invalid ASFF resource: {}".format(asff_resource))
    service, sub_service = get_service_from_asff(asff_resource)
    arn = generate_arn(resource_id, service, sub_service, region, account, partition)
    return arn


# Parse ARN


def parse_arn(arn):
    if validate_arn(arn):
        service = get_service_from_arn(arn)
        sub_service = get_sub_service_from_arn(arn)
        region = get_region_from_arn(arn)
        account = get_account_from_arn(arn)
        resource_id = get_resource_id_from_arn(arn)
        asff_resource = get_asff_from_arn(arn)
        terraform = get_terraform_from_arn(arn)
        cloudformation = get_cloudformation_from_arn(arn)
        return {
            "service": service,
            "sub_service": sub_service,
            "region": region,
            "account": account,
            "resource_id": resource_id,
            "asff_resource": asff_resource,
            "terraform": terraform,
            "cloudformation": cloudformation,
        }
    raise ValueError("Invalid ARN: {}".format(arn))


def get_service_from_arn(arn):
    service_from_arn = arn.split(":")[2]
    try:
        service = aws_arn_data[service_from_arn]
        return service_from_arn
    except KeyError:
        # Let's try finding the service across all ARNs
        for service in aws_arn_data:
            for sub_service in aws_arn_data[service]:
                if (
                    aws_arn_data[service][sub_service]["arn_format"].split(":")[2]
                    == arn.split(":")[2]
                ):
                    return service
        raise KeyError("Unknown service in ARN: {}".format(arn))


def get_region_from_arn(arn):
    return arn.split(":")[3]


def get_account_from_arn(arn):
    return arn.split(":")[4]


def get_sub_service_from_arn(arn):
    arn_part_5 = arn.split(":")[5]
    service = get_service_from_arn(arn)
    if service == "s3":
        if not "/" in arn_part_5:
            return "bucket"
        else:
            return "object"
    elif service == "sqs":
        return "queue"
    elif service == "sns":
        if len(arn.split(":")) == 6:
            return "topic"
        else:
            return "subscription"
    elif arn_part_5.startswith("/"):
        sub_service_from_arn = arn.split(":")[5].split("/")[1].replace("-", "_")
    else:
        sub_service_from_arn = arn.split(":")[5].split("/")[0].replace("-", "_")
    # Let's see if we can find the sub_service in the service
    try:
        sub_service = aws_arn_data[service][sub_service_from_arn]
        return sub_service_from_arn
    except KeyError:
        # Let's try finding the sub_service across all ARNs
        for sub_service in aws_arn_data[service]:
            sub_service_arn_part_5 = aws_arn_data[service][sub_service][
                "arn_format"
            ].split(":")[5]
            if sub_service_arn_part_5.startswith("/"):
                sub_service_arn_part_5 = sub_service_arn_part_5.split("/")[1].replace(
                    "-", "_"
                )
            else:
                sub_service_arn_part_5 = sub_service_arn_part_5.split("/")[0].replace(
                    "-", "_"
                )
            if sub_service_arn_part_5 == sub_service_from_arn:
                return sub_service
        raise KeyError("Unknown sub service in ARN: {}".format(arn))


def get_resource_id_from_arn(arn):
    service = get_service_from_arn(arn)
    sub_service = get_sub_service_from_arn(arn)
    try:
        arn_format = aws_arn_data[service][sub_service]["arn_format"]
    except KeyError:
        raise KeyError(
            "Invalid resource {} or sub resource type {}".format(service, sub_service)
        )

    arn_parts = arn.split(":")
    format_parts = arn_format.split(":")

    if len(arn_parts) != len(format_parts):
        return None  # ARN format doesn't match

    resource_id_index = None
    for i, part in enumerate(format_parts):
        if "{resource_id}" in part:
            resource_id_index = i
            break

    if resource_id_index is None:
        return None  # Resource ID placeholder not found in format

    resource_id = arn_parts[resource_id_index].split("/")[-1]
    return resource_id


def get_asff_from_arn(arn):
    service = get_service_from_arn(arn)
    sub_service = get_sub_service_from_arn(arn)
    try:
        asff_name = aws_arn_data[service][sub_service]["asff_name"]
    except KeyError:
        raise KeyError(
            "Invalid resource {} or sub resource type {}".format(service, sub_service)
        )
    return asff_name


def get_terraform_from_arn(arn):
    service = get_service_from_arn(arn)
    sub_service = get_sub_service_from_arn(arn)
    try:
        terraform = aws_arn_data[service][sub_service]["terraform"]
    except KeyError:
        raise KeyError(
            "Invalid resource {} or sub resource type {}".format(service, sub_service)
        )
    return terraform


def get_cloudformation_from_arn(arn):
    service = get_service_from_arn(arn)
    sub_service = get_sub_service_from_arn(arn)
    try:
        cloudformation = aws_arn_data[service][sub_service]["cloudformation"]
    except KeyError:
        raise KeyError(
            "Invalid resource {} or sub resource type {}".format(service, sub_service)
        )
    return cloudformation


# Get Service


def get_service(item):
    if validate_arn(item):
        return get_service_from_arn(item)
    if validate_terraform(item):
        return get_service_from_terraform(item)
    if validate_cloudformation(item):
        return get_service_from_cloudformation(item)
    if validate_asff(item):
        return get_service_from_asff(item)
    raise ValueError("Invalid input to get service: {}".format(item))


def get_service_from_asff(asff_resource):
    if validate_asff(asff_resource):
        for service in aws_arn_data:
            for sub_service in aws_arn_data[service]:
                if aws_arn_data[service][sub_service]["asff_name"] == asff_resource:
                    return service, sub_service
    return False, False


def get_service_from_terraform(terraform):
    if validate_terraform(terraform):
        for service in aws_arn_data:
            for sub_service in aws_arn_data[service]:
                if aws_arn_data[service][sub_service]["terraform"] == terraform:
                    return service, sub_service
    return False, False


def get_service_from_cloudformation(cloudformation):
    if validate_cloudformation(cloudformation):
        for service in aws_arn_data:
            for sub_service in aws_arn_data[service]:
                if (
                    aws_arn_data[service][sub_service]["cloudformation"]
                    == cloudformation
                ):
                    return service, sub_service
    return False, False


def validate_arn(arn):
    if not arn.startswith("arn:"):
        return False
    arn_parts = arn.split(":")
    if len(arn_parts) < 6:
        return False
    return True


def validate_terraform(terraform):
    if not terraform.startswith("aws_"):
        return False
    return True


def validate_cloudformation(cloudformation):
    if not cloudformation.startswith("AWS::"):
        return False
    return True


def validate_asff(asff_name):
    if not asff_name.startswith("Aws"):
        return False
    return True


def check_resource_id_regexp(resource_id, resource_type, sub_resource_type):
    import re

    pattern = re.compile(aws_arn_data[resource_type][sub_resource_type]["id_regexp"])
    # print (aws_arn_data[resource_type][sub_resource_type]["id_regexp"])

    return bool(re.search(pattern, resource_id))
