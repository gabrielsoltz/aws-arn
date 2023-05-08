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
                print (aws_arn_data[services][sub_services]["asff_name"])

def generate_markdown_table():
    header = "| Service | ARN Format |\n| --- | --- |\n"
    rows = []
    for service in aws_arn_data:
        arn_breaks = ""
        for sub_service in aws_arn_data[service]:
            arn_breaks += sub_service + ": `" + aws_arn_data[service][sub_service]["arn_format"] + "`<br>"
        rows.append(f"| {service} | {arn_breaks} |")
    return header + "\n".join(rows)

def generate_arn(
    resource_id,
    resource_type,
    sub_resource_type,
    region,
    account,
    partition,
):
    sub_resource_type = sub_resource_type.replace("_", "-")
    try:
        arn = aws_arn_data[resource_type][sub_resource_type]["arn_format"].format(
            partition=partition, region=region, account=account, resource_id=resource_id
        )
    except KeyError as e:
        print("Invalid resource type or sub resource type", e)
        return False
    return arn

def check_resource_id_regexp(
    resource_id,
    resource_type,
    sub_resource_type
):
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
        print ("No match found")
        return False
    print ("search", search.group())
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