#!/usr/bin/env python3

import sys

try:
    from __init__ import *
    from get_parser import get_parser
except ModuleNotFoundError:
    from aws_arn.__init__ import *
    from aws_arn.get_parser import get_parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    print("Args:", args)

    id = args.id or ""
    service = args.service or ""
    sub_service = args.sub_service or ""
    arn = args.arn or ""
    asff_resource = args.asff_resource or ""
    region = args.region or ""
    account = args.account or ""
    partition = args.partition or ""
    terraform = args.terraform or ""
    cloudformation = args.cloudformation or ""

    # List services
    if args.list_services:
        list_services()
        sys.exit(0)

    if args.list_sub_services:
        list_sub_services()
        sys.exit(0)

    if args.generate_markdown:
        print(generate_markdown_table())
        sys.exit(0)

    if args.generate_arn:
        print(generate_arn(id, service, sub_service, region, account, partition))

    if args.validate_id:
        print(check_resource_id_regexp(id, service, sub_service))

    if args.get_service_from_asff_resource:
        print(get_sub_service_from_arn(asff_resource))

    if args.get_service_from_terraform:
        print(get_service_from_terraform(terraform))

    if args.generate_arn_from_terraform:
        print(generate_arn_from_terraform(id, terraform, region, account, partition))

    if args.get_service_from_cloudformation:
        print(get_service_from_cloudformation(cloudformation))

    if args.generate_arn_from_cloudformation:
        print(
            generate_arn_from_cloudformation(
                id, cloudformation, region, account, partition
            )
        )


if __name__ == "__main__":
    main()
