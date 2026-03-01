"""CLI tests for aws_arn."""

import subprocess
import sys


def run_cli(*args):
    """Run the aws-arn CLI as a module and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, "-m", "aws_arn.main"] + list(args),
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


class TestListServices:
    def test_list_services(self):
        code, out, err = run_cli("--list-services")
        assert code == 0
        assert "acm" in out
        assert "ec2" in out
        assert "Total number of services:" in out

    def test_list_sub_services(self):
        code, out, err = run_cli("--list-sub-services")
        assert code == 0
        assert "certificate" in out
        assert "Total number of resources:" in out


class TestParseArn:
    def test_parse_valid_arn(self):
        arn = "arn:aws:acm:us-east-1:123456789012:certificate/abc123"
        code, out, err = run_cli("--parse-arn", arn)
        assert code == 0
        assert "acm" in out
        assert "certificate" in out

    def test_parse_invalid_arn(self):
        code, out, err = run_cli("--parse-arn", "not-an-arn")
        # Returns 0 but prints error message
        assert "Invalid ARN" in out or code != 0


class TestGenerateArn:
    def test_generate_acm_certificate(self):
        code, out, err = run_cli(
            "--generate-arn",
            "--id",
            "abc123",
            "--service",
            "acm",
            "--sub-service",
            "certificate",
            "--region",
            "us-east-1",
            "--account",
            "123456789012",
            "--partition",
            "aws",
        )
        assert code == 0
        assert "arn:aws:acm:us-east-1:123456789012:certificate/abc123" in out

    def test_generate_from_terraform(self):
        code, out, err = run_cli(
            "--generate-arn-from-terraform",
            "--id",
            "abc123",
            "--terraform",
            "aws_acm_certificate",
            "--region",
            "us-east-1",
            "--account",
            "123456789012",
            "--partition",
            "aws",
        )
        assert code == 0
        assert "arn:aws:acm:us-east-1:123456789012:certificate/abc123" in out

    def test_generate_from_cloudformation(self):
        code, out, err = run_cli(
            "--generate-arn-from-cloudformation",
            "--id",
            "abc123",
            "--cloudformation",
            "AWS::CertificateManager::Certificate",
            "--region",
            "us-east-1",
            "--account",
            "123456789012",
            "--partition",
            "aws",
        )
        assert code == 0
        assert "arn:aws:acm" in out

    def test_generate_from_asff(self):
        code, out, err = run_cli(
            "--generate-arn-from-asff",
            "--id",
            "abc123",
            "--asff-resource",
            "AwsCertificateManagerCertificate",
            "--region",
            "us-east-1",
            "--account",
            "123456789012",
            "--partition",
            "aws",
        )
        assert code == 0
        assert "arn:aws:acm" in out


class TestVersion:
    def test_version_flag(self):
        code, out, err = run_cli("--version")
        # --version exits with 0 and prints to stdout or stderr depending on Python version
        assert code == 0
        assert "aws-arn" in out or "aws-arn" in err


class TestGetService:
    def test_get_service_from_arn(self):
        arn = "arn:aws:acm:us-east-1:123456789012:certificate/abc123"
        code, out, err = run_cli("--get-service", arn)
        assert code == 0
        assert "acm" in out

    def test_get_service_from_terraform(self):
        code, out, err = run_cli("--get-service", "aws_acm_certificate")
        assert code == 0
        assert "acm" in out
