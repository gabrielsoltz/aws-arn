import argparse


def get_parser():
    """Configure Parser"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
    AWS-ARN is a tool to help you to create ARNs (Amazon Resource Names) for AWS resources.
    """,
    )

    group_functions = parser.add_argument_group("Functions")
    group_functions.add_argument(
        "--generate-arn",
        action=argparse.BooleanOptionalAction,
        help="Generate ARN for a resource",
        required=False,
    )
    group_functions.add_argument(
        "--generate-arn-from-terraform",
        action=argparse.BooleanOptionalAction,
        help="Generate ARN for a resource from Terraform resource",
        required=False,
    )
    group_functions.add_argument(
        "--generate-arn-from-cloudformation",
        action=argparse.BooleanOptionalAction,
        help="Generate ARN for a resource from Cloudformation resource",
        required=False,
    )
    group_functions.add_argument(
        "--validate-id",
        action=argparse.BooleanOptionalAction,
        help="Validate resource_id for a resource",
        required=False,
    )
    group_functions.add_argument(
        "--get-resource-id-from-arn",
        action=argparse.BooleanOptionalAction,
        help="Get resource_id from ARN",
        required=False,
    )
    group_functions.add_argument(
        "--get-service-from-asff-resource",
        action=argparse.BooleanOptionalAction,
        help="Get service and sub service from ASFF resource",
        required=False,
    )
    group_functions.add_argument(
        "--get-service-from-terraform",
        action=argparse.BooleanOptionalAction,
        help="Get service and sub service from Terraform resource",
        required=False,
    )
    group_functions.add_argument(
        "--get-service-from-cloudformation",
        action=argparse.BooleanOptionalAction,
        help="Get service and sub service from Cloudformation resource",
        required=False,
    )
    group_functions.add_argument(
        "--list-services",
        action=argparse.BooleanOptionalAction,
        help="List all services",
        required=False,
    )
    group_functions.add_argument(
        "--list-sub-services",
        action=argparse.BooleanOptionalAction,
        help="List all sub services",
        required=False,
    )
    group_functions.add_argument(
        "--generate-markdown",
        action=argparse.BooleanOptionalAction,
        help="Generate Markdown table for README.md",
        required=False,
    )

    group_data = parser.add_argument_group("Data")
    group_data.add_argument(
        "--service",
        default=None,
        help="Service name",
        required=False,
    )
    group_data.add_argument(
        "--sub-service",
        default=None,
        help="Sub Service name",
        required=False,
    )
    group_data.add_argument(
        "--arn",
        default=None,
        help="ARN",
        required=False,
    )
    group_data.add_argument(
        "--id",
        default=None,
        help="ID",
        required=False,
    )
    group_data.add_argument(
        "--asff-resource",
        default=None,
        help="ID",
        required=False,
    )
    group_data.add_argument(
        "--region",
        default=None,
        help="Region",
        required=False,
    )
    group_data.add_argument(
        "--account",
        default=None,
        help="Account",
        required=False,
    )
    group_data.add_argument(
        "--partition",
        default=None,
        help="Partition",
        required=False,
    )
    group_data.add_argument(
        "--terraform",
        default=None,
        help="Partition",
        required=False,
    )
    group_data.add_argument(
        "--cloudformation",
        default=None,
        help="Partition",
        required=False,
    )

    # Group: Debug Options
    group_debug = parser.add_argument_group("Debug Options")
    group_debug.add_argument(
        "--log-level",
        choices=["ERROR", "WARNING", "INFO", "DEBUG"],
        default="ERROR",
        help="Specify Log Level, by default ERROR",
        required=False,
    )

    return parser
