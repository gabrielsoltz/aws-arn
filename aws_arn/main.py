#!/usr/bin/env python3

import sys


try:
    from get_parser import get_parser
    from __init__ import *
except ModuleNotFoundError:
    from aws_arn.get_parser import get_parser
    from aws_arn.__init__ import *

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

    # List services
    if args.list_services:
        list_services(service)
        sys.exit(0)

    if args.list_sub_services:
        list_sub_services(sub_service)
        sys.exit(0)

    if args.generate_arn:
        print(generate_arn(id, service, sub_service, region, account, partition))
    
    if args.validate_id:
        print(check_resource_id_regexp(id, service, sub_service))

    if args.get_service_from_asff_resource:
        print(get_sub_service_from_arn(asff_resource))

if __name__ == "__main__":
    main()

