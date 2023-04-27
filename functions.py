from arn import aws_arn

def get_services():
    for i in aws_arn:
        print(i)
    print ("Total number of services: ", len(aws_arn))

def get_resources():
    count_resources = 0
    for i in aws_arn.values():
        for j in i:
            print(j)
            count_resources += 1
    print ("Total number of resources: ", count_resources)

def generate_arn_table(arn_dict):
    header = "| Service | ARN Format |\n| --- | --- |\n"
    rows = []
    for service, arn_format in arn_dict.items():
        arn_breaks = ""
        for sub_service, arn in arn_format.items():
            arn_breaks += sub_service + ": `" + arn + "`<br>"
        rows.append(f"| {service} | {arn_breaks} |")
    return header + "\n".join(rows)

print (generate_arn_table(aws_arn))
