import argparse

from . import __version__


def get_parser():
    """Configure Parser"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
AWS-ARN — work with AWS ARNs from the command line.

Examples:
  # Generate an ARN directly
  aws-arn --generate-arn --service acm --sub-service certificate \\
          --id abc-123 --region us-east-1 --account 123456789012 --partition aws

  # Generate from a Terraform resource type
  aws-arn --generate-arn-from-terraform --terraform aws_acm_certificate \\
          --id abc-123 --region us-east-1 --account 123456789012 --partition aws

  # Generate from a CloudFormation resource type
  aws-arn --generate-arn-from-cloudformation \\
          --cloudformation AWS::CertificateManager::Certificate \\
          --id abc-123 --region us-east-1 --account 123456789012 --partition aws

  # Generate from an ASFF resource name
  aws-arn --generate-arn-from-asff \\
          --asff-resource AwsCertificateManagerCertificate \\
          --id abc-123 --region us-east-1 --account 123456789012 --partition aws

  # Parse an ARN into its components
  aws-arn --parse-arn arn:aws:acm:us-east-1:123456789012:certificate/abc-123

  # Look up service and sub-service from any identifier
  aws-arn --get-service arn:aws:acm:us-east-1:123456789012:certificate/abc-123
  aws-arn --get-service aws_acm_certificate
  aws-arn --get-service AWS::CertificateManager::Certificate

  # Validate a resource ID against the expected regexp
  aws-arn --validate-id --service acm --sub-service certificate --id abc-123

  # List all supported services or sub-services
  aws-arn --list-services
  aws-arn --list-sub-services
""",
    )

    group_functions = parser.add_argument_group("Functions")
    group_functions.add_argument(
        "--generate-arn",
        action=argparse.BooleanOptionalAction,
        help=(
            "Generate an ARN from its components. "
            "Requires: --service, --sub-service, --id, --region, --account, --partition."
        ),
        required=False,
    )
    group_functions.add_argument(
        "--generate-arn-from-terraform",
        action=argparse.BooleanOptionalAction,
        help=(
            "Generate an ARN from a Terraform resource type. "
            "Requires: --terraform, --id, --region, --account, --partition."
        ),
        required=False,
    )
    group_functions.add_argument(
        "--generate-arn-from-cloudformation",
        action=argparse.BooleanOptionalAction,
        help=(
            "Generate an ARN from a CloudFormation resource type. "
            "Requires: --cloudformation, --id, --region, --account, --partition."
        ),
        required=False,
    )
    group_functions.add_argument(
        "--generate-arn-from-asff",
        action=argparse.BooleanOptionalAction,
        help=(
            "Generate an ARN from an ASFF resource name. "
            "Requires: --asff-resource, --id, --region, --account, --partition."
        ),
        required=False,
    )
    group_functions.add_argument(
        "--validate-id",
        action=argparse.BooleanOptionalAction,
        help=(
            "Validate a resource ID against the expected regexp for a given resource type. "
            "Requires: --service, --sub-service, --id."
        ),
        required=False,
    )
    group_functions.add_argument(
        "--get-service",
        default=None,
        metavar="IDENTIFIER",
        help=(
            "Return the service and sub-service for any supported identifier: "
            "an ARN, a Terraform resource type (aws_*), "
            "a CloudFormation resource type (AWS::*), "
            "or an ASFF resource name (Aws*)."
        ),
        required=False,
    )
    group_functions.add_argument(
        "--parse-arn",
        default=None,
        metavar="ARN",
        help=(
            "Parse an ARN and print all its components: "
            "service, sub-service, region, account, resource ID, "
            "ASFF name, Terraform resource type, and CloudFormation resource type."
        ),
        required=False,
    )
    group_functions.add_argument(
        "--list-services",
        action=argparse.BooleanOptionalAction,
        help="List all supported AWS services.",
        required=False,
    )
    group_functions.add_argument(
        "--list-sub-services",
        action=argparse.BooleanOptionalAction,
        help="List all supported resource types across every service.",
        required=False,
    )
    group_functions.add_argument(
        "--generate-markdown",
        action=argparse.BooleanOptionalAction,
        help="Print a Markdown table of all supported resources (useful for updating README.md).",
        required=False,
    )

    group_data = parser.add_argument_group("Data")
    group_data.add_argument(
        "--partition",
        default=None,
        metavar="PARTITION",
        help="AWS partition (e.g. aws, aws-cn, aws-us-gov).",
        required=False,
    )
    group_data.add_argument(
        "--service",
        default=None,
        metavar="SERVICE",
        help="AWS service name as used in ARNs (e.g. acm, ec2, s3).",
        required=False,
    )
    group_data.add_argument(
        "--region",
        default=None,
        metavar="REGION",
        help="AWS region (e.g. us-east-1). Leave empty for global resources such as IAM.",
        required=False,
    )
    group_data.add_argument(
        "--account",
        default=None,
        metavar="ACCOUNT_ID",
        help="12-digit AWS account ID. Leave empty for resources that omit it (e.g. S3).",
        required=False,
    )
    group_data.add_argument(
        "--sub-service",
        default=None,
        metavar="SUB_SERVICE",
        help="Resource type within a service (e.g. certificate, instance, bucket).",
        required=False,
    )
    group_data.add_argument(
        "--id",
        default=None,
        metavar="RESOURCE_ID",
        help="The resource identifier (e.g. i-1234567890abcdef0, abc-123).",
        required=False,
    )
    group_data.add_argument(
        "--asff-resource",
        default=None,
        metavar="ASFF_NAME",
        help="ASFF resource name (e.g. AwsCertificateManagerCertificate). Use --list-sub-services to browse available names.",
        required=False,
    )
    group_data.add_argument(
        "--terraform",
        default=None,
        metavar="TF_RESOURCE",
        help="Terraform resource type (e.g. aws_acm_certificate). Use --list-sub-services to browse available types.",
        required=False,
    )
    group_data.add_argument(
        "--cloudformation",
        default=None,
        metavar="CF_RESOURCE",
        help="CloudFormation resource type (e.g. AWS::CertificateManager::Certificate). Use --list-sub-services to browse available types.",
        required=False,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"aws-arn {__version__}",
    )

    # Group: Debug Options
    group_debug = parser.add_argument_group("Debug Options")
    group_debug.add_argument(
        "--log-level",
        choices=["ERROR", "WARNING", "INFO", "DEBUG"],
        default="ERROR",
        help="Log verbosity level (default: ERROR).",
        required=False,
    )

    return parser
