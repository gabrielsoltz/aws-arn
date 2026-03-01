"""Core function tests for aws_arn."""

import pytest

import aws_arn

# ---------------------------------------------------------------------------
# validate_arn
# ---------------------------------------------------------------------------


class TestValidateArn:
    def test_valid_arn(self):
        assert aws_arn.validate_arn("arn:aws:iam::123456789012:role/MyRole") is True

    def test_valid_arn_with_region(self):
        assert (
            aws_arn.validate_arn("arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0")
            is True
        )

    def test_invalid_not_starting_with_arn(self):
        assert aws_arn.validate_arn("aws:iam::123456789012:role/MyRole") is False

    def test_invalid_too_few_parts(self):
        assert aws_arn.validate_arn("arn:aws:iam") is False

    def test_invalid_empty_string(self):
        assert aws_arn.validate_arn("") is False

    def test_s3_bucket_arn(self):
        assert aws_arn.validate_arn("arn:aws:s3:::my-bucket") is True


# ---------------------------------------------------------------------------
# parse_arn
# ---------------------------------------------------------------------------


class TestParseArn:
    def test_ec2_instance(self):
        arn = "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
        result = aws_arn.parse_arn(arn)
        assert result["service"] == "ec2"
        assert result["region"] == "us-east-1"
        assert result["account"] == "123456789012"
        assert result["sub_service"] == "instance"
        assert result["resource_id"] == "i-1234567890abcdef0"

    def test_s3_bucket(self):
        arn = "arn:aws:s3:::my-test-bucket"
        result = aws_arn.parse_arn(arn)
        assert result["service"] == "s3"
        assert result["sub_service"] == "bucket"
        assert result["region"] == ""
        assert result["account"] == ""

    def test_iam_role_no_region_no_account(self):
        arn = "arn:aws:iam::123456789012:role/MyRole"
        result = aws_arn.parse_arn(arn)
        assert result["service"] == "iam"
        assert result["sub_service"] == "role"
        assert result["region"] == ""
        assert result["account"] == "123456789012"

    def test_sns_topic(self):
        arn = "arn:aws:sns:us-east-1:123456789012:MyTopic"
        result = aws_arn.parse_arn(arn)
        assert result["service"] == "sns"
        assert result["sub_service"] == "topic"

    def test_sqs_queue(self):
        arn = "arn:aws:sqs:us-east-1:123456789012:MyQueue"
        result = aws_arn.parse_arn(arn)
        assert result["service"] == "sqs"
        assert result["sub_service"] == "queue"

    def test_acm_certificate(self):
        arn = "arn:aws:acm:us-east-1:123456789012:certificate/abc123-def456-ghi789"
        result = aws_arn.parse_arn(arn)
        assert result["service"] == "acm"
        assert result["sub_service"] == "certificate"
        assert result["terraform"] == "aws_acm_certificate"
        assert result["cloudformation"] == "AWS::CertificateManager::Certificate"
        assert result["asff_resource"] == "AwsCertificateManagerCertificate"

    def test_invalid_arn_raises_value_error(self):
        with pytest.raises(ValueError, match="Invalid ARN"):
            aws_arn.parse_arn("not-an-arn")


# ---------------------------------------------------------------------------
# generate_arn
# ---------------------------------------------------------------------------


class TestGenerateArn:
    def test_generate_ec2_instance(self):
        arn = aws_arn.generate_arn(
            resource_id="i-1234567890abcdef0",
            service="ec2",
            sub_service="instance",
            region="us-east-1",
            account="123456789012",
            partition="aws",
        )
        assert arn == "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"

    def test_generate_acm_certificate(self):
        arn = aws_arn.generate_arn(
            resource_id="abc123",
            service="acm",
            sub_service="certificate",
            region="us-east-1",
            account="123456789012",
            partition="aws",
        )
        assert arn == "arn:aws:acm:us-east-1:123456789012:certificate/abc123"

    def test_generate_invalid_service_raises(self):
        with pytest.raises(KeyError):
            aws_arn.generate_arn(
                resource_id="id",
                service="nonexistent",
                sub_service="resource",
                region="us-east-1",
                account="123456789012",
                partition="aws",
            )


