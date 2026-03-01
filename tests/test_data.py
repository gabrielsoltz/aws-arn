"""Data integrity tests for aws_arn_data."""

import pytest

from aws_arn.data import aws_arn_data

REQUIRED_KEYS = {"arn_format", "id_name", "id_regexp", "asff_name", "cloudformation", "terraform"}


def all_resources():
    """Yield (service, sub_service, attrs) for every entry in aws_arn_data."""
    for service, resources in aws_arn_data.items():
        for sub_service, attrs in resources.items():
            yield service, sub_service, attrs


@pytest.mark.parametrize("service,sub_service,attrs", list(all_resources()))
def test_required_keys_present(service, sub_service, attrs):
    missing = REQUIRED_KEYS - set(attrs.keys())
    assert not missing, f"{service}/{sub_service} is missing keys: {missing}"


@pytest.mark.parametrize("service,sub_service,attrs", list(all_resources()))
def test_arn_format_has_partition(service, sub_service, attrs):
    arn = attrs["arn_format"]
    assert "{partition}" in arn, f"{service}/{sub_service} arn_format missing {{partition}}: {arn}"


@pytest.mark.parametrize("service,sub_service,attrs", list(all_resources()))
def test_arn_format_no_typos(service, sub_service, attrs):
    arn = attrs["arn_format"]
    assert "{Partition}" not in arn, (
        f"{service}/{sub_service} has {{Partition}} typo (should be lowercase): {arn}"
    )
    assert "{gegion}" not in arn, (
        f"{service}/{sub_service} has {{gegion}} typo (should be {{region}}): {arn}"
    )
    assert "{Region}" not in arn, (
        f"{service}/{sub_service} has {{Region}} typo (should be lowercase): {arn}"
    )


@pytest.mark.parametrize("service,sub_service,attrs", list(all_resources()))
def test_terraform_prefix(service, sub_service, attrs):
    tf = attrs["terraform"]
    if tf:
        assert tf.startswith("aws_"), (
            f"{service}/{sub_service} terraform value doesn't start with 'aws_': {tf}"
        )


@pytest.mark.parametrize("service,sub_service,attrs", list(all_resources()))
def test_cloudformation_prefix(service, sub_service, attrs):
    cf = attrs["cloudformation"]
    if cf:
        assert cf.startswith("AWS::"), (
            f"{service}/{sub_service} cloudformation value doesn't start with 'AWS::': {cf}"
        )


@pytest.mark.parametrize("service,sub_service,attrs", list(all_resources()))
def test_asff_prefix(service, sub_service, attrs):
    asff = attrs["asff_name"]
    if asff:
        assert asff.startswith("Aws"), (
            f"{service}/{sub_service} asff_name doesn't start with 'Aws': {asff}"
        )


@pytest.mark.parametrize("service,sub_service,attrs", list(all_resources()))
def test_id_regexp_is_valid_regex(service, sub_service, attrs):
    import re

    pattern = attrs["id_regexp"]
    if pattern:
        try:
            re.compile(pattern)
        except re.error as e:
            pytest.fail(f"{service}/{sub_service} has invalid id_regexp '{pattern}': {e}")


def test_aws_arn_data_is_not_empty():
    assert len(aws_arn_data) > 0


def test_all_services_have_resources():
    for service, resources in aws_arn_data.items():
        assert len(resources) > 0, f"Service {service} has no resources"
