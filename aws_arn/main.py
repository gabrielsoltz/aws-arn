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

    id = args.id or ""
    service = args.service or ""
    sub_service = args.sub_service or ""
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

    # Generate ARNs
    if args.generate_arn:
        print(generate_arn(id, service, sub_service, region, account, partition))

    if args.generate_arn_from_terraform:
        print(generate_arn_from_terraform(id, terraform, region, account, partition))

    if args.generate_arn_from_cloudformation:
        print(
            generate_arn_from_cloudformation(
                id, cloudformation, region, account, partition
            )
        )
    if args.generate_arn_from_asff:
        print(generate_arn_from_asff(id, asff_resource, region, account, partition))

    # Parse ARN
    if args.parse_arn:
        try:
            print(parse_arn(args.parse_arn))
        except ValueError as e:
            print(e)

    # Get service
    if args.get_service:
        try:
            print(get_service(args.get_service))
        except ValueError as e:
            print(e)

    if args.validate_id:
        print(check_resource_id_regexp(id, service, sub_service))


if __name__ == "__main__":
    main()