# ---------------------------------------------------------------------------
# generate_arn_from_terraform
# ---------------------------------------------------------------------------


class TestGenerateArnFromTerraform:
    def test_valid_terraform(self):
        arn = aws_arn.generate_arn_from_terraform(
            resource_id="abc123",
            terraform="aws_acm_certificate",
            region="us-east-1",
            account="123456789012",
            partition="aws",
        )
        assert "acm" in arn
        assert "certificate" in arn

    def test_invalid_terraform_prefix_raises(self):
        with pytest.raises(ValueError, match="Invalid Terraform resource"):
            aws_arn.generate_arn_from_terraform(
                resource_id="id",
                terraform="invalid_resource",
                region="us-east-1",
                account="123456789012",
                partition="aws",
            )

    def test_unknown_terraform_resource_raises(self):
        with pytest.raises(ValueError):
            aws_arn.generate_arn_from_terraform(
                resource_id="id",
                terraform="aws_nonexistent_resource_xyz",
                region="us-east-1",
                account="123456789012",
                partition="aws",
            )


# ---------------------------------------------------------------------------
# generate_arn_from_cloudformation
# ---------------------------------------------------------------------------


class TestGenerateArnFromCloudformation:
    def test_valid_cloudformation(self):
        arn = aws_arn.generate_arn_from_cloudformation(
            resource_id="abc123",
            cloudformation="AWS::CertificateManager::Certificate",
            region="us-east-1",
            account="123456789012",
            partition="aws",
        )
        assert "acm" in arn

    def test_invalid_cloudformation_prefix_raises(self):
        with pytest.raises(ValueError, match="Invalid CloudFormation resource"):
            aws_arn.generate_arn_from_cloudformation(
                resource_id="id",
                cloudformation="NotAWS::Resource::Type",
                region="us-east-1",
                account="123456789012",
                partition="aws",
            )

    def test_unknown_cloudformation_resource_raises(self):
        with pytest.raises(ValueError):
            aws_arn.generate_arn_from_cloudformation(
                resource_id="id",
                cloudformation="AWS::Nonexistent::Resource",
                region="us-east-1",
                account="123456789012",
                partition="aws",
            )


# ---------------------------------------------------------------------------
# generate_arn_from_asff
# ---------------------------------------------------------------------------


class TestGenerateArnFromAsff:
    def test_valid_asff(self):
        arn = aws_arn.generate_arn_from_asff(
            resource_id="abc123",
            asff_resource="AwsCertificateManagerCertificate",
            region="us-east-1",
            account="123456789012",
            partition="aws",
        )
        assert "acm" in arn

    def test_invalid_asff_prefix_raises(self):
        with pytest.raises(ValueError, match="Invalid ASFF resource"):
            aws_arn.generate_arn_from_asff(
                resource_id="id",
                asff_resource="InvalidAsffResource",
                region="us-east-1",
                account="123456789012",
                partition="aws",
            )

    def test_unknown_asff_resource_raises(self):
        with pytest.raises(ValueError):
            aws_arn.generate_arn_from_asff(
                resource_id="id",
                asff_resource="AwsNonexistentResourceXyz",
                region="us-east-1",
                account="123456789012",
                partition="aws",
            )


# ---------------------------------------------------------------------------
# get_service_from_arn
# ---------------------------------------------------------------------------


class TestGetServiceFromArn:
    def test_ec2(self):
        assert (
            aws_arn.get_service_from_arn("arn:aws:ec2:us-east-1:123456789012:instance/i-abc")
            == "ec2"
        )

    def test_s3(self):
        assert aws_arn.get_service_from_arn("arn:aws:s3:::my-bucket") == "s3"

    def test_iam(self):
        assert aws_arn.get_service_from_arn("arn:aws:iam::123456789012:role/MyRole") == "iam"

    def test_elb_classic(self):
        assert (
            aws_arn.get_service_from_arn(
                "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/my-lb"
            )
            == "elb"
        )

    def test_elbv2_app(self):
        assert (
            aws_arn.get_service_from_arn(
                "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-lb/abc123"
            )
            == "elbv2"
        )


