# aws-arn

[![PyPI version](https://badge.fury.io/py/aws-arn.svg)](https://badge.fury.io/py/aws-arn)
[![Python Version](https://img.shields.io/pypi/pyversions/aws-arn)](https://pypi.org/project/aws-arn/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Test](https://github.com/gabrielsoltz/aws-arn/actions/workflows/test.yml/badge.svg)](https://github.com/gabrielsoltz/aws-arn/actions/workflows/test.yml)

A library and CLI tool to work with AWS ARNs (Amazon Resource Names).

Contains definitions for almost all AWS services and resources, including their **ARN format**, **ID regexp**, **ASFF name**, **CloudFormation resource type**, and **Terraform resource type**.

The full reference table is available as:

- **Searchable page**: [gabrielsoltz.github.io/aws-arn](https://gabrielsoltz.github.io/aws-arn) — filter by service, Terraform type, CloudFormation type, or ASFF name
- **Markdown file**: [docs/arn-list.md](docs/arn-list.md)

> The docs are regenerated automatically by a GitHub Action whenever `aws_arn/data.py` changes.

---

## Installation

```bash
pip install aws-arn
```

---

## Use Cases

- **Parse** an ARN into all its components (service, resource, region, account, resource ID, Terraform type, CloudFormation type, ASFF name)
- **Generate** ARNs from:
  - Service + resource name (e.g. `acm` + `certificate`)
  - Terraform resource type (e.g. `aws_acm_certificate`)
  - CloudFormation resource type (e.g. `AWS::CertificateManager::Certificate`)
  - ASFF resource name (e.g. `AwsCertificateManagerCertificate`)
- **Validate** a resource ID against its expected regexp
- **Look up** the service and sub-service for any ARN, Terraform, CloudFormation, or ASFF identifier

---

## Python Library

### Generate ARN

```python
import aws_arn

# From service and resource name
aws_arn.generate_arn('i-1234568901', 'ec2', 'instance', 'us-east-1', '012345789012', 'aws')
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# From Terraform resource type
aws_arn.generate_arn_from_terraform('i-1234568901', 'aws_instance', 'us-east-1', '012345789012', 'aws')
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# From CloudFormation resource type
aws_arn.generate_arn_from_cloudformation('i-1234568901', 'AWS::EC2::Instance', 'us-east-1', '012345789012', 'aws')
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# From ASFF resource name
aws_arn.generate_arn_from_asff('i-1234568901', 'AwsEc2Instance', 'us-east-1', '012345789012', 'aws')
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
```

### Parse ARN

```python
import aws_arn

aws_arn.parse_arn('arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901')
# {
#   'service': 'ec2',
#   'sub_service': 'instance',
#   'region': 'us-east-1',
#   'account': '012345789012',
#   'resource_id': 'i-1234568901',
#   'asff_resource': 'AwsEc2Instance',
#   'terraform': 'aws_instance',
#   'cloudformation': 'AWS::EC2::Instance'
# }
```

### Validate Resource ID

```python
import aws_arn

aws_arn.check_resource_id_regexp('i-1234567890abcdef0', 'ec2', 'instance')  # True
aws_arn.check_resource_id_regexp('not-valid', 'ec2', 'instance')            # False
```

### Look Up Service

```python
import aws_arn

aws_arn.get_service_from_terraform('aws_acm_certificate')
# ('acm', 'certificate')

aws_arn.get_service_from_cloudformation('AWS::CertificateManager::Certificate')
# ('acm', 'certificate')

aws_arn.get_service_from_asff('AwsCertificateManagerCertificate')
# ('acm', 'certificate')
```

---

## CLI Tool

### Generate ARN

```bash
# From service and resource name
aws-arn --generate-arn \
  --service ec2 --sub-service instance \
  --id i-1234568901 --region us-east-1 --account 012345789012 --partition aws
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# From Terraform resource type
aws-arn --generate-arn-from-terraform \
  --terraform aws_instance \
  --id i-1234568901 --region us-east-1 --account 012345789012 --partition aws
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# From CloudFormation resource type
aws-arn --generate-arn-from-cloudformation \
  --cloudformation AWS::EC2::Instance \
  --id i-1234568901 --region us-east-1 --account 012345789012 --partition aws
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# From ASFF resource name
aws-arn --generate-arn-from-asff \
  --asff-resource AwsEc2Instance \
  --id i-1234568901 --region us-east-1 --account 012345789012 --partition aws
# arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
```

### Parse ARN

```bash
aws-arn --parse-arn arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
# {'service': 'ec2', 'sub_service': 'instance', 'region': 'us-east-1',
#  'account': '012345789012', 'resource_id': 'i-1234568901',
#  'asff_resource': 'AwsEc2Instance', 'terraform': 'aws_instance',
#  'cloudformation': 'AWS::EC2::Instance'}
```

### Look Up Service

```bash
# From an ARN
aws-arn --get-service arn:aws:acm:us-east-1:012345789012:certificate/abc-123
# ('acm', 'certificate')

# From a Terraform resource type
aws-arn --get-service aws_acm_certificate
# ('acm', 'certificate')

# From a CloudFormation resource type
aws-arn --get-service AWS::CertificateManager::Certificate
# ('acm', 'certificate')
```

### Validate Resource ID

```bash
aws-arn --validate-id --service ec2 --sub-service instance --id i-1234567890abcdef0
# True
```

### List Services and Resources

```bash
aws-arn --list-services
aws-arn --list-sub-services
```

---

## Contributing

> **Work in progress** — not all services and resources are included yet. Please open an issue or pull request if you find any errors or omissions.

The data is defined in [aws_arn/data.py](aws_arn/data.py) as a Python dictionary. Each entry follows this structure:

```python
"acm": {                          # Service name (follows boto3 naming)
    "certificate": {              # Resource name (follows boto3 naming)
        "arn_format":     "arn:{partition}:acm:{region}:{account}:certificate/{resource_id}",
        "id_name":        "CertificateId",
        "id_regexp":      "([a-z0-9-]+)",
        "asff_name":      "AwsCertificateManagerCertificate",
        "cloudformation": "AWS::CertificateManager::Certificate",
        "terraform":      "aws_acm_certificate",
    }
},
```
