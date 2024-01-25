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
    resource_type,
    sub_resource_type,
    region,
    account,
    partition,
):
    try:
        arn = aws_arn_data[resource_type][sub_resource_type]["arn_format"].format(
            partition=partition, region=region, account=account, resource_id=resource_id
        )
    except KeyError as e:
        print("Invalid resource type or sub resource type", e)
        return False
    return arn


def check_resource_id_regexp(resource_id, resource_type, sub_resource_type):
    import re

    pattern = re.compile(aws_arn_data[resource_type][sub_resource_type]["id_regexp"])
    # print (aws_arn_data[resource_type][sub_resource_type]["id_regexp"])

    return bool(re.search(pattern, resource_id))


def get_resource_id_from_arn(arn):
    import re

    service = get_service_from_arn(arn)
    sub_service = get_sub_service_from_arn(arn)
    regexp = aws_arn_data[service][sub_service]["id_regexp"]
    if regexp.startswith("^"):
        regexp = regexp[1:]
    pattern = re.compile(regexp)
    search = re.search(pattern, arn)
    if bool(search) == False:
        print("No match found")
        return False
    print("search", search.group())
    return search.group()


def get_service_from_arn(arn):
    return arn.split(":")[2]


def get_sub_service_from_arn(arn):
    return arn.split(":")[5].split("/")[0].replace("-", "_")


def get_account_from_arn(arn):
    return arn.split(":")[4]


def get_region_from_arn(arn):
    return arn.split(":")[3]


def get_service_from_asff_resource(asff_resource):
    for service in aws_arn_data:
        for sub_service in aws_arn_data[service]:
            if aws_arn_data[service][sub_service]["asff_name"] == asff_resource:
                return service, sub_service
    return False


def get_service_from_terraform(terraform):
    for service in aws_arn_data:
        for sub_service in aws_arn_data[service]:
            if aws_arn_data[service][sub_service]["terraform"] == terraform:
                return service, sub_service
    return False


def get_service_from_cloudformation(cloudformation):
    for service in aws_arn_data:
        for sub_service in aws_arn_data[service]:
            if aws_arn_data[service][sub_service]["cloudformation"] == cloudformation:
                return service, sub_service
    return False


def generate_arn_from_asff(
    resource_id,
    asff_resource,
    region,
    account,
    partition,
):
    service, sub_service = get_service_from_asff_resource(asff_resource)
    try:
        arn = aws_arn_data[service][sub_service]["arn_format"].format(
            partition=partition, region=region, account=account, resource_id=resource_id
        )
    except KeyError as e:
        print("Invalid resource type or sub resource type", e)
        return False
    return arn


def generate_arn_from_terraform(
    resource_id,
    terraform,
    region,
    account,
    partition,
):
    service, sub_service = get_service_from_terraform(terraform)
    try:
        arn = aws_arn_data[service][sub_service]["arn_format"].format(
            partition=partition, region=region, account=account, resource_id=resource_id
        )
    except KeyError as e:
        print("Invalid resource type or sub resource type", e)
        return False
    return arn


def generate_arn_from_cloudformation(
    resource_id,
    cloudformation,
    region,
    account,
    partition,
):
    service, sub_service = get_service_from_cloudformation(cloudformation)
    try:
        arn = aws_arn_data[service][sub_service]["arn_format"].format(
            partition=partition, region=region, account=account, resource_id=resource_id
        )
    except KeyError as e:
        print("Invalid resource type or sub resource type", e)
        return False
    return arn