# ---------------------------------------------------------------------------
# get_sub_service_from_arn
# ---------------------------------------------------------------------------


class TestGetSubServiceFromArn:
    def test_ec2_instance(self):
        assert (
            aws_arn.get_sub_service_from_arn("arn:aws:ec2:us-east-1:123456789012:instance/i-abc")
            == "instance"
        )

    def test_s3_bucket(self):
        assert aws_arn.get_sub_service_from_arn("arn:aws:s3:::my-bucket") == "bucket"

    def test_iam_role(self):
        assert aws_arn.get_sub_service_from_arn("arn:aws:iam::123456789012:role/MyRole") == "role"

    def test_sns_topic(self):
        assert (
            aws_arn.get_sub_service_from_arn("arn:aws:sns:us-east-1:123456789012:MyTopic")
            == "topic"
        )

    def test_elbv2_app_loadbalancer(self):
        assert (
            aws_arn.get_sub_service_from_arn(
                "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-lb/abc123"
            )
            == "app_loadbalancer"
        )


# ---------------------------------------------------------------------------
# get_service_from_terraform / cloudformation / asff
# ---------------------------------------------------------------------------


class TestGetServiceFromLookup:
    def test_from_terraform(self):
        svc, sub = aws_arn.get_service_from_terraform("aws_acm_certificate")
        assert svc == "acm"
        assert sub == "certificate"

    def test_from_cloudformation(self):
        svc, sub = aws_arn.get_service_from_cloudformation("AWS::CertificateManager::Certificate")
        assert svc == "acm"
        assert sub == "certificate"

    def test_from_asff(self):
        svc, sub = aws_arn.get_service_from_asff("AwsCertificateManagerCertificate")
        assert svc == "acm"
        assert sub == "certificate"

    def test_invalid_terraform_raises(self):
        with pytest.raises(ValueError):
            aws_arn.get_service_from_terraform("aws_nonexistent_xyz")

    def test_invalid_cloudformation_raises(self):
        with pytest.raises(ValueError):
            aws_arn.get_service_from_cloudformation("AWS::Nonexistent::Resource")

    def test_invalid_asff_raises(self):
        with pytest.raises(ValueError):
            aws_arn.get_service_from_asff("AwsNonexistentXyz")


# ---------------------------------------------------------------------------
# check_resource_id_regexp
# ---------------------------------------------------------------------------


class TestCheckResourceIdRegexp:
    def test_valid_certificate_id(self):
        assert aws_arn.check_resource_id_regexp("abc123-def456", "acm", "certificate") is True

    def test_invalid_ec2_instance_id(self):
        assert aws_arn.check_resource_id_regexp("not-an-instance-id", "ec2", "instance") is False

    def test_valid_ec2_instance_id(self):
        assert aws_arn.check_resource_id_regexp("i-1234567890abcdef0", "ec2", "instance") is True


# ---------------------------------------------------------------------------
# validate_terraform / cloudformation / asff
# ---------------------------------------------------------------------------


class TestValidators:
    def test_valid_terraform(self):
        assert aws_arn.validate_terraform("aws_acm_certificate") is True

    def test_invalid_terraform(self):
        assert aws_arn.validate_terraform("acm_certificate") is False

    def test_valid_cloudformation(self):
        assert aws_arn.validate_cloudformation("AWS::CertificateManager::Certificate") is True

    def test_invalid_cloudformation(self):
        assert aws_arn.validate_cloudformation("CertificateManager::Certificate") is False

    def test_valid_asff(self):
        assert aws_arn.validate_asff("AwsCertificateManagerCertificate") is True

    def test_invalid_asff(self):
        assert aws_arn.validate_asff("CertificateManagerCertificate") is False


# ---------------------------------------------------------------------------
# __version__
# ---------------------------------------------------------------------------


def test_version_defined():
    assert hasattr(aws_arn, "__version__")
    assert isinstance(aws_arn.__version__, str)
    assert aws_arn.__version__
