#!/usr/bin/env python3

import logging
import sys

from aws_arn import (
    check_resource_id_regexp,
    generate_arn,
    generate_arn_from_asff,
    generate_arn_from_cloudformation,
    generate_arn_from_terraform,
    get_service,
    list_services,
    list_sub_services,
    parse_arn,
)
from aws_arn.get_parser import get_parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.log_level))

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

    # Generate ARNs
    if args.generate_arn:
        try:
            print(generate_arn(id, service, sub_service, region, account, partition))
        except (KeyError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    if args.generate_arn_from_terraform:
        try:
            print(generate_arn_from_terraform(id, terraform, region, account, partition))
        except (KeyError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    if args.generate_arn_from_cloudformation:
        try:
            print(generate_arn_from_cloudformation(id, cloudformation, region, account, partition))
        except (KeyError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    if args.generate_arn_from_asff:
        try:
            print(generate_arn_from_asff(id, asff_resource, region, account, partition))
        except (KeyError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    # Parse ARN
    if args.parse_arn:
        try:
            print(parse_arn(args.parse_arn))
        except (KeyError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    # Get service
    if args.get_service:
        try:
            print(get_service(args.get_service))
        except (KeyError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    if args.validate_id:
        try:
            print(check_resource_id_regexp(id, service, sub_service))
        except (KeyError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
