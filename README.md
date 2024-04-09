# aws-arn

This repository contains a list of almost all (WIP) AWS services and resources with their **ARN format**, **ID name**, **ID regexp**, **ASFF name**, **CloudFormation resource name** and **Terraform resource name**, that you can use as [Documentation](#complete-list-of-arns), as a [Python module](#python-module) or as [CLI tool](#cli-tool).

| AWS Services 	| AWS Resources 	|
|--------------	|---------------	|
| 155          	| 479           	|

# Use Cases

- Parse an ARN and get the service, resource name, region, account, and resource ID, Terraform resource name, CloudFormation resource name and ASFF resource name
- Generate ARNs for any AWS resource by passing in different parameters
  - Using service and resource name (e.g. `acm` and `certificate`)
  - Using Terraform resource name (e.g. `aws_acm_certificate`)
  - Using Cloudformation resource name (e.g. `AWS::CertificateManager::Certificate`)
  - Using ASFF resource name (e.g. `AwsCertificateManagerCertificate`)
- Get the ASFF Resource Name for any AWS resource
- Get the Cloudformation Resource Name for any AWS resource
- Get the Terraform Resource Name for any AWS resource

# Contributing

> :warning: **Work in progress**: This is a work in progress. Not all services and resources are included yet. Please open an issue or pull request if you find any errors or omissions.

The data is defined in the file [data.py](aws_arn/data.py) as Python dictionary. 

For each service:

```json
"acm": { # The Service Name (we follow boto3 naming conventions)
    "certificate": {  # The Resource Name (we follow boto3 naming conventions)
        "arn_format": "arn:{partition}:acm:{region}:{account}:certificate/{resource_id}", # The ARN format
        "id_name": "CertificateId",  # The Resource Id name
        "id_regexp": "([a-z0-9-]+)", # The Resource Id regexp
        "asff_name": "AwsCertificateManagerCertificate",   # The ASFF Resource Name
        "cloudformation": "AWS::CertificateManager::Certificate",  # The CloudFormation Resource Name
        "terraform": "aws_acm_certificate",  # The Terraform Resource Name
    }
},
```

# Python Module

```python
pip3 install aws-arn
```

## Generate ARN

```python
import aws_arn

# Generate ARN using service and resource name
print(aws_arn.generate_arn('i-1234568901', 'ec2', 'instance', 'us-east-1', '012345789012', 'aws')) 
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# Generate ARN using Terraform resource name
print(aws_arn.generate_arn_from_terraform('i-1234568901', 'aws_instance', 'us-east-1', '012345789012', 'aws'))
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# Generate ARN using Cloudformation resource name
print(aws_arn.generate_arn_from_cloudformation('i-1234568901', 'AWS::EC2::Instance', 'us-east-1', '012345789012', 'aws'))
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# Generate ARN using ASFF resource name
print(aws_arn.generate_arn_from_asff('i-1234568901', 'AwsEC2Instance', 'us-east-1', '012345789012', 'aws'))
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
```

## Parse ARN:
  
```python
import aws_arn

print(aws_arn.parse_arn('arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901'))

{
   "service":"ec2",
   "sub_service":"instance",
   "region":"us-east-1",
   "account":"012345789012",
   "resource_id":"i-1234568901",
   "asff_resource":"AwsEc2Instance",
   "terraform":"aws_instance",
   "cloudformation":"AWS::EC2::Instance"
}
```

# CLI Tool

```bash
git clone git@github.com:gabrielsoltz/aws-arn.git
./aws-arn --help
```

## Generate ARN

```bash
# Generate ARN using service and resource name
./aws-arn --generate-arn --id i-1234568901 --service ec2 --sub-service instance --region us-east-1 --account 012345789012 --partition aws
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# Generate ARN using Terraform resource name
./aws-arn --generate-arn-from-terraform --id i-1234568901 --terraform aws_instance --region us-east-1 --account 012345789012 --partition aws
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# Generate ARN using Cloudformation resource name
./aws-arn --generate-arn-from-cloudformation --id i-1234568901 --cloudformation AWS::EC2::Instance --region us-east-1 --account 012345789012 --partition aws
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

# Generate ARN using ASFF resource name
./aws-arn --generate-arn-from-asff --id i-1234568901 --asff-resource AwsEC2Instance --region us-east-1 --account 012345789012 --partition aws
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
```

## Parse ARN
```bash
./aws-arn --parse-arn arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
{'service': 'ec2', 'sub_service': 'instance', 'region': 'us-east-1', 'account': '012345789012', 'resource_id': 'i-1234568901', 'asff_resource': 'AwsEc2Instance', 'terraform': 'aws_instance', 'cloudformation': 'AWS::EC2::Instance'}
```

## Complete List of ARNs

| Service | Resource | ARN Format | ID Name | ID Regexp | ASFF Name | CloudFormation | Terraform |
|----|----|----|----|----|----|----|----|
| acm | certificate | `arn:{partition}:acm:{region}:{account}:certificate/{resource_id}` | CertificateId | `([a-z0-9-]+)` | AwsCertificateManagerCertificate | AWS::CertificateManager::Certificate | aws_acm_certificate |
| acm-pca | certificate_authority | `arn:{partition}:acm-pca:{region}:{account}:certificate-authority/{resource_id}` | CertificateAuthorityId | `([a-z0-9-]+)` |  | AWS::ACMPCA::CertificateAuthority | aws_acm_certificate_authority |
| alexaforbusiness | skill | `arn:{partition}:aplb:{region}:{account}:skill/{resource_id}` | SkillId | `([a-zA-Z0-9_\-]+)` |  | AWS::AlexaForBusiness::Skill | aws_alexa_skill |
| apigateway | api | `arn:{partition}:apigateway:{region}::/restapis/{resource_id}` | ApiId | `[a-zA-Z0-9\-]+` | AwsApiGatewayV2Api | AWS::ApiGateway::RestApi | aws_api_gateway_rest_api |
| apigateway | api_key | `arn:{partition}:apigateway:{region}::/apikeys/{resource_id}` | ApiKeyId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::ApiKey | aws_api_gateway_api_key |
| apigateway | authorizer | `arn:{partition}:apigateway:{region}::/restapis/{api_id}/authorizers/{resource_id}` | AuthorizerId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::Authorizer | aws_api_gateway_authorizer |
| apigateway | base_path_mapping | `arn:{partition}:apigateway:{region}::/restapis/{api_id}/basepathmappings/{resource_id}` | BasePathMappingId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::BasePathMapping | aws_api_gateway_base_path_mapping |
| apigateway | client_certificate | `arn:{partition}:apigateway:{region}::/clientcertificates/{resource_id}` | ClientCertificateId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::ClientCertificate | aws_api_gateway_client_certificate |
| apigateway | deployment | `arn:{partition}:apigateway:{region}::/restapis/{api_id}/deployments/{resource_id}` | DeploymentId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::Deployment | aws_api_gateway_deployment |
| apigateway | documentation_part | `arn:{partition}:apigateway:{region}::/restapis/{api_id}/documentation/parts/{resource_id}` | DocumentationPartId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::DocumentationPart | aws_api_gateway_documentation_part |
| apigateway | documentation_version | `arn:{partition}:apigateway:{region}::/restapis/{api_id}/documentation/versions/{resource_id}` | DocumentationVersion | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::DocumentationVersion | aws_api_gateway_documentation_version |
| apigateway | domain_name | `arn:{partition}:apigateway:{region}::/domainnames/{resource_id}` | DomainName | `[a-zA-Z0-9\.\-_]+` |  | AWS::ApiGateway::DomainName | aws_api_gateway_domain_name |
| apigateway | gateway_response | `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/gatewayresponses/{resource_id}` | GatewayResponseId | `[a-zA-Z0-9\.\-_]+` |  | AWS::ApiGateway::GatewayResponse | aws_api_gateway_gateway_response |
| apigateway | integration | `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{ResourceId}/methods/{HttpMethod}/integrations/{resource_id}` | IntegrationId | `[a-zA-Z0-9\.\-_]+` |  | AWS::ApiGateway::Integration | aws_api_gateway_integration |
| apigateway | method | `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{ResourceId}/methods/{resource_id}` | HttpMethod | `[a-zA-Z0-9\.\-_]+` |  | AWS::ApiGateway::Method | aws_api_gateway_method |
| apigateway | model | `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/models/{resource_id}` | ModelName | `[a-zA-Z0-9\.\-_]+` |  | AWS::ApiGateway::Model | aws_api_gateway_model |
| apigateway | request_validator | `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/requestvalidators/{resource_id}` | RequestValidatorId | `[a-zA-Z0-9\.\-_]+` |  | AWS::ApiGateway::RequestValidator | aws_api_gateway_request_validator |
| apigateway | resource | `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{resource_id}` | ResourceId | `[a-zA-Z0-9\.\-_]+` |  | AWS::ApiGateway::Resource | aws_api_gateway_resource |
| apigateway | rest_api | `arn:{partition}:apigateway:{region}::/restapis/{resource_id}` | ApiId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::RestApi | aws_api_gateway_rest_api |
| apigateway | stage | `arn:{partition}:apigateway:{region}::/restapis/{rest_api_id}/stages/{resource_id}` | StageName | `[a-zA-Z0-9\-_]+` | AwsApiGatewayV2Stage | AWS::ApiGateway::Stage | aws_api_gateway_stage |
| apigateway | usage_plan | `arn:{partition}:apigateway:{region}::/usageplans/{resource_id}` | UsagePlanId | `[a-zA-Z0-9\-]+` |  | AWS::ApiGateway::UsagePlan | aws_api_gateway_usage_plan |
| apigateway | usage_plan_key | `arn:{partition}:apigateway:{region}::/usageplans/{usage_plan_id}/keys/{resource_id}` | KeyId | `[a-zA-Z0-9-_]+` |  | AWS::ApiGateway::UsagePlanKey | aws_api_gateway_usage_plan_key |
| apigateway | vpc_link | `arn:{partition}:apigateway:{region}::/vpclinks/{resource_id}` | VpcLinkId | `[a-zA-Z0-9\-_]+` |  | AWS::ApiGateway::VpcLink | aws_api_gateway_vpc_link |
| appflow | connector_profile | `arn:{partition}:appflow:{region}:{account}:connectorprofile/{resource_id}` | ConnectorProfileName | `([a-zA-Z0-9-_]{1,256})` |  | AWS::AppFlow::ConnectorProfile | aws_appflow_connector_profile |
| appflow | flow | `arn:{partition}:appflow:{region}:{account}:flow/{resource_id}` | FlowName | `([a-zA-Z0-9-_]{1,256})` |  | AWS::AppFlow::Flow | aws_appflow_flow |
| apprunner | service | `arn:{partition}:apprunner:{region}:{account}:service/{resource_id}` | Service | `([a-zA-Z0-9-_]{1,256})` |  | AWS::AppRunner::Service | aws_apprunner_service |
| apprunner | connection | `arn:{partition}:apprunner:{region}:{account}:connection/{ConnectionName}/{resource_id}` | Connection | `([a-zA-Z0-9-_]{1,256})` |  |  | aws_apprunner_connection |
| apprunner | auto_scaling_configuration | `arn:{partition}:apprunner:{region}:{account}:autoscalingconfiguration/{resource_name}/{AutoScalingConfigurationVersion}/{resource_id}` | AutoScalingConfiguration | `([a-zA-Z0-9-_]{1,256})` |  | AWS::AppRunner::AutoScalingConfiguration | aws_apprunner_auto_scaling_configuration_version |
| apprunner | observability_configuration | `arn:{Partition}:apprunner:{gegion}:{account}:observabilityconfiguration/{resource_name}/{ObservabilityConfigurationVersion}/{resource_id}` | ObservabilityConfiguration | `([a-zA-Z0-9-_]{1,256})` |  | AWS::AppRunner::ObservabilityConfiguration | aws_apprunner_observability_configuration |
| apprunner | vpc_connector | `arn:{partition}:apprunner:{gegion}:{account}:vpcconnector/{resource_name}/{VpcConnectorVersion}/{resource_id}` | VpcConnector | `([a-zA-Z0-9-_]{1,256})` |  | AWS::AppRunner::VpcConnector | aws_apprunner_vpc_connector |
| apprunner | vpc_ingress_connection | `arn:{partition}:apprunner:{region}:{account}:vpcingressconnection/{resource_name}/{resource_id}` | vpc_ingress_connection | `([a-zA-Z0-9-_]{1,256})` |  | AWS::AppRunner::VpcIngressConnection | aws_apprunner_vpc_ingress_connection |
| appstream | directory_config | `arn:{partition}:appstream:{region}:{account}:directoryconfig/{resource_id}` | DirectoryConfigName | `[a-zA-Z0-9-]+` |  | AWS::AppStream::DirectoryConfig | aws_appstream_directory_config |
| appstream | fleet | `arn:{partition}:appstream:{region}:{account}:fleet/{resource_id}` | FleetName | `[a-zA-Z0-9-]+` |  | AWS::AppStream::Fleet | aws_appstream_fleet |
| appstream | image | `arn:{partition}:appstream:{region}:{account}:image/{resource_id}` | ImageName | `[a-zA-Z0-9-]+` |  | AWS::AppStream::Image | aws_appstream_image |
| appstream | image_builder | `arn:{partition}:appstream:{region}:{account}:imagebuilder/{resource_id}` | ImageBuilderName | `[a-zA-Z0-9-]+` |  | AWS::AppStream::ImageBuilder | aws_appstream_image_builder |
| appstream | stack | `arn:{partition}:appstream:{region}:{account}:stack/{resource_id}` | StackName | `[a-zA-Z0-9-]+` |  | AWS::AppStream::Stack | aws_appstream_stack |
| athena | workgroup | `arn:{partition}:athena:{region}:{account}:workgroup/{resource_id}` | WorkGroupName | `([a-zA-Z0-9._-]+)` |  | AWS::Athena::WorkGroup | aws_athena_workgroup |
| augmentedairuntime | human_loop | `arn:{partition}:sagemaker:{region}:{account}:human-loop/{resource_id}` | HumanLoopName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*` |  | AWS::SageMaker::HumanTaskUi | aws_sagemaker_human_task_ui |
| autoscaling | auto_scaling_group | `arn:{partition}:autoscaling:{region}:{account}:autoScalingGroup/{resource_id}` | AutoScalingGroupName | `[a-zA-Z0-9-]{1,255}` | AwsAutoScalingAutoScalingGroup | AWS::AutoScaling::AutoScalingGroup | aws_autoscaling_group |
| autoscaling | launch_configuration | `arn:{partition}:autoscaling:{region}:{account}:launchConfiguration/{resource_id}` | LaunchConfigurationName | `[a-zA-Z0-9-]{1,255}` | AwsAutoScalingLaunchConfiguration | AWS::AutoScaling::LaunchConfiguration | aws_launch_configuration |
| backup | backup_plan | `arn:{partition}:backup:{region}:{account}:backup-plan/{resource_id}` | BackupPlanId | `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` | AwsBackupBackupPlan | AWS::Backup::BackupPlan | aws_backup_plan |
| backup | backup_vault | `arn:{partition}:backup:{region}:{account}:backup-vault/{resource_id}` | BackupVaultName | `^[a-zA-Z0-9_-]{1,50}$` | AwsBackupBackupVault | AWS::Backup::BackupVault | aws_backup_vault |
| backup | recovery_plan | `arn:{partition}:backup:{region}:{account}:recoveryplan/{resource_id}` | RecoveryPlanName | `^[a-zA-Z0-9\-\_\.]+$` | AwsBackupRecoveryPoint | AWS::Backup::RecoveryPlan | aws_backup_recovery_point |
| batch | compute_environment | `arn:{partition}:batch:{region}:{account}:compute-environment/{resource_id}` | ComputeEnvironmentName | `[a-zA-Z0-9_-]+` |  | AWS::Batch::ComputeEnvironment | aws_batch_compute_environment |
| batch | job_definition | `arn:{partition}:batch:{region}:{account}:job-definition/{resource_id}:{version}` | JobDefinitionName | `[a-zA-Z0-9_-]+` |  | AWS::Batch::JobDefinition | aws_batch_job_definition |
| batch | job_queue | `arn:{partition}:batch:{region}:{account}:job-queue/{resource_id}` | JobQueueName | `[a-zA-Z0-9_-]+` |  | AWS::Batch::JobQueue | aws_batch_job_queue |
| budgets | budget | `arn:{partition}:budgets:{region}:{account}:budget/{resource_id}` | BudgetName | `([a-zA-Z0-9-_.]+)` |  | AWS::Budgets::Budget | aws_budgets_budget |
| cloud9 | environment | `arn:{partition}:cloud9:{region}:{account}:environment:{resource_id}` | EnvironmentId | `[a-zA-Z0-9-]+` |  | AWS::Cloud9::EnvironmentEC2 | aws_cloud9_environment_ec2 |
| cloudformation | change_set | `arn:{partition}:cloudformation:{region}:{account}:changeSet/{resource_id}` | ChangeSetId | `([a-zA-Z0-9-]+)` |  | AWS::CloudFormation::ChangeSet | aws_cloudformation_change_set |
| cloudformation | stack | `arn:{partition}:cloudformation:{region}:{account}:stack/{resource_id}/{stack_id}` | StackName | `([a-zA-Z][-a-zA-Z0-9]*)` | AwsCloudFormationStack | AWS::CloudFormation::Stack | aws_cloudformation_stack |
| cloudfront | distribution | `arn:{partition}:cloudfront::{account}:distribution/{resource_id}` | DistributionId | `[A-Z0-9]+` | AwsCloudFrontDistribution | AWS::CloudFront::Distribution | aws_cloudfront_distribution |
| cloudfront | field_level_encryption_config | `arn:{partition}:cloudfront::{account}:field-level-encryption-config/{resource_id}` | FieldLevelEncryptionConfigId | `[A-Z0-9]+` |  | AWS::CloudFront::FieldLevelEncryptionConfig | aws_cloudfront_field_level_encryption_config |
| cloudfront | field_level_encryption_profile | `arn:{partition}:cloudfront::{account}:field-level-encryption-profile/{resource_id}` | FieldLevelEncryptionProfileId | `[A-Z0-9]+` |  | AWS::CloudFront::FieldLevelEncryptionProfile | aws_cloudfront_field_level_encryption_profile |
| cloudfront | realtime_log_config | `arn:{partition}:cloudfront::{account}:realtime-log-config/{resource_id}` | RealtimeLogConfigId | `[A-Z0-9]+` |  | AWS::CloudFront::RealtimeLogConfig | aws_cloudfront_realtime_log_config |
| cloudhsmv2 | cluster | `arn:{partition}:cloudhsmv2:{region}:{account}:cluster/{resource_id}` | ClusterId | `[a-zA-Z0-9-]+` |  | AWS::CloudHSMV2::Cluster | aws_cloudhsmv2_cluster |
| cloudhsmv2 | backup | `arn:{partition}:cloudhsmv2:{region}:{account}:backup/{resource_id}` | BackupId | `[a-zA-Z0-9-]+` |  | AWS::CloudHSMV2::Backup | aws_cloudhsmv2_backup |
| cloudhsmv2 | hsm | `arn:{partition}:cloudhsmv2:{region}:{account}:cluster/{resource_id}/hsm/{hsm_id}` | HsmId | `[a-zA-Z0-9-]+` |  | AWS::CloudHSMV2::Hsm | aws_cloudhsmv2_hsm |
| cloudtrail | trail | `arn:{partition}:cloudtrail:{region}:{account}:trail/{resource_id}` | TrailName | `[a-zA-Z0-9-_\.]+` | AwsCloudTrailTrail | AWS::CloudTrail::Trail | aws_cloudtrail |
| cloudwatch | alarm | `arn:{partition}:cloudwatch:{region}:{account}:alarm:{resource_id}` | AlarmName | `^[a-zA-Z0-9\-_]{1,255}$` | AwsCloudWatchAlarm | AWS::CloudWatch::Alarm | aws_cloudwatch_metric_alarm |
| cloudwatch | dashboard | `arn:{partition}:cloudwatch::{account}:dashboard/{resource_id}` | DashboardName | `^[a-zA-Z0-9-_ ]{3,255}$` |  | AWS::CloudWatch::Dashboard | aws_cloudwatch_dashboard |
| codeartifact | domain | `arn:{partition}:codeartifact:{region}:{account}:domain/{resource_id}` | DomainName | `([a-zA-Z0-9._-]+)` |  | AWS::CodeArtifact::Domain | aws_codeartifact_domain |
| codeartifact | repository | `arn:{partition}:codeartifact:{region}:{account}:repository/{domain_name}/{resource_id}` | RepositoryName | `([a-zA-Z0-9._-]+)` |  | AWS::CodeArtifact::Repository | aws_codeartifact_repository |
| codeartifact | package | `arn:{partition}:codeartifact:{region}:{account}:repository/{domain_name}/{repository_name}/package/{package_format}/{resource_id}@{package_version}` | PackageName | `([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+)` |  | AWS::CodeArtifact::Package | aws_codeartifact_package |
| codebuild | project | `arn:{partition}:codebuild:{region}:{account}:project/{resource_id}` | ProjectName | `([a-zA-Z0-9-_]+)` | AwsCodeBuildProject | AWS::CodeBuild::Project | aws_codebuild_project |
| codecommit | repository | `arn:{partition}:codecommit:{region}:{account}:{resource_id}` | RepositoryName | `([a-zA-Z0-9_.-]+)` |  | AWS::CodeCommit::Repository | aws_codecommit_repository |
| codedeploy | application | `arn:{partition}:codedeploy:{region}:{account}:application:{resource_id}` | ApplicationName | `([a-zA-Z0-9-_]+)` |  | AWS::CodeDeploy::Application | aws_codedeploy_app |
| codedeploy | deployment_config | `arn:{partition}:codedeploy:{region}:{account}:deploymentconfig:{resource_id}` | DeploymentConfigName | `([a-zA-Z0-9-_]+)` |  | AWS::CodeDeploy::DeploymentConfig | aws_codedeploy_deployment_config |
| codedeploy | deployment_group | `arn:{partition}:codedeploy:{region}:{account}:deploymentgroup:{resource_id}` | ApplicationName/DeploymentGroupName | `([a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+)` |  | AWS::CodeDeploy::DeploymentGroup | aws_codedeploy_deployment_group |
| codepipeline | pipeline | `arn:{partition}:codepipeline:{region}:{account}:{resource_type}/{resource_id}` | PipelineName | `([a-zA-Z0-9_\-]+)` |  | AWS::CodePipeline::Pipeline | aws_codepipeline |
| codestar-connections | connection | `arn:{partition}:codestar-connections:{region}:{account}:connection/{resource_id}` | ConnectionName | `([a-zA-Z0-9-]+)` |  | AWS::CodeStarConnections::Connection | aws_codestarconnections_connection |
| codestar-notifications | rule | `arn:{partition}:codestar-notifications:{region}:{account}:notificationrule/{resource_id}` | NotificationRuleId | `([a-zA-Z0-9-_]+)` |  | AWS::CodeStarNotifications::NotificationRule | aws_codestarnotifications_notification_rule |
| cognito-idp | identity_provider | `arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id}:identityprovider/{resource_id}` | IdentityProviderName | `([a-zA-Z0-9_\.\-]+)` |  | AWS::Cognito::UserPoolIdentityProvider | aws_cognito_identity_provider |
| cognito-idp | resource_server | `arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id}/resource-server/{resource_id}` | ResourceServerIdentifier | `([a-zA-Z0-9_\.\-]+)` |  | AWS::Cognito::UserPoolResourceServer | aws_cognito_user_pool_resource_server |
| cognito-idp | user_pool | `arn:{partition}:cognito-idp:{region}:{account}:userpool/{resource_id}` | UserPoolId | `([a-zA-Z0-9_\.\-]+)` |  | AWS::Cognito::UserPool | aws_cognito_user_pool |
| comprehend | document_classifier | `arn:{partition}:comprehend:{region}:{account}:document-classifier/{resource_id}` | DocumentClassifierName | `([a-zA-Z0-9-_]+)` |  | AWS::Comprehend::DocumentClassifier | aws_comprehend_document_classifier |
| comprehend | entity_recognizer | `arn:{partition}:comprehend:{region}:{account}:entity-recognizer/{resource_id}` | EntityRecognizerName | `([a-zA-Z0-9-_]+)` |  | AWS::Comprehend::EntityRecognizer | aws_comprehend_entity_recognizer |
| comprehend | key_phrases_detection_job | `arn:{partition}:comprehend:{region}:{account}:key-phrases-detection-job/{resource_id}` | KeyPhrasesDetectionJobName | `([a-zA-Z0-9-_]+)` |  | AWS::Comprehend::KeyPhrasesDetectionJob | aws_comprehend_key_phrases_detection_job |
| comprehend | sentiment_detection_job | `arn:{partition}:comprehend:{region}:{account}:sentiment-detection-job/{resource_id}` | SentimentDetectionJobName | `([a-zA-Z0-9-_]+)` |  | AWS::Comprehend::SentimentDetectionJob | aws_comprehend_sentiment_detection_job |
| comprehend | topic_detection_job | `arn:{partition}:comprehend:{region}:{account}:topic-detection-job/{resource_id}` | TopicDetectionJobName | `([a-zA-Z0-9-_]+)` |  | AWS::Comprehend::TopicDetectionJob | aws_comprehend_topic_detection_job |
| compute-optimizer | recommendation_export_job | `arn:{partition}:compute-optimizer:{region}:{account}:recommendation-export-job/{resource_id}` | ExportJobId | `([a-z0-9-]+)` |  | AWS::ComputeOptimizer::RecommendationExportJob | aws_compute_optimizer_export_destination |
| config | aggregator | `arn:{partition}:config:{region}:{account}:config-aggregator/{resource_id}` | ConfigAggregatorName | `([a-zA-Z0-9-_]+)` |  | AWS::Config::Aggregator | aws_config_configuration_aggregator |
| config | conformance_pack | `arn:{partition}:config:{region}:{account}:conformance-pack/{resource_id}` | ConformancePackName | `([a-zA-Z0-9-_]+)` |  | AWS::Config::ConformancePack | aws_config_conformance_pack |
| config | config_rule | `arn:{partition}:config:{region}:{account}:config-rule/{resource_id}` | ConfigRuleName | `([a-zA-Z0-9-_]+)` |  | AWS::Config::ConfigRule | aws_config_config_rule |
| config | organization_config_rule | `arn:{partition}:config:{region}:{account}:organization-config-rule/{resource_id}` | OrganizationConfigRuleName | `([a-zA-Z0-9-_]+)` |  | AWS::Config::OrganizationConfigRule | aws_config_organization_custom_rule |
| config | remediation_configuration | `arn:{partition}:config:{region}:{account}:remediation-configuration/{resource_id}` | RemediationConfigurationName | `([a-zA-Z0-9-_]+)` |  | AWS::Config::RemediationConfiguration | aws_config_remediation_configuration |
| config | config_recorder | `arn:{partition}:config:{region}:{account}:config_recorder/{resource_id}` | ConfigRecorderName | `([a-zA-Z0-9-_]+)` |  | AWS::Config::ConfigurationRecorder | aws_config_configuration_recorder |
| cur | report_definition | `arn:{partition}:cur:{region}:{account}:{ReportName}-{YYYYMM}-{AdditionalArtifact}-{region}-{account}` | ReportName | `([a-zA-Z0-9-_.]+)` |  | AWS::CUR::ReportDefinition | aws_cur_report_definition |
| dataexchange | asset | `arn:{partition}:dataexchange:{region}:{account}:asset/{resource_id}` | AssetId | `([a-zA-Z0-9-_.]+)` |  | AWS::DataExchange::Asset | aws_dataexchange_asset |
| dataexchange | data_set | `arn:{partition}:dataexchange:{region}:{account}:data-sets/{resource_id}` | DataSetId | `([a-zA-Z0-9-_.]+)` |  | AWS::DataExchange::DataSet | aws_dataexchange_data_set |
| dataexchange | job | `arn:{partition}:dataexchange:{region}:{account}:job/{resource_id}` | JobId | `([a-zA-Z0-9-_.]+)` |  | AWS::DataExchange::Job | aws_dataexchange_job |
| dataexchange | revision | `arn:{partition}:dataexchange:{region}:{account}:revision/{resource_id}` | RevisionId | `([a-zA-Z0-9-_.]+)` |  | AWS::DataExchange::Revision | aws_dataexchange_revision |
| datapipeline | pipeline | `arn:{partition}:datapipeline:{region}:{account}:{resource_type}/{resource_id}` | PipelineId | `([a-zA-Z0-9_-]+)` |  | AWS::DataPipeline::Pipeline | aws_datapipeline_pipeline |
| dax | cluster | `arn:{partition}:dax:{region}:{account}:cluster:{resource_id}` | ClusterName | `([a-zA-Z0-9_.-]+)` |  | AWS::DAX::Cluster | aws_dax_cluster |
| devicefarm | project | `arn:{partition}:devicefarm:{region}:{account}:project:{resource_id}` | ProjectArnSuffix | `([a-zA-Z0-9-_.]+)` |  | AWS::DeviceFarm::Project | aws_devicefarm_project |
| devicefarm | device_instance | `arn:{partition}:devicefarm:{region}:{account}:device-instance:{resource_id}` | DeviceInstanceArnSuffix | `([a-zA-Z0-9-_.]+)` |  | AWS::DeviceFarm::DeviceInstance | aws_devicefarm_device_instance |
| devicefarm | device_pool | `arn:{partition}:devicefarm:{region}:{account}:devicepool:{resource_id}` | DevicePoolArnSuffix | `([a-zA-Z0-9-_.]+)` |  | AWS::DeviceFarm::DevicePool | aws_devicefarm_device_pool |
| devicefarm | run | `arn:{partition}:devicefarm:{region}:{account}:run:{resource_id}` | RunArnSuffix | `([a-zA-Z0-9-_.]+)` |  | AWS::DeviceFarm::Run | aws_devicefarm_run |
| devicefarm | job | `arn:{partition}:devicefarm:{region}:{account}:job:{resource_id}` | JobArnSuffix | `([a-zA-Z0-9-_.]+)` |  | AWS::DeviceFarm::Job | aws_devicefarm_job |
| devicefarm | suite | `arn:{partition}:devicefarm:{region}:{account}:suite:{resource_id}` | SuiteArnSuffix | `([a-zA-Z0-9-_.]+)` |  | AWS::DeviceFarm::Suite | aws_devicefarm_suite |
| devicefarm | test | `arn:{partition}:devicefarm:{region}:{account}:test:{resource_id}` | TestArnSuffix | `([a-zA-Z0-9-_.]+)` |  | AWS::DeviceFarm::Test | aws_devicefarm_test |
| directconnect | connection | `arn:{partition}:directconnect:{region}:{account}:dxcon:{resource_id}` | ConnectionId | `([a-zA-Z0-9-]+)` |  | AWS::DirectConnect::Connection | aws_dx_connection |
| directconnect | link_aggregation_group | `arn:{partition}:directconnect:{region}:{account}:linkaggregations:{resource_id}` | LagId | `([a-zA-Z0-9-]+)` |  | AWS::DirectConnect::LinkAggregationGroup | aws_dx_lag |
| directconnect | private_virtual_interface | `arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id}` | VirtualInterfaceId | `([a-zA-Z0-9-]+)` |  | AWS::DirectConnect::PrivateVirtualInterface | aws_dx_private_virtual_interface |
| directconnect | public_virtual_interface | `arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id}` | VirtualInterfaceId | `([a-zA-Z0-9-]+)` |  | AWS::DirectConnect::PublicVirtualInterface | aws_dx_public_virtual_interface |
| directconnect | transit_virtual_interface | `arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id}` | VirtualInterfaceId | `([a-zA-Z0-9-]+)` |  | AWS::DirectConnect::TransitVirtualInterface | aws_dx_transit_virtual_interface |
| ds | directory | `arn:{partition}:ds:{region}:{account}:directory/{resource_id}` | DirectoryId | `([a-zA-Z0-9-]+)` |  | AWS::DirectoryService::MicrosoftAD | aws_directory_service_directory |
| dynamodb | table | `arn:{partition}:dynamodb:{region}:{account}:table/{resource_id}` | TableName | `([a-zA-Z0-9_.-]+)` | AwsDynamoDbTable | AWS::DynamoDB::Table | aws_dynamodb_table |
| ec2 | customer_gateway | `arn:{partition}:ec2:{region}:{account}:customer-gateway/{resource_id}` | CustomerGatewayId | `^cgw-[a-f0-9]{8}$` | AwsEc2CustomerGateway | AWS::EC2::CustomerGateway | aws_customer_gateway |
| ec2 | dedicated_host | `arn:{partition}:ec2:{region}:{account}:host/{resource_id}` | DedicatedHostId | `^h-[0-9a-f]{17}$` | AwsEc2DedicatedHost | AWS::EC2::Host | aws_ec2_host |
| ec2 | dhcp_options | `arn:{partition}:ec2:{region}:{account}:dhcp-options/{resource_id}` | DhcpOptionsId | `^dopt-[0-9a-fA-F]{8,17}$` | AwsEc2DhcpOptions | AWS::EC2::DHCPOptions | aws_dhcp_options |
| ec2 | egress_only_internet_gateway | `arn:{partition}:ec2:{region}:{account}:egress-only-internet-gateway/{resource_id}` | EgressOnlyInternetGatewayId | `^egress-only-igw-[a-f0-9]{8,17}$` | AwsEc2EgressOnlyInternetGateway | AWS::EC2::EgressOnlyInternetGateway | aws_egress_only_internet_gateway |
| ec2 | elastic_gpu | `arn:{partition}:ec2:{region}:{account}:elastic-gpu/{resource_id}` | ElasticGpuId | `^egp-[0-9a-f]{8,17}$` | AwsEc2ElasticGpu | AWS::EC2::ElasticGpu |  |
| ec2 | elastic_inference_accelerator | `arn:{partition}:elastic-inference:{region}:{account}:accelerator/{resource_id}` | AcceleratorId | `^eia-[0-9a-f]{17}$` | AwsElasticInferenceAccelerator | AWS::ElasticInference::Accelerator | aws_eia_accelerator |
| ec2 | eip_allocation | `arn:{partition}:ec2:{region}:{account}:eip-allocation/{resource_id}` | AllocationId | `^eipalloc-[0-9a-fA-F]{8,17}$` | AwsEc2Eip | AWS::EC2::EIP | aws_eip |
| ec2 | eip | `arn:{partition}:ec2:{region}:{account}:elastic-ip/{resource_id}` | AllocationId | `^eipalloc-[0-9a-fA-F]{8,17}$` | AwsEc2Eip | AWS::EC2::EIP | aws_eip |
| ec2 | flow_log | `arn:{partition}:ec2:{region}:{account}:flow-log/{resource_id}` | FlowLogId | `^fl-[0-9a-f]{17}$` |  | AWS::EC2::FlowLog | aws_flow_log |
| ec2 | image | `arn:{partition}:ec2:{region}:{account}:image/{resource_id}` | ImageId | `^ami-[a-f0-9]{8}$|^ami-[a-f0-9]{17}$` |  | AWS::EC2::Image | aws_ami |
| ec2 | instance | `arn:{partition}:ec2:{region}:{account}:instance/{resource_id}` | InstanceId | `^i-[0-9a-f]{8,17}$` | AwsEc2Instance | AWS::EC2::Instance | aws_instance |
| ec2 | internet_gateway | `arn:{partition}:ec2:{region}:{account}:internet-gateway/{resource_id}` | InternetGatewayId | `^igw-[a-f0-9]{8,17}$` |  | AWS::EC2::InternetGateway | aws_internet_gateway |
| ec2 | key_pair | `arn:{partition}:ec2:{region}:{account}:key-pair/{resource_id}` | KeyName | `^[a-zA-Z0-9-_=,.@()]{1,255}$` |  | AWS::EC2::KeyPair | aws_key_pair |
| ec2 | launch_template | `arn:{partition}:ec2:{region}:{account}:launch-template/{resource_id}` | LaunchTemplateId | `^lt-[a-zA-Z0-9]{17}$` | AwsEc2LaunchTemplate | AWS::EC2::LaunchTemplate | aws_launch_template |
| ec2 | natgateway | `arn:{partition}:ec2:{region}:{account}:natgateway/{resource_id}` | NatGatewayId | `^nat-[a-f0-9]{8,}$` |  | AWS::EC2::NatGateway | aws_nat_gateway |
| ec2 | network_acl | `arn:{partition}:ec2:{region}:{account}:network-acl/{resource_id}` | NetworkAclId | `^acl-[0-9a-fA-F]{8,17}$` | AwsEc2NetworkAcl | AWS::EC2::NetworkAcl | aws_network_acl |
| ec2 | network_interface | `arn:{partition}:ec2:{region}:{account}:network-interface/{resource_id}` | NetworkInterfaceId | `^eni-[0-9a-f]{8}|eni-[0-9a-f]{17}$` | AwsEc2NetworkInterface | AWS::EC2::NetworkInterface | aws_network_interface |
| ec2 | placement_group | `arn:{partition}:ec2:{region}:{account}:placement-group/{resource_id}` | PlacementGroupName | `^pg-[a-z0-9]{8}$` | AwsEc2PlacementGroup | AWS::EC2::PlacementGroup | aws_placement_group |
| ec2 | reserved_instances | `arn:{partition}:ec2:{region}:{account}:reserved-instances/{resource_id}` | ReservedInstancesId | `^i-[a-zA-Z0-9]{12}$` | AwsEc2ReservedInstances | AWS::EC2::ReservedInstances | aws_instance |
| ec2 | route_table | `arn:{partition}:ec2:{region}:{account}:route-table/{resource_id}` | RouteTableId | `^rtb-[a-f0-9]{8,17}$` | AwsEc2RouteTable | AWS::EC2::RouteTable | aws_route_table |
| ec2 | security_group | `arn:{partition}:ec2:{region}:{account}:security-group/{resource_id}` | SecurityGroupId | `^sg-[0-9a-f]{8,17}$` | AwsEc2SecurityGroup | AWS::EC2::SecurityGroup | aws_security_group |
| ec2 | snapshot | `arn:{partition}:ec2:{region}:{account}:snapshot/{resource_id}` | SnapshotId | `^snap-[a-f0-9]{8,17}$` | AwsEc2Snapshot | AWS::EC2::Snapshot | aws_ebs_snapshot |
| ec2 | spot_fleet_request | `arn:{partition}:ec2:{region}:{account}:spot-fleet-request/{resource_id}` | SpotFleetRequestId | `^sfr-[0-9a-f]{8,17}$` | AwsEc2SpotFleetRequest | AWS::EC2::SpotFleet | aws_spot_fleet_request |
| ec2 | spot_instance_request | `arn:{partition}:ec2:{region}:{account}:spot-instances-request/{resource_id}` | SpotInstanceRequestId | `^sir-[0-9a-f]{8,17}$` | AwsEc2SpotInstanceRequest | AWS::EC2::SpotInstance | aws_spot_instance_request |
| ec2 | subnet | `arn:{partition}:ec2:{region}:{account}:subnet/{resource_id}` | SubnetId | `^subnet-[0-9a-f]{8,17}$` | AwsEc2Subnet | AWS::EC2::Subnet | aws_subnet |
| ec2 | traffic_mirror_filter | `arn:{partition}:ec2:{region}:{account}:traffic-mirror-filter/{resource_id}` | TrafficMirrorFilterId | `^tmf-[a-f0-9]{17}$` |  | AWS::EC2::TrafficMirrorFilter | aws_ec2_traffic_mirror_filter |
| ec2 | traffic_mirror_session | `arn:{partition}:ec2:{region}:{account}:traffic-mirror-session/{resource_id}` | TrafficMirrorSessionId | `^tmse-[a-f0-9]{17}$` |  | AWS::EC2::TrafficMirrorSession | aws_ec2_traffic_mirror_session |
| ec2 | traffic_mirror_target | `arn:{partition}:ec2:{region}:{account}:traffic-mirror-target/{resource_id}` | TrafficMirrorTargetId | `^tmt-[a-f0-9]{17}$` |  | AWS::EC2::TrafficMirrorTarget | aws_ec2_traffic_mirror_target |
| ec2 | transit_gateway | `arn:{partition}:ec2:{region}:{account}:transit-gateway/{resource_id}` | TransitGatewayId | `^tgw-\w{8,17}$` | AwsEc2TransitGateway | AWS::EC2::TransitGateway | aws_ec2_transit_gateway |
| ec2 | transit_gateway_attachment | `arn:{partition}:ec2:{region}:{account}:transit-gateway-attachment/{resource_id}` | TransitGatewayAttachmentId | `^tgw-attach-[0-9a-f]{17}$` |  | AWS::EC2::TransitGatewayAttachment | aws_ec2_transit_gateway_attachment |
| ec2 | transit_gateway_multicast_domain | `arn:{partition}:ec2:{region}:{account}:transit-gateway-multicast-domain/{resource_id}` | TransitGatewayMulticastDomainId | `^tgmd-[a-f0-9]{8,17}$` |  | AWS::EC2::TransitGatewayMulticastDomain | aws_ec2_transit_gateway_multicast_domain |
| ec2 | transit_gateway_route_table | `arn:{partition}:ec2:{region}:{account}:transit-gateway-route-table/{resource_id}` | TransitGatewayRouteTableId | `^tgw-rtb-[0-9a-f]{17}$` |  | AWS::EC2::TransitGatewayRouteTable | aws_ec2_transit_gateway_route_table |
| ec2 | volume | `arn:{partition}:ec2:{region}:{account}:volume/{resource_id}` | VolumeId | `^vol-[a-f0-9]{8}|vol-[a-f0-9]{17}$` | AwsEc2Volume | AWS::EC2::Volume | aws_ebs_volume |
| ec2 | vpc | `arn:{partition}:ec2:{region}:{account}:vpc/{resource_id}` | VpcId | `^vpc-[0-9a-f]{8,17}$` | AwsEc2Vpc | AWS::EC2::VPC | aws_vpc |
| ec2 | vpc_endpoint | `arn:{partition}:ec2:{region}:{account}:vpc-endpoint/{resource_id}` | VpcEndpointId | `^vpce-[a-z0-9]{8,}$` |  | AWS::EC2::VPCEndpoint | aws_vpc_endpoint |
| ec2 | vpc_endpoint_service | `arn:{partition}:ec2:{region}:{account}:vpc-endpoint-service/{resource_id}` | VpcEndpointServiceId | `^vpce-svc-[0-9a-f]{8,}$` | AwsEc2VpcEndpointService | AWS::EC2::VPCEndpointService | aws_vpc_endpoint_service |
| ec2 | vpc_peering_connection | `arn:{partition}:ec2:{region}:{account}:vpc-peering-connection/{resource_id}` | VpcPeeringConnectionId | `^pcx-[a-z0-9]{8,17}$` | AwsEc2VpcPeeringConnection | AWS::EC2::VPCPeeringConnection | aws_vpc_peering_connection |
| ec2 | vpn_connection | `arn:{partition}:ec2:{region}:{account}:vpn-connection/{resource_id}` | VpnConnectionId | `^vpn-[a-f0-9]{8}$` | AwsEc2VpnConnection | AWS::EC2::VPNConnection | aws_vpn_connection |
| ec2 | vpn_gateway | `arn:{partition}:ec2:{region}:{account}:vpn-gateway/{resource_id}` | VpnGatewayId | `^vgw-[0-9a-f]{8}$` |  | AWS::EC2::VPNGateway | aws_vpn_gateway |
| ec2-instance-connect | connect | `arn:{partition}:ec2-instance-connect:{region}:{account}:connect/{resource_id}` | InstanceId | `([a-zA-Z0-9\-]+)` |  | AWS::EC2::Instance | aws_instance |
| ecr | repository | `arn:{partition}:ecr:{region}:{account}:repository/{resource_id}` | RepositoryName | `([a-zA-Z0-9-_]+)` | AwsEcrRepository | AWS::ECR::Repository | aws_ecr_repository |
| ecr | image | `arn:{partition}:ecr:{region}:{account}:image/{resource_id}` | ImageDigest | `([a-zA-Z0-9-_]+)` | AwsEcrContainerImage | AWS::ECR::Image | aws_ecr_lifecycle_policy |
| ecs | cluster | `arn:{partition}:ecs:{region}:{account}:cluster/{resource_id}` | ClusterName | `([a-zA-Z0-9-_.]+)` | AwsEcsCluster | AWS::ECS::Cluster | aws_ecs_cluster |
| ecs | task_definition | `arn:{partition}:ecs:{region}:{account}:task-definition/{resource_id}` | TaskDefinitionFamily | `([a-zA-Z0-9-_.]+)` | AwsEcsTaskDefinition | AWS::ECS::TaskDefinition | aws_ecs_task_definition |
| ecs | task | `arn:{partition}:ecs:{region}:{account}:task/{resource_id}` | TaskId | `([a-zA-Z0-9-_.]+)` | AwsEcsTask | AWS::ECS::Task | aws_ecs_task |
| ecs | service | `arn:{partition}:ecs:{region}:{account}:service/{cluster_name}/{resource_id}` | ServiceName | `([a-zA-Z0-9-_.]+)` | AwsEcsService | AWS::ECS::Service | aws_ecs_service |
| ecs | container_instance | `arn:{partition}:ecs:{region}:{account}:container-instance/{resource_id}` | ContainerInstanceId | `([a-zA-Z0-9-_.]+)` | AwsEcsContainer | AWS::ECS::ContainerInstance | aws_ecs_container_instance |
| efs | file_system | `arn:{partition}:elasticfilesystem:{region}:{account}:file-system/{resource_id}` | FileSystemId | `fs-[a-zA-Z0-9]{8}` |  | AWS::EFS::FileSystem | aws_efs_file_system |
| efs | access_point | `arn:{partition}:elasticfilesystem:{region}:{account}:access-point/{resource_id}` | AccessPointId | `fsap-[a-zA-Z0-9]{8}` | AwsEfsAccessPoint | AWS::EFS::AccessPoint | aws_efs_access_point |
| eks | cluster | `arn:{partition}:eks:{region}:{account}:cluster/{resource_id}` | ClusterName | `([a-zA-Z0-9._-]+)` | AwsEksCluster | AWS::EKS::Cluster | aws_eks_cluster |
| elastic-inference | accelerator_type | `arn:{partition}:elastic-inference:{region}:{account}:accelerator-type/{resource_id}` | AcceleratorTypeName | `([a-zA-Z0-9-_.]+)` |  | AWS::ElasticInference::AcceleratorType | aws_ei_accelerator_type |
| elasticache | cache_cluster | `arn:{partition}:elasticache:{region}:{account}:cluster:{resource_id}` | CacheClusterId | `([a-zA-Z0-9-]+)` |  | AWS::ElastiCache::CacheCluster | aws_elasticache_cluster |
| elasticache | cache_parameter_group | `arn:{partition}:elasticache:{region}:{account}:parameter-group:{resource_id}` | CacheParameterGroupName | `([a-zA-Z0-9-]+)` |  | AWS::ElastiCache::CacheParameterGroup | aws_elasticache_parameter_group |
| elasticache | cache_security_group | `arn:{partition}:elasticache:{region}:{account}:security-group:{resource_id}` | CacheSecurityGroupName | `([a-zA-Z0-9-]+)` |  | AWS::ElastiCache::SecurityGroup | aws_elasticache_security_group |
| elasticache | cache_subnet_group | `arn:{partition}:elasticache:{region}:{account}:subnet-group:{resource_id}` | CacheSubnetGroupName | `([a-zA-Z0-9-]+)` |  | AWS::ElastiCache::SubnetGroup | aws_elasticache_subnet_group |
| elasticache | global_replication_group | `arn:{partition}:elasticache:{region}:{account}:global-replication-group:{resource_id}` | GlobalReplicationGroupId | `([a-zA-Z0-9-]+)` |  | AWS::ElastiCache::GlobalReplicationGroup | aws_elasticache_global_replication_group |
| elasticache | replication_group | `arn:{partition}:elasticache:{region}:{account}:cluster:{resource_id}` | ReplicationGroupId | `([a-zA-Z0-9-]+)` |  | AWS::ElastiCache::ReplicationGroup | aws_elasticache_replication_group |
| elasticache | user_group | `arn:{partition}:elasticache:{region}:{account}:user-group:{resource_id}` | UserGroupId | `([a-zA-Z0-9-]+)` |  | AWS::ElastiCache::UserGroup | aws_elasticache_user_group |
| elasticbeanstalk | application | `arn:{partition}:elasticbeanstalk:{region}:{account}:application/{resource_id}` | ApplicationName | `([a-zA-Z0-9-_.]+)` |  | AWS::ElasticBeanstalk::Application | aws_elastic_beanstalk_application |
| elasticbeanstalk | application_version | `arn:{partition}:elasticbeanstalk:{region}:{account}:applicationversion/{resource_id}` | ApplicationVersionName | `([a-zA-Z0-9-_.]+)` |  | AWS::ElasticBeanstalk::ApplicationVersion | aws_elastic_beanstalk_application_version |
| elasticbeanstalk | environment | `arn:{partition}:elasticbeanstalk:{region}:{account}:environment/{resource_id}` | EnvironmentId | `([a-zA-Z0-9-_.]+)` | AwsElasticBeanstalkEnvironment | AWS::ElasticBeanstalk::Environment | aws_elastic_beanstalk_environment |
| elb | loadbalancer | `arn:{partition}:elasticloadbalancing:{region}:{account}:loadbalancer/{resource_id}` | LoadBalancerName | `[\w.-]{1,32}` | AwsElbLoadBalancer | AWS::ElasticLoadBalancing::LoadBalancer | aws_elb |
| elbv2 | app_loadbalancer | `arn:{partition}:elasticloadbalancing:{region}:{account}:loadbalancer/app/{resource_id}/{load_balancer_id}` | LoadBalancerName | `[\w.-]{1,32}` | AwsElbv2LoadBalancer | AWS::ElasticLoadBalancingV2::LoadBalancer | aws_alb |
| elbv2 | net_loadbalancer | `arn:{partition}:elasticloadbalancing:{region}:{account}:loadbalancer/net/{resource_id}/{load_balancer_id}` | LoadBalancerName | `[\w.-]{1,32}` | AwsElbv2LoadBalancer | AWS::ElasticLoadBalancingV2::LoadBalancer | aws_alb |
| elbv2 | targetgroup | `arn:{partition}:elasticloadbalancing:{region}:{account}:targetgroup/{resource_id}/{targetgroup_id}` | TargetGroupID | `[\w.-]{1,32}` |  | AWS::ElasticLoadBalancingV2::TargetGroup | aws_alb_target_group |
| elbv2 | listener | `arn:{partition}:elasticloadbalancing:{region}:{account}:listener/{resource_id}/{load_balancer_id}/{listener_id}` | ListenerId | `(?<=listener\/app\/)[^\/]+` |  | AWS::ElasticLoadBalancingV2::Listener | aws_alb_listener |
| elbv2 | listener_rule | `arn:{partition}:elasticloadbalancing:{region}:{account}:listener-rule/{resource_id}` | ListenerRuleId | `[\w.-]{1,32}` |  | AWS::ElasticLoadBalancingV2::ListenerRule | aws_alb_listener_rule |
| elasticmapreduce | cluster | `arn:{partition}:elasticmapreduce:{region}:{account}:cluster/{resource_id}` | ClusterId | `j-[0-9a-zA-Z]+` |  | AWS::EMR::Cluster | aws_emr_cluster |
| elasticmapreduce | security_configuration | `arn:{partition}:elasticmapreduce:{region}:{account}:security-configuration/{resource_id}` | SecurityConfigurationName | `[a-zA-Z0-9_.\-]+` |  | AWS::EMR::SecurityConfiguration | aws_emr_security_configuration |
| elasticmapreduce | step | `arn:{partition}:elasticmapreduce:{region}:{account}:cluster/{resource_id}/step/{step_id}` | StepId | `s-[0-9a-zA-Z]+` |  | AWS::EMR::Step | aws_emr_step |
| elastictranscoder | pipeline | `arn:{partition}:elastictranscoder:{region}:{account}:pipeline/{resource_id}` | PipelineId | `[0-9a-zA-Z-_]{1,255}` |  | AWS::ElasticTranscoder::Pipeline | aws_elastictranscoder_pipeline |
| elastictranscoder | preset | `arn:{partition}:elastictranscoder:{region}:{account}:preset/{resource_id}` | PresetId | `[0-9a-zA-Z-_]{1,255}` |  | AWS::ElasticTranscoder::Preset | aws_elastictranscoder_preset |
| es | domain | `arn:{partition}:es:{region}:{account}:domain/{resource_id}` | DomainName | `[a-z0-9][a-z0-9-]{2,28}[a-z0-9]` | AwsElasticsearchDomain | AWS::Elasticsearch::Domain | aws_elasticsearch_domain |
| events | archive | `arn:{partition}:events:{region}:{account}:archive/{resource_id}` | ArchiveName | `[0-9a-zA-Z_.:-]+` |  | AWS::Events::Archive | aws_cloudwatch_event_archive |
| events | bus | `arn:{partition}:events:{region}:{account}:event-bus/{resource_id}` | EventBusName | `[0-9a-zA-Z_]+` |  | AWS::Events::EventBus | aws_cloudwatch_event_bus |
| events | rule | `arn:{partition}:events:{region}:{account}:rule/{resource_id}` | RuleName | `[0-9a-zA-Z_]+` |  | AWS::Events::Rule | aws_cloudwatch_event_rule |
| firehose | delivery_stream | `arn:{partition}:firehose:{region}:{account}:deliverystream/{resource_id}` | DeliveryStreamName | `[a-zA-Z0-9_-]+` |  | AWS::KinesisFirehose::DeliveryStream | aws_kinesis_firehose_delivery_stream |
| fms | policy | `arn:{partition}:fms:{region}:{account}:policy/{resource_id}` | PolicyName | `[\w-]+` |  | AWS::FMS::Policy | aws_fms_policy |
| fsx | backup | `arn:{partition}:fsx:{region}:{account}:backup/{resource_id}` | BackupId | `backup-[0-9a-f]+` |  | AWS::FSx::Backup | aws_fsx_backup |
| fsx | file_system | `arn:{partition}:fsx:{region}:{account}:file-system/{resource_id}` | FileSystemId | `fs-[0-9a-f]+` |  | AWS::FSx::FileSystem | aws_fsx_lustre_file_system |
| gamelift | alias | `arn:{partition}:gamelift:{region}:{account}:alias/{resource_id}` | AliasId | `^[a-zA-Z0-9-]{1,128}$` |  | AWS::GameLift::Alias | aws_gamelift_alias |
| gamelift | build | `arn:{partition}:gamelift:{region}:{account}:build/{resource_id}` | BuildId | `^build-[a-z0-9]{14}$` |  | AWS::GameLift::Build | aws_gamelift_build |
| gamelift | fleet | `arn:{partition}:gamelift:{region}:{account}:fleet/{resource_id}` | FleetId | `^fleet-[a-z0-9]{14}$` |  | AWS::GameLift::Fleet | aws_gamelift_fleet |
| glacier | vault | `arn:{partition}:glacier:{region}:{account}:vaults/{resource_id}` | VaultName | `^[a-zA-Z0-9][a-zA-Z0-9-]{0,254}$` |  | AWS::Glacier::Vault | aws_glacier_vault |
| globalaccelerator | accelerator | `arn:{partition}:globalaccelerator::{account}:accelerator/{resource_id}` | AcceleratorId | `[a-z0-9]{16}` |  | AWS::GlobalAccelerator::Accelerator | aws_globalaccelerator_accelerator |
| globalaccelerator | listener | `arn:{partition}:globalaccelerator::{account}:listener/{resource_id}` | ListenerId | `[a-z0-9]{16}` |  | AWS::GlobalAccelerator::Listener | aws_globalaccelerator_listener |
| globalaccelerator | endpoint_group | `arn:{partition}:globalaccelerator::{account}:endpoint-group/{resource_id}` | EndpointGroupId | `[a-z0-9]{16}` |  | AWS::GlobalAccelerator::EndpointGroup | aws_globalaccelerator_endpoint_group |
| glue | catalog | `arn:{partition}:glue:{region}:{account}:catalog` | None | `None` |  | AWS::Glue::Catalog | aws_glue_catalog_database |
| glue | crawler | `arn:{partition}:glue:{region}:{account}:crawler:{resource_name}` | CrawlerName | `[-0-9a-zA-Z]+` |  | AWS::Glue::Crawler | aws_glue_crawler |
| glue | database | `arn:{partition}:glue:{region}:{account}:database/{resource_id}` | DatabaseName | `[-0-9a-zA-Z]+` |  | AWS::Glue::Database | aws_glue_catalog_database |
| glue | dev_endpoint | `arn:{partition}:glue:{region}:{account}:devEndpoint/{resource_id}` | DevEndpointName | `[-0-9a-zA-Z]+` |  | AWS::Glue::DevEndpoint | aws_glue_dev_endpoint |
| glue | job | `arn:{partition}:glue:{region}:{account}:job/{resource_id}` | JobName | `[-0-9a-zA-Z]+` |  | AWS::Glue::Job | aws_glue_job |
| glue | partition | `arn:{partition}:glue:{region}:{account}:table/{database_name}/{resource_id}/partition/{PartitionValues}` | None | `None` |  | AWS::Glue::Partition | aws_glue_catalog_partition |
| glue | trigger | `arn:{partition}:glue:{region}:{account}:trigger/{resource_id}` | TriggerName | `[-0-9a-zA-Z]+` |  | AWS::Glue::Trigger | aws_glue_trigger |
| glue | workflow | `arn:{partition}:glue:{region}:{account}:workflow/{resource_id}` | WorkflowName | `[-0-9a-zA-Z]+` |  | AWS::Glue::Workflow | aws_glue_workflow |
| greengrass | group | `arn:{partition}:greengrass:{region}:{account}:/greengrass/groups/{resource_id}` | GroupId | `^[a-zA-Z0-9-_]{1,128}$` |  | AWS::Greengrass::Group | aws_greengrass_group |
| guardduty | detector | `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}` | DetectorId | `^[0-9a-f]{8,}-[0-9a-f]{4,}-[0-9a-f]{4,}-[0-9a-f]{4,}-[0-9a-f]{12,}$` |  | AWS::GuardDuty::Detector | aws_guardduty_detector |
| guardduty | filter | `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/filter/{subresource_id}` | FilterName | `^[a-zA-Z0-9-_]{1,64}$` |  | AWS::GuardDuty::Filter | aws_guardduty_filter |
| guardduty | ipset | `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/ipset/{subresource_id}` | IpSetId | `^[a-zA-Z0-9-_]{1,64}$` |  | AWS::GuardDuty::IPSet | aws_guardduty_ipset |
| guardduty | member | `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/member/{subresource_id}` | MemberId | `^[0-9a-zA-Z-_]{1,64}$` |  | AWS::GuardDuty::Member | aws_guardduty_member |
| guardduty | threatintelset | `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/threatintelset/{subresource_id}` | ThreatIntelSetId | `^[a-zA-Z0-9-_]{1,64}$` |  | AWS::GuardDuty::ThreatIntelSet | aws_guardduty_threatintelset |
| health | event | `arn:{partition}:health:{region}:{account}:event/{resource_id}` | EventArn | `arn:[^:]+:health:[^:]+:[^:]+:event\/[0-9a-f-]+` |  | AWS::Health::Event | aws_health_event |
| health | health_check | `arn:{partition}:health:{region}:{account}:healthcheck/{resource_id}` | HealthCheckId | `[0-9a-f-]{8}` |  | AWS::Health::HealthCheck | aws_health_check |
| health | organization_event_detail | `arn:{partition}:health:{region}:{account}:event-organization/{event_type_code}/{service}/{event_type_version}/{event_id}` | EventArn | `arn:[^:]+:health:[^:]+:[^:]+:event\/[0-9a-f-]+` |  | AWS::Health::OrganizationEventDetail | aws_health_organization_event_detail |
| health | service | `arn:{partition}:health:{region}:{account}:service/{resource_id}` | Service | `[a-zA-Z0-9_-]{1,64}` |  | AWS::Health::Service | aws_health_service |
| iam | access_key | `arn:{partition}:iam::{account}:accesskey/{resource_id}` | AccessKeyId | `^[A-Z0-9]{16}$` | AwsIamAccessKey | AWS::IAM::AccessKey | aws_iam_access_key |
| iam | account_alias | `arn:{partition}:iam::{account}:alias/{resource_id}` | AccountAlias | `^[a-z0-9][a-z0-9.-]{0,62}$` |  | AWS::IAM::AccountAlias | aws_iam_account_alias |
| iam | group | `arn:{partition}:iam::{account}:group/{resource_id}` | GroupName | `^[a-zA-Z0-9+=,.@_-]{1,128}$` | AwsIamGroup | AWS::IAM::Group | aws_iam_group |
| iam | instance_profile | `arn:{partition}:iam::{account}:instance-profile/{resource_id}` | InstanceProfileName | `^[a-zA-Z0-9_/+=.@-]{1,128}$` |  | AWS::IAM::InstanceProfile | aws_iam_instance_profile |
| iam | policy | `arn:{partition}:iam::{account}:policy/{resource_id}` | PolicyName | `^[a-zA-Z0-9+=,.@-_]{1,128}$` | AwsIamPolicy | AWS::IAM::Policy | aws_iam_policy |
| iam | role | `arn:{partition}:iam::{account}:role/{resource_id}` | RoleName | `^[a-zA-Z_][a-zA-Z0-9_=@,.+-]{1,63}$` | AwsIamRole | AWS::IAM::Role | aws_iam_role |
| iam | server_certificate | `arn:{partition}:iam::{account}:server-certificate/{resource_id}` | ServerCertificateName | `^[a-zA-Z0-9_/+=.@-]{1,128}$` |  | AWS::IAM::ServerCertificate | aws_iam_server_certificate |
| iam | user | `arn:{partition}:iam::{account}:user/{resource_id}` | UserName | `^[a-zA-Z0-9_+=,.@-]{1,128}$` | AwsIamUser | AWS::IAM::User | aws_iam_user |
| iam | virtual_mfa_device | `arn:{partition}:iam::{account}:mfa/{resource_id}` | VirtualMFADeviceName | `^[\w+=,.@-]{1,64}$` |  | AWS::IAM::VirtualMFADevice | aws_iam_virtual_mfa_device |
| iam | group_policy | `arn:{partition}:iam::{account}:group/{group_id}/policy/{resource_id}` | PolicyName | `^[\w+=,.@-]{1,128}$` |  | AWS::IAM::Policy | aws_iam_group_policy_attachment |
| iam | role_policy | `arn:{partition}:iam::{account}:role/{role_id}/policy/{resource_id}` | PolicyName | `^[\w+=,.@-]{1,128}$` |  | AWS::IAM::Policy | aws_iam_role_policy_attachment |
| iam | user_policy | `arn:{partition}:iam::{account}:user/{user_id}/policy/{resource_id}` | PolicyName | `^[\w+=,.@-]{1,128}$` |  | AWS::IAM::Policy | aws_iam_user_policy_attachment |
| imagebuilder | component | `arn:{partition}:imagebuilder:{region}:{account}:component/{resource_id}` | ComponentBuildVersionArn | `^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:component/.$` |  | AWS::ImageBuilder::Component | aws_imagebuilder_component |
| imagebuilder | distribution_configuration | `arn:{partition}:imagebuilder:{region}:{account}:distribution-configuration/{resource_id}` | DistributionConfigurationArn | `^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:distribution-configuration/.$` |  | AWS::ImageBuilder::DistributionConfiguration | aws_imagebuilder_distribution_configuration |
| imagebuilder | image | `arn:{partition}:imagebuilder:{region}:{account}:image/{resource_id}` | ImageBuildVersionArn | `^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:image/.$` |  | AWS::ImageBuilder::Image | aws_imagebuilder_image |
| imagebuilder | image_pipeline | `arn:{partition}:imagebuilder:{region}:{account}:image-pipeline/{resource_id}` | ImagePipelineArn | `^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:image-pipeline/.$` |  | AWS::ImageBuilder::ImagePipeline | aws_imagebuilder_image_pipeline |
| imagebuilder | infrastructure_configuration | `arn:{partition}:imagebuilder:{region}:{account}:infrastructure-configuration/{resource_id}` | InfrastructureConfigurationArn | `^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:infrastructure-configuration/.$` |  | AWS::ImageBuilder::InfrastructureConfiguration | aws_imagebuilder_infrastructure_configuration |
| inspector | assessment_target | `arn:{partition}:inspector:{region}:{account}:target/{resource_id}` | AssessmentTargetArn | `^arn:aws:inspector:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:target/[a-zA-Z0-9_-]{36}$` |  | AWS::Inspector::AssessmentTarget | aws_inspector_assessment_target |
| inspector | assessment_template | `arn:{partition}:inspector:{region}:{account}:template/{resource_id}` | AssessmentTemplateArn | `^arn:aws:inspector:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:template/[a-zA-Z0-9_-]{36}$` |  | AWS::Inspector::AssessmentTemplate | aws_inspector_assessment_template |
| inspector | assessment_run | `arn:{partition}:inspector:{region}:{account}:run/{resource_id}` | AssessmentRunArn | `^arn:aws:inspector:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:run/[a-zA-Z0-9_-]{36}$` |  | AWS::Inspector::AssessmentRun | aws_inspector_assessment_run |
| iot | authorizer | `arn:{partition}:iot:{region}:{account}:authorizer/{resource_id}` | AuthorizerName | `^([a-zA-Z0-9:_-]){1,128}$` |  | AWS::IoT::Authorizer | aws_iot_authorizer |
| iot | billing_group | `arn:{partition}:iot:{region}:{account}:billinggroup/{resource_id}` | BillingGroupName | `^([a-zA-Z0-9:_-]){1,128}$` |  | AWS::IoT::BillingGroup | aws_iot_billing_group |
| iot | certificate | `arn:{partition}:iot:{region}:{account}:cert/{resource_id}` | CertificateId | `^([a-f0-9]){64}$` |  | AWS::IoT::Certificate | aws_iot_certificate |
| iot | dimension | `arn:{partition}:iot:{region}:{account}:dimension/{resource_id}` | DimensionName | `^([a-zA-Z0-9:_-]){1,128}$` |  | AWS::IoT::Dimension | aws_iot_dimension |
| iot | policy | `arn:{partition}:iot:{region}:{account}:policy/{resource_id}` | PolicyName | `^([a-zA-Z0-9:_-]){1,128}$` |  | AWS::IoT::Policy | aws_iot_policy |
| iot | provisioning_template | `arn:{partition}:iot:{region}:{account}:provisioningtemplate/{resource_id}` | TemplateName | `^([a-zA-Z0-9:_-]){1,128}$` |  | AWS::IoT::ProvisioningTemplate | aws_iot_provisioning_template |
| iot | rule | `arn:{partition}:iot:{region}:{account}:rule/{resource_id}` | RuleName | `^([a-zA-Z0-9:_-]){1,128}$` |  | AWS::IoT::TopicRule | aws_iot_topic_rule |
| iot | scheduled_audit | `arn:{partition}:iot:{region}:{account}:scheduledaudit/{resource_id}` | ScheduledAuditName | `^([a-zA-Z0-9:_-]){1,128}$` |  | AWS::IoT::ScheduledAudit | aws_iot_scheduled_audit |
| iot | thing | `arn:{partition}:iot:{region}:{account}:thing/{resource_id}` | ThingName | `^[a-zA-Z0-9_-]+$` |  | AWS::IoT::Thing | aws_iot_thing |
| iot | thing_group | `arn:{partition}:iot:{region}:{account}:thinggroup/{resource_id}` | ThingGroupName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT::ThingGroup | aws_iot_thing_group |
| iot | thing_type | `arn:{partition}:iot:{region}:{account}:thingtype/{resource_id}` | ThingTypeName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT::ThingType | aws_iot_thing_type |
| iot | topic_rule_destination | `arn:{partition}:iot:{region}:{account}:topic-rule-destination/{resource_id}` | TopicRuleDestinationName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT::TopicRuleDestination | aws_iot_topic_rule_destination |
| iot | topic_rule | `arn:{partition}:iot:{region}:{account}:rule/{resource_id}` | RuleName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT::TopicRule | aws_iot_topic_rule |
| iot | domain_configuration | `arn:{partition}:iot:{region}:{account}:domainconfiguration/{resource_id}` | DomainConfigurationName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT::DomainConfiguration | aws_iot_domain_configuration |
| iot | fleet_indexing_configuration | `arn:{partition}:iot:{region}:{account}:fleet-indexing-configuration/{resource_id}` | IndexingConfigurationName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT::FleetIndexingConfiguration | aws_iot_fleet_indexing_configuration |
| iot | job | `arn:{partition}:iot:{region}:{account}:job/{resource_id}` | JobId | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT::Job | aws_iot_job |
| iot-device-tester | test_suite_run | `arn:{partition}:iot-device-tester:{region}:{account}:test-suite-run:{SuiteDefinitionId}/{resource_id}` | SuiteRunId | `^[a-zA-Z0-9-_]{1,128}$` |  | AWS::IoTDeviceTester::TestSuiteRun | aws_iot_device_tester_test_suite_run |
| iot1click-projects | device | `arn:{partition}:iot1click:{region}:{account}:device/{resource_id}` | DeviceId | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT1Click::Device | aws_iot1click_device |
| iot1click-projects | placement | `arn:{partition}:iot1click:{region}:{account}:placement/{resource_id}` | PlacementName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT1Click::Placement | aws_iot1click_placement |
| iot1click-projects | project | `arn:{partition}:iot1click:{region}:{account}:project/{resource_id}` | ProjectName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoT1Click::Project | aws_iot1click_project |
| iotanalytics | channel | `arn:{partition}:iotanalytics:{region}:{account}:channel/{resource_id}` | ChannelName | `^[a-zA-Z0-9_]+$` |  | AWS::IoTAnalytics::Channel | aws_iot_analytics_channel |
| iotanalytics | dataset | `arn:{partition}:iotanalytics:{region}:{account}:dataset/{resource_id}` | DatasetName | `^[a-zA-Z0-9_]+$` |  | AWS::IoTAnalytics::Dataset | aws_iot_analytics_dataset |
| iotanalytics | datastore | `arn:{partition}:iotanalytics:{region}:{account}:datastore/{resource_id}` | DatastoreName | `^[a-zA-Z0-9_]+$` |  | AWS::IoTAnalytics::Datastore | aws_iot_analytics_datastore |
| iotanalytics | pipeline | `arn:{partition}:iotanalytics:{region}:{account}:pipeline/{resource_id}` | PipelineName | `^[a-zA-Z0-9_]+$` |  | AWS::IoTAnalytics::Pipeline | aws_iot_analytics_pipeline |
| iotevents | input | `arn:{partition}:iotevents:{region}:{account}:input/{resource_id}` | InputName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoTEvents::Input | aws_iot_events_input |
| iotevents | detector_model | `arn:{partition}:iotevents:{region}:{account}:detector-model/{resource_id}` | DetectorModelName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoTEvents::DetectorModel | aws_iot_events_detector_model |
| iotsitewise | asset_model | `arn:{partition}:iotsitewise:{region}:{account}:asset-model/{resource_id}` | AssetModelId | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoTSiteWise::AssetModel | aws_iotsitewise_asset_model |
| iotsitewise | gateway | `arn:{partition}:iotsitewise:{region}:{account}:gateway/{resource_id}` | GatewayId | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::IoTSiteWise::Gateway | aws_iotsitewise_gateway |
| kafka | cluster | `arn:{partition}:kafka:{region}:{account}:cluster/{resource_id}` | ClusterName | `^[a-zA-Z0-9_-]{1,64}$` |  | AWS::MSK::Cluster | aws_msk_cluster |
| kinesis | stream | `arn:{partition}:kinesis:{region}:{account}:stream/{resource_id}` | StreamName | `^[a-zA-Z0-9_.-]{1,128}$` | AwsKinesisStream | AWS::Kinesis::Stream | aws_kinesis_stream |
| kinesis | firehose_delivery_stream | `arn:{partition}:firehose:{region}:{account}:deliverystream/{resource_id}` | DeliveryStreamName | `^[a-zA-Z0-9_.-]{1,64}$` |  | AWS::Firehose::DeliveryStream | aws_kinesis_firehose_delivery_stream |
| kinesis-video-archived-media | archive | `arn:{partition}:kinesisvideo:{region}:{account}:archive/{stream_id}/{resource_id}` | ArchiveId | `^[a-zA-Z0-9_.-]{1,128}$` |  | AWS::KinesisVideo::Stream/Archive | aws_kinesis_video_archive |
| kinesis-video-archived-media | stream | `arn:{partition}:kinesisvideo:{region}:{account}:stream/{stream_id}/{resource_id}` | StreamARN | `^arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:stream/[a-zA-Z0-9_.-]{1,256}/[0-9]+/[0-9]+$` |  | AWS::KinesisVideo::Stream | aws_kinesis_video_stream |
| kinesis-video-media | stream | `arn:{partition}:kinesisvideo:{region}:{account}:stream/{stream_id}/{resource_id}` | StreamARN | `^arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:stream/[a-zA-Z0-9_.-]{1,256}/[0-9]+/[0-9]+$` |  | AWS::KinesisVideo::Stream | aws_kinesis_video_stream |
| kinesis-video-signaling | channel | `arn:{partition}:kinesisvideo:{region}:{account}:channel/{channel_name}/{resource_id}` | ChannelARN | `^arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9_.-]{1,256}/[0-9]+/[0-9]+$` |  | AWS::KinesisVideo::Channel | aws_kinesis_video_channel |
| kms | key | `arn:{partition}:kms:{region}:{account}:key/{resource_id}` | KeyId | `^[a-zA-Z0-9-_]{1,64}$` | AwsKmsKey | AWS::KMS::Key | aws_kms_key |
| kms | alias | `arn:{partition}:kms:{region}:{account}:alias/{resource_id}` | AliasName | `^alias/[a-zA-Z0-9:/_-]{1,256}$` |  | AWS::KMS::Alias | aws_kms_alias |
| lakeformation | data_lake_settings | `arn:{partition}:lakeformation:{region}:{account}:datalake/{resource_id}/settings` | DataLakeId | `^[a-zA-Z0-9-]{1,255}$` |  | AWS::LakeFormation::DataLakeSettings | aws_lakeformation_data_lake_settings |
| lakeformation | permissions | `arn:{partition}:lakeformation:{region}:{account}:permissions/{resource_id}` | ResourceId | `^[a-zA-Z0-9-]{1,255}$` |  | AWS::LakeFormation::Permissions | aws_lakeformation_permissions |
| lambda | function | `arn:{partition}:lambda:{region}:{account}:function:{resource_id}` | FunctionName | `^[a-zA-Z0-9-_]{1,140}$` | AwsLambdaFunction | AWS::Lambda::Function | aws_lambda_function |
| lambda | layer | `arn:{partition}:lambda:{region}:{account}:layer:{resource_id}` | LayerName | `^[a-zA-Z0-9-_]{1,140}$` | AwsLambdaLayerVersion | AWS::Lambda::LayerVersion | aws_lambda_layer_version |
| lambda | event_source_mapping | `arn:{partition}:lambda:{region}:{account}:event-source-mapping:{resource_id}` | UUID | `^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$` |  | AWS::Lambda::EventSourceMapping | aws_lambda_event_source_mapping |
| lambda | event_invoke_config | `arn:{partition}:lambda:{region}:{account}:event-invoke-config:{resource_id}` | UUID | `^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$` |  | AWS::Lambda::EventInvokeConfig | aws_lambda_event_invoke_config |
| lex | bot | `arn:{partition}:lex:{region}:{account}:bot:{resource_id}` | BotName | `^[a-zA-Z0-9_-]{1,50}$` |  | AWS::Lex::Bot | aws_lex_bot |
| lex | bot_alias | `arn:{partition}:lex:{region}:{account}:bot:{BotName}:alias:{resource_id}` | BotAlias | `^[a-zA-Z0-9_-]{1,50}$` |  | AWS::Lex::BotAlias | aws_lex_bot_alias |
| lex | bot_channel | `arn:{partition}:lex:{region}:{account}:bot-channel:{BotName}:{BotAlias}:{ChannelName}` | ChannelName | `^[a-zA-Z0-9_-]{1,50}$` |  | AWS::Lex::BotChannel | aws_lex_bot_channel |
| license-manager | license_configuration | `arn:{partition}:license-manager:{region}:{account}:license-configuration/{resource_id}` | LicenseConfigurationId | `^[a-zA-Z0-9_-]{1,100}$` |  | AWS::LicenseManager::LicenseConfiguration | aws_licensemanager_license_configuration |
| lightsail | instance | `arn:{partition}:lightsail:{region}:{account}:instance/{resource_id}` | InstanceName | `^[a-zA-Z0-9-]{1,64}$` |  | AWS::Lightsail::Instance | aws_lightsail_instance |
| lightsail | key_pair | `arn:{partition}:lightsail:{region}:{account}:key-pair/{resource_id}` | KeyName | `^[a-zA-Z0-9-]{1,64}$` |  | AWS::Lightsail::KeyPair | aws_lightsail_key_pair |
| lightsail | static_ip | `arn:{partition}:lightsail:{region}:{account}:static-ip/{resource_id}` | StaticIpName | `^[a-zA-Z0-9-]{1,64}$` |  | AWS::Lightsail::StaticIp | aws_lightsail_static_ip |
| lightsail | load_balancer | `arn:{partition}:lightsail:{region}:{account}:loadbalancer/{resource_id}` | LoadBalancerName | `^[a-zA-Z0-9-]{1,64}$` |  | AWS::Lightsail::LoadBalancer | aws_lightsail_load_balancer |
| lightsail | bucket | `arn:{partition}:lightsail:{region}:{account}:bucket/{resource_id}` | BucketName | `^[a-zA-Z0-9-]{1,64}$` |  | AWS::Lightsail::Bucket | aws_lightsail_bucket |
| logs | log_group | `arn:{partition}:logs:{region}:{account}:log-group:{resource_id}` | LogGroupName | `^[a-zA-Z0-9._/-]{1,512}$` |  | AWS::Logs::LogGroup | aws_cloudwatch_log_group |
| logs | log_stream | `arn:{partition}:logs:{region}:{account}:log-group:{LogGroupName}:log-stream:{resource_id}` | LogStreamName | `^[^:*]*$` |  | AWS::Logs::LogStream | aws_cloudwatch_log_stream |
| logs | metric_filter | `arn:{partition}:logs:{region}:{account}:metric-filter:{resource_id}` | MetricFilterName | `^[a-zA-Z0-9._/-]{1,512}$` |  | AWS::Logs::MetricFilter | aws_cloudwatch_log_metric_filter |
| logs | destination | `arn:{partition}:logs:{region}:{account}:destination:{resource_id}` | DestinationName | `^[a-zA-Z0-9._/-]{1,512}$` |  | AWS::Logs::Destination | aws_cloudwatch_log_destination |
| logs | query_definition | `arn:{partition}:logs:{region}:{account}:query-definition:{resource_id}` | QueryDefinitionName | `^[a-zA-Z0-9._/-]{1,512}$` |  | AWS::Logs::QueryDefinition | aws_cloudwatch_log_query_definition |
| machinelearning | batch_prediction | `arn:{partition}:machinelearning:{region}:{account}:batchprediction/{resource_id}` | BatchPredictionId | `^[a-zA-Z0-9_.-]{1,64}$` |  | AWS::MachineLearning::BatchPrediction | aws_machine_learning_batch_prediction |
| machinelearning | data_source | `arn:{partition}:machinelearning:{region}:{account}:datasource/{resource_id}` | DataSourceId | `^[a-zA-Z0-9_.-]{1,64}$` |  | AWS::MachineLearning::DataSource | aws_machine_learning_data_source |
| machinelearning | evaluation | `arn:{partition}:machinelearning:{region}:{account}:evaluation/{resource_id}` | EvaluationId | `^[a-zA-Z0-9_.-]{1,64}$` |  | AWS::MachineLearning::Evaluation | aws_machine_learning_evaluation |
| machinelearning | ml_model | `arn:{partition}:machinelearning:{region}:{account}:mlmodel/{resource_id}` | MLModelId | `^[a-zA-Z0-9_.-]{1,64}$` |  | AWS::MachineLearning::MLModel | aws_machine_learning_model |
| macie | classification_job | `arn:{partition}:macie:{region}:{account}:classification-job/{resource_id}` | ClassificationJobId | `^[a-f0-9]{32}$` |  | AWS::Macie::ClassificationJob | aws_macie_classification_job |
| macie | custom_data_identifier | `arn:{partition}:macie:{region}:{account}:custom-data-identifier/{resource_id}` | CustomDataIdentifierId | `^[a-f0-9]{32}$` |  | AWS::Macie::CustomDataIdentifier | aws_macie_custom_data_identifier |
| macie | findings_filter | `arn:{partition}:macie:{region}:{account}:findings-filter/{resource_id}` | FindingsFilterId | `^[a-f0-9]{32}$` |  | AWS::Macie::FindingsFilter | aws_macie_findings_filter |
| macie | member_account | `arn:{partition}:macie:{region}:{account}:member-account/{resource_id}` | MemberAccountId | `^\d{12}$` |  | AWS::Macie::MemberAccount | aws_macie_member_account_association |
| macie | s3_object | `arn:{partition}:macie:{region}:{account}:s3-object/{resource_id}` | S3BucketName/S3ObjectKey | `^[^/]{1,255}/.*$` |  | AWS::Macie::S3Object | aws_macie_s3_bucket_association |
| managedblockchain | network | `arn:{partition}:managedblockchain:{region}:{account}:network/{resource_id}` | NetworkId | `^[a-zA-Z0-9]{1,32}$` |  | AWS::ManagedBlockchain::Network | aws_managed_blockchain_network |
| managedblockchain | node | `arn:{partition}:managedblockchain:{region}:{account}:node/{NetworkId}/{MemberId}/{resource_id}` | NodeId | `^[a-zA-Z0-9]{1,32}$` |  | AWS::ManagedBlockchain::Node | aws_managed_blockchain_node |
| managedblockchain | proposal | `arn:{partition}:managedblockchain:{region}:{account}:proposal/{NetworkId}/{resource_id}` | ProposalId | `^[a-zA-Z0-9]{1,32}$` |  | AWS::ManagedBlockchain::Proposal | aws_managed_blockchain_proposal |
| mediaconnect | flow | `arn:{partition}:mediaconnect:{region}:{account}:flow/{resource_id}` | FlowArn | `^arn:aws:mediaconnect:[^:]+:[^:]+:[0-9]+:[^/]+/[^/]+$` |  | AWS::MediaConnect::Flow | aws_media_connect_flow |
| mediaconvert | queue | `arn:{partition}:mediaconvert:{region}:{account}:queue/{resource_id}` | QueueName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::MediaConvert::Queue | aws_media_convert_queue |
| mediaconvert | preset | `arn:{partition}:mediaconvert:{region}:{account}:preset/{resource_id}` | PresetName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::MediaConvert::Preset | aws_media_convert_preset |
| mediaconvert | job_template | `arn:{partition}:mediaconvert:{region}:{account}:jobTemplate/{resource_id}` | JobTemplateName | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::MediaConvert::JobTemplate | aws_media_convert_job_template |
| medialive | channel | `arn:{partition}:medialive:{region}:{account}:channel:{resource_id}` | ChannelId | `^[a-zA-Z0-9-_]{1,64}$` |  | AWS::MediaLive::Channel | aws_media_live_channel |
| mediapackage | channel | `arn:{partition}:mediapackage:{region}:{account}:channel/{resource_id}` | ChannelId | `^[a-zA-Z0-9_-]{1,64}$` |  | AWS::MediaPackage::Channel | aws_media_package_channel |
| mediapackage | origin_endpoint | `arn:{partition}:mediapackage:{region}:{account}:origin_endpoint/{resource_id}` | OriginEndpointId | `^[a-zA-Z0-9_-]{1,64}$` |  | AWS::MediaPackage::OriginEndpoint | aws_media_package_origin_endpoint |
| mediastore | container | `arn:{partition}:mediastore:{region}:{account}:container/{resource_id}` | ContainerName | `^[a-zA-Z0-9_-]{1,255}$` |  | AWS::MediaStore::Container | aws_media_store_container |
| mediastore-data | object | `arn:{partition}:mediastore-data:{region}:{account}:object/{resource_id}` | Path | `^.{1,1024}$` |  | AWS::MediaStore::Object | aws_media_store_data_object |
| meteringmarketplace | product | `arn:{partition}:meteringmarketplace:{region}:{account}:product/{resource_id}` | ProductCode | `^[a-zA-Z0-9_.-]{1,255}$` |  | AWS::Marketplace::Product | aws_marketplace_catalog_product |
| meteringmarketplace | usage_record | `arn:{partition}:meteringmarketplace:{region}:{account}:usage-record:{resource_id}` | ProductCode | `^[a-zA-Z0-9_.-]{1,255}$` |  | AWS::Marketplace::UsageRecord | aws_marketplace_entitlement |
| mgh | home_region_control | `arn:{partition}:mgh:{region}:{account}:homeRegionControl/{resource_id}` | HomeRegionControlId | `^[a-zA-Z0-9_-]{1,64}$` |  | AWS::MGH::HomeRegionControl | aws_migration_hub_home_region_control |
| mgh | migration_task | `arn:{partition}:mgh:{region}:{account}:migrationTask/{resource_id}` | MigrationTaskName | `^[a-zA-Z0-9_-]{1,256}$` |  | AWS::MGH::MigrationTask | aws_migration_hub_migration_task |
| mgh | progress_update_stream | `arn:{partition}:mgh:{region}:{account}:progressUpdateStream/{resource_id}` | ProgressUpdateStreamName | `^[a-zA-Z0-9_-]{1,256}$` |  | AWS::MGH::ProgressUpdateStream | aws_migration_hub_progress_update_stream |
| mobilehub | project | `arn:{partition}:mobilehub:{region}:{account}:project/{resource_id}` | ProjectId | `^[a-zA-Z0-9_.:-]{1,32}$` |  | AWS::MobileHub::Project | aws_mobilehub_project |
| mq | broker | `arn:{partition}:mq:{region}:{account}:broker:{resource_id}` | BrokerId | `^[a-zA-Z0-9_-]{1,36}$` |  | AWS::AmazonMQ::Broker | aws_mq_broker |
| mq | configuration | `arn:{partition}:mq:{region}:{account}:configuration:{resource_id}` | ConfigurationId | `^[a-zA-Z0-9_-]{1,36}$` |  | AWS::AmazonMQ::Configuration | aws_mq_configuration |
| mturk | hit_type | `arn:{partition}:mturk:{region}:{account}:hittype/{resource_id}` | HITTypeId | `^[A-Z0-9A-Z]{10,}$` |  | AWS::MTurk::HITType | aws_mturk_hit_type |
| mturk | hit | `arn:{partition}:mturk:{region}:{account}:hit/{resource_id}` | HITId | `^[A-Z0-9A-Z]{30,}$` |  | AWS::MTurk::HIT | aws_mturk_hit |
| mturk | qualification_type | `arn:{partition}:mturk:{region}:{account}:qualificationtype/{resource_id}` | QualificationTypeId | `^[A-Z0-9A-Z]{10,}$` |  | AWS::MTurk::QualificationType | aws_mturk_qualification_type |
| neptune-db | cluster | `arn:{partition}:neptune-db:{region}:{account}:cluster:{resource_id}` | ClusterResourceId | `^neptune-[^:]*:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |  | AWS::Neptune::DBCluster | aws_neptune_cluster |
| network-firewall | firewall_policy | `arn:{partition}:network-firewall:{region}:{account}:policy/{resource_id}` | FirewallPolicyName | `^[a-zA-Z0-9-]{1,128}$` | AwsNetworkFirewallFirewallPolicy | AWS::NetworkFirewall::FirewallPolicy | aws_networkfirewall_firewall_policy |
| network-firewall | firewall | `arn:{partition}:network-firewall:{region}:{account}:firewall/{resource_id}` | FirewallName | `^[a-zA-Z0-9-]{1,128}$` | AwsNetworkFirewallFirewall | AWS::NetworkFirewall::Firewall | aws_networkfirewall_firewall |
| network-firewall | rule_group | `arn:{partition}:network-firewall:{region}:{account}:rulegroup/{resource_id}` | RuleGroupName | `^[a-zA-Z0-9-]{1,128}$` | AwsNetworkFirewallRuleGroup | AWS::NetworkFirewall::RuleGroup | aws_networkfirewall_rule_group |
| networkmanager | global_network | `arn:{partition}:networkmanager:{region}:{account}:global-network/{resource_id}` | GlobalNetworkId | `^[a-zA-Z0-9\-]{1,255}$` |  | AWS::NetworkManager::GlobalNetwork | aws_networkmanager_global_network |
| networkmanager | device | `arn:{partition}:networkmanager:{region}:{account}:device/{resource_id}` | DeviceId | `^[a-zA-Z0-9\-]{1,255}$` |  | AWS::NetworkManager::Device | aws_networkmanager_device |
| networkmanager | link | `arn:{partition}:networkmanager:{region}:{account}:link/{resource_id}` | LinkId | `^[a-zA-Z0-9\-]{1,255}$` |  | AWS::NetworkManager::Link | aws_networkmanager_link |
| networkmanager | site | `arn:{partition}:networkmanager:{region}:{account}:site/{resource_id}` | SiteId | `^[a-zA-Z0-9\-]{1,255}$` |  | AWS::NetworkManager::Site | aws_networkmanager_site |
| opensearch | domain | `arn:{partition}:opensearch:{region}:{account}:domain/{resource_id}` | DomainId | `^[a-zA-Z0-9][a-zA-Z0-9\-]{2,28}[a-zA-Z0-9]$` | AwsOpenSearchServiceDomain | AWS::OpenSearchService::Domain | aws_opensearch_service_domain |
| opsworks | stack | `arn:{partition}:opsworks:{region}:{account}:stack/{resource_id}` | StackId | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::OpsWorks::Stack | aws_opsworks_stack |
| opsworks | layer | `arn:{partition}:opsworks:{region}:{account}:layer/{resource_id}` | LayerId | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::OpsWorks::Layer | aws_opsworks_layer |
| opsworks | app | `arn:{partition}:opsworks:{region}:{account}:app/{resource_id}` | AppId | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::OpsWorks::App | aws_opsworks_app |
| opsworks | instance | `arn:{partition}:opsworks:{region}:{account}:instance/{resource_id}` | InstanceId | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::OpsWorks::Instance | aws_opsworks_instance |
| opsworks | user_profile | `arn:{partition}:opsworks:{region}:{account}:user-profile/{resource_id}` | UserProfileId | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::OpsWorks::UserProfile | aws_opsworks_user_profile |
| opsworks | permission | `arn:{partition}:opsworks:{region}:{account}:permission/{resource_id}` | PermissionId | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::OpsWorks::Permission | aws_opsworks_permission |
| opsworks | deployment | `arn:{partition}:opsworks:{region}:{account}:deployment/{resource_id}` | DeploymentId | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::OpsWorks::Deployment | aws_opsworks_deployment |
| organizations | organization | `arn:{partition}:organizations::{account}:organization/{resource_id}` | OrganizationId | `^o-[a-z0-9]{10,32}$` |  | AWS::Organizations::Organization | aws_organizations_organization |
| organizations | account | `arn:{partition}:organizations::{account}:account/{resource_id}` | AccountId | `^[0-9]{12}$` |  | AWS::Organizations::Account | aws_organizations_account |
| organizations | organizational_unit | `arn:{partition}:organizations::{account}:ou/{resource_id}` | OrganizationalUnitId | `^ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}$` |  | AWS::Organizations::OrganizationalUnit | aws_organizations_organizational_unit |
| outposts | outpost | `arn:{partition}:outposts:{region}:{account}:outpost/{resource_id}` | OutpostId | `^[a-zA-Z0-9_\-]{1,64}$` |  | AWS::Outposts::Outpost | aws_outposts_outpost |
| personalize | dataset_group | `arn:{partition}:personalize:{region}:{account}:dataset-group/{resource_id}` | DatasetGroupId | `^[a-zA-Z0-9-]{1,63}$` |  | AWS::Personalize::DatasetGroup | aws_personalize_dataset_group |
| personalize | dataset | `arn:{partition}:personalize:{region}:{account}:dataset/{dataset_group_arn}/dataset/{resource_id}` | DatasetArn | `^[a-zA-Z0-9-]{1,63}$` |  | AWS::Personalize::Dataset | aws_personalize_dataset |
| personalize | solution | `arn:{partition}:personalize:{region}:{account}:solution/{resource_id}` | SolutionArn | `^[a-zA-Z0-9-]{1,63}$` |  | AWS::Personalize::Solution | aws_personalize_solution |
| personalize | campaign | `arn:{partition}:personalize:{region}:{account}:campaign/{resource_id}` | CampaignArn | `^[a-zA-Z0-9-]{1,63}$` |  | AWS::Personalize::Campaign | aws_personalize_campaign |
| personalize | event_tracker | `arn:{partition}:personalize:{region}:{account}:event-tracker/{resource_id}` | EventTrackerArn | `^[a-zA-Z0-9-]{1,63}$` |  | AWS::Personalize::EventTracker | aws_personalize_event_tracker |
| pi | dimension | `arn:{partition}:pi:{region}:{account}:dimension:{resource_id}` | DimensionName | `^[a-zA-Z0-9_]+$` |  | AWS::PI::Dimension | aws_pi_dimension |
| pinpoint | app | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::App | aws_pinpoint_app |
| pinpoint | adm_channel | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}/channels/adm` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::ADMChannel | aws_pinpoint_adm_channel |
| pinpoint | apns_channel | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}/channels/apns` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::APNSChannel | aws_pinpoint_apns_channel |
| pinpoint | apns_sandbox_channel | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}/channels/apns_sandbox` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::APNSSandboxChannel | aws_pinpoint_apns_sandbox_channel |
| pinpoint | baidu_channel | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}/channels/baidu` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::BaiduChannel | aws_pinpoint_baidu_channel |
| pinpoint | email_channel | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}/channels/email` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::EmailChannel | aws_pinpoint_email_channel |
| pinpoint | gcm_channel | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}/channels/gcm` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::GCMChannel | aws_pinpoint_gcm_channel |
| pinpoint | sms_channel | `arn:{partition}:mobiletargeting:{region}:{account}:apps/{resource_id}/channels/sms}` | ApplicationId | `^[a-zA-Z0-9]{1,64}$` |  | AWS::Pinpoint::SMSChannel | aws_pinpoint_sms_channel |
| polly | lexicon | `arn:{partition}:polly:{region}:{account}:lexicon/{resource_id}` | LexiconName | `^[a-zA-Z0-9_]+$` |  | AWS::Polly::Lexicon | aws_polly_lexicon |
| qldb | ledger | `arn:{partition}:qldb:{region}:{account}:ledger/{resource_id}` | LedgerName | `^[a-zA-Z0-9_-]{1,32}$` |  | AWS::QLDB::Ledger | aws_qldb_ledger |
| quickSight | group | `arn:{partition}:quicksight:{region}:{account}:group/{resource_id}` | GroupName | `^[a-zA-Z0-9._-]{1,64}$` |  | AWS::QuickSight::Group | aws_quicksight_group |
| quickSight | user | `arn:{partition}:quicksight:{region}:{account}:user/{resource_id}` | UserName | `^[a-zA-Z0-9._-]{1,64}$` |  | AWS::QuickSight::User | aws_quicksight_user |
| ram | resource_share | `arn:{partition}:ram:{region}:{account}:resource-share/{resource_id}` | ResourceShareName | `^[a-zA-Z0-9-]{1,64}$` |  | AWS::RAM::ResourceShare | aws_ram_resource_share |
| ram | resource_share_invitation | `arn:{partition}:ram:{region}:{account}:resource-share-invitation/{resource_id}` | ResourceShareInvitationId | `^[a-zA-Z0-9-]{1,64}$` |  | AWS::RAM::ResourceShareInvitation | aws_ram_resource_share_invitation |
| rds | db_instance | `arn:{partition}:rds:{region}:{account}:db:{resource_id}` | DBInstanceIdentifier | `^[a-zA-Z0-9-]+$` | AwsRdsDbInstance | AWS::RDS::DBInstance | aws_db_instance |
| rds | db_snapshot | `arn:{partition}:rds:{region}:{account}:snapshot:{resource_id}` | DBSnapshotIdentifier | `^[a-zA-Z0-9-]+$` | AwsRdsDbSnapshot | AWS::RDS::DBSnapshot | aws_db_snapshot |
| rds | db_cluster | `arn:{partition}:rds:{region}:{account}:cluster:{resource_id}` | DBClusterIdentifier | `^[a-zA-Z0-9-]+$` | AwsRdsDbCluster | AWS::RDS::DBCluster | aws_rds_cluster |
| rds | db_cluster_snapshot | `arn:{partition}:rds:{region}:{account}:cluster-snapshot:{resource_id}` | DBClusterSnapshotIdentifier | `^[a-zA-Z0-9-]+$` | AwsRdsDbClusterSnapshot | AWS::RDS::DBClusterSnapshot | aws_rds_cluster_snapshot |
| rds | option_group | `arn:{partition}:rds:{region}:{account}:og:{resource_id}` | OptionGroupName | `^[a-zA-Z0-9-]+$` |  | AWS::RDS::OptionGroup | aws_db_option_group |
| rds | parameter_group | `arn:{partition}:rds:{region}:{account}:pg:{resource_id}` | DBParameterGroupName | `^[a-zA-Z0-9-]+$` |  | AWS::RDS::DBParameterGroup | aws_db_parameter_group |
| rds | cluster_parameter_group | `arn:{partition}:rds:{region}:{account}:cluster-pg:{resource_id}` | DBClusterParameterGroupName | `^[a-zA-Z0-9-]+$` |  | AWS::RDS::DBClusterParameterGroup | aws_rds_cluster_parameter_group |
| rds | security_group | `arn:{partition}:rds:{region}:{account}:secgrp:{resource_id}` | DBSecurityGroupName | `^[a-zA-Z0-9-]+$` | AwsRdsDbSecurityGroup | AWS::RDS::DBSecurityGroup | aws_db_security_group |
| rds | subnet_group | `arn:{partition}:rds:{region}:{account}:subgrp:{resource_id}` | DBSubnetGroupName | `^[a-zA-Z0-9-]+$` |  | AWS::RDS::DBSubnetGroup | aws_db_subnet_group |
| rds | event_subscription | `arn:{partition}:rds:{region}:{account}:es:{resource_id}` | EventSubscriptionName | `^[a-zA-Z0-9-_]+$` | AwsRdsEventSubscription | AWS::RDS::EventSubscription | aws_db_event_subscription |
| rds | global_cluster | `arn:{partition}:rds:{region}:{account}:global-cluster:{resource_id}` | GlobalClusterIdentifier | `^[a-zA-Z0-9-]{1,63}$` |  | AWS::RDS::GlobalCluster | aws_rds_global_cluster |
| rds-data | secret | `arn:{partition}:secretsmanager:{region}:{account}:secret:{resource_id}` | SecretId | `^[-0-9a-zA-Z:_/]+$` |  | AWS::SecretsManager::Secret | aws_secretsmanager_secret |
| redshift | cluster | `arn:{partition}:redshift:{region}:{account}:cluster:{resource_id}` | ClusterName | `^([a-z0-9][a-z0-9-]*[a-z0-9]|[a-z0-9])$` | AwsRedshiftCluster | AWS::Redshift::Cluster | aws_redshift_cluster |
| redshift | snapshot | `arn:{partition}:redshift:{region}:{account}:snapshot:{resource_id}` | SnapshotName | `^([a-z0-9][a-z0-9-]*[a-z0-9]|[a-z0-9])$` |  | AWS::Redshift::Snapshot | aws_redshift_snapshot |
| rekognition | collection | `arn:{partition}:rekognition:{region}:{account}:collection/{resource_id}` | CollectionId | `^[a-zA-Z0-9-_]+$` |  | AWS::Rekognition::Collection | aws_rekognition_collection |
| rekognition | stream_processor | `arn:{partition}:rekognition:{region}:{account}:stream-processor/{resource_id}` | StreamProcessorName | `^[a-zA-Z0-9-_]+$` |  | AWS::Rekognition::StreamProcessor | aws_rekognition_stream_processor |
| resource-groups | group | `arn:{partition}:resource-groups:{region}:{account}:group/{resource_id}` | GroupName | `^[a-zA-Z0-9._\-]+$` |  | AWS::ResourceGroups::Group | aws_resourcegroups_group |
| robomaker | robot_application | `arn:{partition}:robomaker:{region}:{account}:robot-application/{resource_id}/{ApplicationVersion}` | ApplicationName | `^[a-zA-Z0-9-_]{1,127}$` |  | AWS::RoboMaker::RobotApplication | aws_robomaker_robot_application |
| robomaker | simulation_application | `arn:{partition}:robomaker:{region}:{account}:simulation-application/{resource_id}/{ApplicationVersion}` | ApplicationName | `^[a-zA-Z0-9-_]{1,127}$` |  | AWS::RoboMaker::SimulationApplication | aws_robomaker_simulation_application |
| robomaker | robot | `arn:{partition}:robomaker:{region}:{account}:robot/{resource_id}` | RobotName | `^[a-zA-Z0-9-_]{1,127}$` |  | AWS::RoboMaker::Robot | aws_robomaker_robot |
| robomaker | simulation_job | `arn:{partition}:robomaker:{region}:{account}:simulation-job/{resource_id}` | SimulationJobArn | `^arn:[a-zA-Z0-9-]+:robomaker:[a-z]{2}(-gov)?-[a-z]+-\d+:[a-z0-9]{12}:simulation-job:[a-zA-Z0-9-_]{1,128}(/\d+)?$` |  | AWS::RoboMaker::SimulationJob | aws_robomaker_simulation_job |
| robomaker | fleet | `arn:{partition}:robomaker:{region}:{account}:fleet/{resource_id}` | FleetName | `^[a-zA-Z0-9-_]{1,127}$` |  | AWS::RoboMaker::Fleet | aws_robomaker_fleet |
| route53 | health_check | `arn:{partition}:route53:::healthcheck/{resource_id}` | HealthCheckId | `^[a-zA-Z0-9]+$` |  | AWS::Route53::HealthCheck | aws_route53_health_check |
| route53 | hosted_zone | `arn:{partition}:route53:::hostedzone/{resource_id}` | HostedZoneId | `^Z[a-zA-Z0-9]+$` |  | AWS::Route53::HostedZone | aws_route53_zone |
| route53 | vpc_association_authorization | `arn:{partition}:route53:::vpc/{region}:{account}:authorizevpcassociation/{resource_id}/{vpc_id}` | HostedZoneId | `^vpc-[a-z0-9]+$` |  | AWS::Route53::VPCAssociationAuthorization | aws_route53_zone_association_authorization |
| route53 | resolver_endpoint | `arn:{partition}:route53resolver:{region}:{account}:resolver-endpoint/{resource_id}` | ResolverEndpointId | `^rslv-[a-z0-9]{17}$` |  | AWS::Route53Resolver::ResolverEndpoint | aws_route53_resolver_endpoint |
| route53 | resolver_rule | `arn:{partition}:route53resolver:{region}:{account}:resolver-rule/{resource_id}` | ResolverRuleId | `^rslvrule-[a-z0-9]{17}$` |  | AWS::Route53Resolver::ResolverRule | aws_route53_resolver_rule |
| route53 | resolver_rule_association | `arn:{partition}:route53resolver:{region}:{account}:resolver-rule-association/{resource_id}` | ResolverRuleAssociationId | `^rslvrassoc-[a-z0-9]{17}$` |  | AWS::Route53Resolver::ResolverRuleAssociation | aws_route53_resolver_rule_association |
| s3 | bucket | `arn:{partition}:s3:::{resource_id}` | BucketName | `^[a-z0-9.-]{3,63}$` | AwsS3Bucket | AWS::S3::Bucket | aws_s3_bucket |
| s3 | object | `arn:{partition}:s3:::{bucket}/{resource_id}` | ObjectName | `.+` | AwsS3Object | AWS::S3::Object | aws_s3_bucket_object |
| s3-object-lambda | access_point | `arn:{partition}:s3-object-lambda:{region}:{account}:accesspoint/{resource_id}` | AccessPointName | `^[a-zA-Z0-9\.\-_]{1,64}$` |  | AWS::S3ObjectLambda::AccessPoint | aws_s3object_lambda_access_point |
| s3-object-lambda | access_point_policy | `arn:{partition}:s3-object-lambda:{region}:{account}:accesspoint-policy/{resource_id}` | AccessPointName | `^[a-zA-Z0-9\.\-_]{1,64}$` |  | AWS::S3ObjectLambda::AccessPointPolicy | aws_s3object_lambda_access_point_policy |
| s3-object-lambda | access_point_configuration | `arn:{partition}:s3-object-lambda:{region}:{account}:accesspoint/{resource_id}/configuration` | AccessPointName | `^[a-zA-Z0-9\.\-_]{1,64}$` |  | AWS::S3ObjectLambda::AccessPointConfiguration | aws_s3object_lambda_access_point_configuration |
| sagemaker | notebook_instance | `arn:{partition}:sagemaker:{region}:{account}:notebook-instance/{resource_id}` | NotebookInstanceName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` | AwsSageMakerNotebookInstance | AWS::SageMaker::NotebookInstance | aws_sagemaker_notebook_instance |
| sagemaker | notebook_instance_lifecycle_configuration | `arn:{partition}:sagemaker:{region}:{account}:notebook-instance-lifecycle-config/{resource_id}` | NotebookInstanceLifecycleConfigName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` |  | AWS::SageMaker::NotebookInstanceLifecycleConfig | aws_sagemaker_notebook_instance_lifecycle_configuration |
| sagemaker | training_job | `arn:{partition}:sagemaker:{region}:{account}:training-job/{resource_id}` | TrainingJobName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` |  | AWS::SageMaker::TrainingJob | aws_sagemaker_training_job |
| sagemaker | processing_job | `arn:{partition}:sagemaker:{region}:{account}:processing-job/{resource_id}` | ProcessingJobName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` |  | AWS::SageMaker::ProcessingJob | aws_sagemaker_processing_job |
| sagemaker | transform_job | `arn:{partition}:sagemaker:{region}:{account}:transform-job/{resource_id}` | TransformJobName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` |  | AWS::SageMaker::TransformJob | aws_sagemaker_transform_job |
| sagemaker | model | `arn:{partition}:sagemaker:{region}:{account}:model/{resource_id}` | ModelName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` |  | AWS::SageMaker::Model | aws_sagemaker_model |
| sagemaker | endpoint_config | `arn:{partition}:sagemaker:{region}:{account}:endpoint-config/{resource_id}` | EndpointConfigName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` |  | AWS::SageMaker::EndpointConfig | aws_sagemaker_endpoint_configuration |
| sagemaker | endpoint | `arn:{partition}:sagemaker:{region}:{account}:endpoint/{resource_id}` | EndpointName | `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$` |  | AWS::SageMaker::Endpoint | aws_sagemaker_endpoint |
| sagemaker | feature_group | `arn:{partition}:sagemaker:{region}:{account}:feature-group/{resource_id}` | FeatureGroupName | `^[a-zA-Z0-9]([a-zA-Z0-9_-]{0,62}[a-zA-Z0-9])?$` |  | AWS::SageMaker::FeatureGroup | aws_sagemaker_feature_group |
| sdb | domain | `arn:{partition}:sdb:{region}:{account}:domain/{resource_id}` | DomainName | `^[a-zA-Z0-9_.-]{3,255}$` |  | AWS::SDB::Domain | aws_sdb_domain |
| secretsmanager | secret | `arn:{partition}:secretsmanager:{region}:{account}:secret:{resource_id}` | SecretId | `^[a-zA-Z0-9/_+=.@-]{1,64}$` | AwsSecretsManagerSecret | AWS::SecretsManager::Secret | aws_secretsmanager_secret |
| securityhub | hub | `arn:{partition}:securityhub:{region}:{account}:hub/default` | none | `` |  | AWS::SecurityHub::Hub | aws_securityhub_account |
| securityhub | product_subscription | `arn:{partition}:securityhub:{region}:{account}:subscription/{resource_id}` | SubscriptionId | `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$` |  | AWS::SecurityHub::ProductSubscription | aws_securityhub_product_subscription |
| serverlessrepo | application | `arn:{partition}:serverlessrepo:{region}:{account}:applications/{resource_id}` | ApplicationId | `^[a-zA-Z0-9-_]+$` |  | AWS::ServerlessRepo::Application | aws_serverlessapplicationrepository_application |
| servicecatalog | product | `arn:{partition}:catalog:{region}:{account}:product/{resource_id}` | ProductId | `^[a-zA-Z0-9-_]{1,64}$` |  | AWS::ServiceCatalog::CloudFormationProduct | aws_servicecatalog_cloudformation_product |
| servicecatalog | portfolio | `arn:{partition}:catalog:{region}:{account}:portfolio/{resource_id}` | PortfolioId | `^[a-zA-Z0-9-_]{1,64}$` |  | AWS::ServiceCatalog::CloudFormationProduct | aws_servicecatalog_portfolio |
| servicecatalog | portfolio_share | `arn:{partition}:catalog:{region}:{account}:share/{resource_id}` | ShareId | `^[a-f0-9]{64}$` |  | AWS::ServiceCatalog::CloudFormationProduct | aws_servicecatalog_portfolio_share |
| servicecatalog | cloudformation_stack_set_constraint | `arn:{partition}:cloudformation:{region}:{account}:stack-set/{StackSetName}:constraint/{resource_id}` | ConstraintId | `^[a-zA-Z0-9-_]{1,64}$` |  | AWS::ServiceCatalog::CloudFormationStackSetConstraint | aws_servicecatalog_stack_set_constraint |
| servicediscovery | namespace | `arn:{partition}:servicediscovery:{region}:{account}:namespace/{resource_id}` | NamespaceId | `^[a-zA-Z0-9_]+$` |  | AWS::ServiceDiscovery::Namespace | aws_service_discovery_private_dns_namespace |
| servicediscovery | service | `arn:{partition}:servicediscovery:{region}:{account}:service/{resource_id}` | ServiceId | `^[a-zA-Z0-9_]+$` |  | AWS::ServiceDiscovery::Service | aws_service_discovery_service |
| ses | configuration_set | `arn:{partition}:ses:{region}:{account}:configuration-set/{resource_id}` | ConfigurationSetName | `^[a-zA-Z0-9_-]{1,64}$` |  | AWS::SES::ConfigurationSet | aws_ses_configuration_set |
| shield | protection | `arn:{partition}:shield::{account}:protection/{resource_id}` | ProtectionId | `^[a-zA-Z0-9_/-]{1,36}$` |  | AWS::Shield::Protection | aws_shield_protection |
| signer | signing_profile | `arn:{partition}:signer:{region}:{account}:signing-profiles/{resource_id}` | SigningProfileName | `^[a-zA-Z0-9_-]{1,64}$` |  | AWS::Signer::SigningProfile | aws_signer_signing_profile |
| sms | app | `arn:{partition}:sms:{region}:{account}:app/{resource_id}` | AppId | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::SMS::App | aws_sms_app |
| sms | server | `arn:{partition}:sms:{region}:{account}:server/{resource_id}` | ServerId | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::SMS::Server | aws_sms_server |
| sms | replication_job | `arn:{partition}:sms:{region}:{account}:replication-job/{resource_id}` | ReplicationJobId | `^[a-zA-Z0-9_-]{1,128}$` |  | AWS::SMS::ReplicationJob | aws_sms_replication_job |
| snowball | job | `arn:{partition}:snowball:{region}:{account}:job/{resource_id}` | JobId | `^[a-zA-Z0-9-]+$` |  | AWS::Snowball::Job | aws_snowball_job |
| sns | topic | `arn:{partition}:sns:{region}:{account}:{resource_id}` | TopicName | `^[a-zA-Z0-9-_]{1,256}$` | AwsSnsTopic | AWS::SNS::Topic | aws_sns_topic |
| sns | subscription | `arn:{partition}:sns:{region}:{account}:{TopicName}:{resource_id}` | SubscriptionId | `^[a-zA-Z0-9-_]{1,256}$` |  | AWS::SNS::Subscription | aws_sns_topic_subscription |
| sqs | queue | `arn:{partition}:sqs:{region}:{account}:{resource_id}` | QueueName | `^[a-zA-Z0-9_-]{1,80}$` | AwsSqsQueue | AWS::SQS::Queue | aws_sqs_queue |
| ssm | document | `arn:{partition}:ssm:{region}:{account}:document/{resource_id}` | DocumentName | `^[a-zA-Z0-9_/+.-]{3,128}$` |  | AWS::SSM::Document | aws_ssm_document |
| ssm | parameter | `arn:{partition}:ssm:{region}:{account}:parameter/{resource_id}` | ParameterName | `^[a-zA-Z0-9_/+.-]{1,2048}$` |  | AWS::SSM::Parameter | aws_ssm_parameter |
| ssm | maintenance_window | `arn:{partition}:ssm:{region}:{account}:maintenancewindow/{resource_id}` | WindowId | `^[a-zA-Z0-9_-]{20,40}$` |  | AWS::SSM::MaintenanceWindow | aws_ssm_maintenance_window |
| ssm | maintenance_window_task | `arn:{partition}:ssm:{region}:{account}:maintenancewindow/{WindowId}/task/{resource_id}` | WindowTaskId | `^[a-zA-Z0-9_-]{20,40}$` |  | AWS::SSM::MaintenanceWindowTask | aws_ssm_maintenance_window_task |
| ssm | patch_baseline | `arn:{partition}:ssm:{region}:{account}:patchbaseline/{resource_id}` | BaselineId | `^[a-zA-Z0-9_-]{1,128}$` | AwsSsmPatchCompliance | AWS::SSM::PatchBaseline | aws_ssm_patch_baseline |
| sso | instance | `arn:{partition}:sso:{region}:{account}:instance/{resource_id}` | InstanceId | `^[a-zA-Z0-9-]+$` |  | AWS::SSO::Instance | aws_sso_instance |
| sso | permission_set | `arn:{partition}:sso:{region}:{account}:permissionSet/{resource_id}` | PermissionSetId | `^[a-zA-Z0-9-]+$` |  | AWS::SSO::PermissionSet | aws_sso_permission_set |
| sso-directory | directory | `arn:{partition}:sso-directory:{region}:{account}:directory/{resource_id}` | DirectoryId | `^[a-zA-Z0-9-_]+$` |  | AWS::SSO::Directory | aws_sso_directory |
| stepfunctions | state_machine | `arn:{partition}:states:{region}:{account}:stateMachine:{resource_id}` | StateMachineName | `^[a-zA-Z0-9-_]+$` |  | AWS::StepFunctions::StateMachine | aws_sfn_state_machine |
| storagegateway | gateway | `arn:{partition}:storagegateway:{region}:{account}:gateway/{resource_id}` | GatewayId | `^[a-zA-Z0-9-_]+$` |  | AWS::StorageGateway::Gateway | aws_storagegateway_gateway |
| storagegateway | share | `arn:{partition}:storagegateway:{region}:{account}:share/{resource_id}` | ShareId | `^[a-zA-Z0-9-_]+$` |  | AWS::StorageGateway::NFSFileShare | aws_storagegateway_nfs_file_share |
| storagegateway | tape | `arn:{partition}:storagegateway:{region}:{account}:tape/{resource_id}` | TapeARN | `^[a-zA-Z0-9-:/_\.\(\)]+$` |  | AWS::StorageGateway::Tape | aws_storagegateway_tape |
| storagegateway | volume | `arn:{partition}:storagegateway:{region}:{account}:gateway/{gateway_id}/volume/{resource_id}` | VolumeId | `^[a-zA-Z0-9-_]+$` |  | AWS::StorageGateway::StorediSCSIVolume | aws_storagegateway_cached_iscsi_volume |
| sts | assumed_role | `arn:{partition}:sts::{account}:assumed-role/{resource_name}/{resource_id}` | RoleSessionName | `^[\w+=,.@-]+$` |  | AWS::STS::AssumedRole | aws_iam_role |
| sts | federated_user | `arn:{partition}:sts::{account}:federated-user/{resource_id}` | UserName | `^[\w+=,.@-]+$` |  | AWS::STS::FederatedUser | aws_iam_user |
| sts | oidc_provider | `arn:{partition}:iam::{account}:oidc-provider/{resource_id}` | Url | `^(https|http)://.*$` |  | AWS::IAM::OpenIDConnectProvider | aws_iam_openid_connect_provider |
| sts | saml_provider | `arn:{partition}:iam::{account}:saml-provider/{resource_id}` | Name | `^[\w+=,.@-]+$` |  | AWS::IAM::SAMLProvider | aws_iam_saml_provider |
| swf | domain | `arn:{partition}:swf:{region}:{account}:domain/{resource_id}` | DomainName | `^[a-zA-Z0-9-_]+$` |  | AWS::SWF::Domain | aws_swf_domain |
| swf | workflow_type | `arn:{partition}:swf:{region}:{account}:workflowType/{DomainName}/{resource_id}` | WorkflowTypeName | `^[a-zA-Z0-9-_]+$` |  | AWS::SWF::WorkflowType | aws_swf_workflow_type |
| swf | activity_type | `arn:{partition}:swf:{region}:{account}:activityType/{DomainName}/{resource_id}` | ActivityTypeName | `^[a-zA-Z0-9-_]+$` |  | AWS::SWF::ActivityType | aws_swf_activity_type |
| swf | workflow_execution | `arn:{partition}:swf:{region}:{account}:workflow/{DomainName}/{WorkflowType}:{resource_id}` | WorkflowExecutionId | `^[-a-zA-Z0-9_]+(?:\.[-a-zA-Z0-9_]+)*$` |  | AWS::SWF::WorkflowExecution | aws_swf_workflow_execution |
| swf | activity_execution | `arn:{partition}:swf:{region}:{account}:activity/{DomainName}/{ActivityType}:{resource_id}` | ActivityId | `^[a-zA-Z0-9-_]+$` |  | AWS::SWF::ActivityTask | aws_swf_activity_task |
| synthetics | canary | `arn:{partition}:synthetics:{region}:{account}:canary:{resource_id}` | CanaryName | `^[a-zA-Z0-9_-]{1,63}$` |  | AWS::Synthetics::Canary | aws_synthetics_canary |
| synthetics | canary_run | `arn:{partition}:synthetics:{region}:{account}:canary:{CanaryName}:run:{resource_id}` | CanaryRunId | `^[a-zA-Z0-9_-]{1,63}$` |  | AWS::Synthetics::CanaryRun | aws_synthetics_canary_run |
| textract | document | `arn:{partition}:textract:{region}:{account}:document/{resource_id}` | DocumentId | `^[a-f0-9]{32}$` |  | AWS::Textract::Document | aws_textract_document |
| transcribe | vocabulary | `arn:{partition}:transcribe:{region}:{account}:vocabulary/{resource_id}` | VocabularyName | `^[a-zA-Z0-9-_]+$` |  | AWS::Transcribe::Vocabulary | aws_transcribe_vocabulary |
| transfer | server | `arn:{partition}:transfer:{region}:{account}:server/{resource_id}` | ServerId | `^[a-zA-Z0-9-_]+$` |  | AWS::Transfer::Server | aws_transfer_server |
| transfer | user | `arn:{partition}:transfer:{region}:{account}:user/{ServerId}/{resource_id}` | UserName | `^[a-zA-Z0-9-_]+$` |  | AWS::Transfer::User | aws_transfer_user |
| translate | terminology | `arn:{partition}:translate:{region}:{account}:terminology/{resource_id}` | TerminologyName | `^[a-zA-Z0-9\-\_]+$` |  | AWS::Translate::Terminology | aws_translate_terminology |
| waf | ipset | `arn:{partition}:waf:{region}:{account}:ipset/{resource_id}` | IpSetId | `^[a-zA-Z0-9]+$` |  | AWS::WAF::IPSet | aws_waf_ipset |
| waf | rule | `arn:{partition}:waf:{region}:{account}:rule/{resource_id}` | RuleId | `^[a-zA-Z0-9]+$` | AwsWafRule | AWS::WAF::Rule | aws_waf_rule |
| waf | rule_group | `arn:{partition}:waf::{account}:rulegroup/{resource_name}/{resource_id}` | RuleGroupId | `^[a-zA-Z0-9]+$` | AwsWafRuleGroup | AWS::WAF::RuleGroup | aws_waf_rule_group |
| waf | web_acl | `arn:{partition}:waf:{region}:{account}:webacl/{resource_id}` | WebACLId | `^[a-zA-Z0-9]+$` | AwsWafWebAcl | AWS::WAF::WebACL | aws_waf_web_acl |
| waf | global_web_acl | `arn:{partition}:waf::{account}:global-webacl/{resource_name}/{resource_id}` | WebACLId | `^[a-zA-Z0-9]+$` |  | AWS::WAFv2::WebACL | aws_wafv2_web_acl |
| waf | rate_based_rule | `arn:{partition}:waf::{account}:ratebasedrule/{resource_name}/{resource_id}` | RuleId | `^[a-zA-Z0-9]+$` | AwsWafRateBasedRule | AWS::WAF::RateBasedRule | aws_waf_rate_based_rule |
| waf-regional | ipset | `arn:{partition}:waf-regional:{region}:{account}:ipset/{resource_id}` | IpSetId | `^[a-zA-Z0-9-]+$` |  | AWS::WAF::IPSet | aws_waf_ipset |
| waf-regional | regional_rule | `arn:{partition}:waf-regional:{region}:{account}:rule/{resource_id}` | RuleId | `^[a-zA-Z0-9-]+$` | AwsWafRegionalRule | AWS::WAF::Rule | aws_waf_rule |
| waf-regional | regional_web_acl | `arn:{partition}:waf-regional:{region}:{account}:webacl/{resource_id}` | WebACLId | `^[a-zA-Z0-9-]+$` | AwsWafRegionalWebAcl | AWS::WAF::WebACL | aws_waf_web_acl |
| waf-regional | regional_rule_group | `arn:{partition}:waf-regional:{region}:{account}:rulegroup/{RuleGroupName}/{resource_id}` | RuleGroupId | `^[a-zA-Z0-9-]+$` | AwsWafRegionalRuleGroup | AWS::WAF::RuleGroup | aws_waf_rule_group |
| waf-regional | regional_rate_based_rule | `arn:{partition}:waf-regional:{region}:{account}:rule/{resource_id}` | RuleId | `^[a-zA-Z0-9-]+$` | AwsWafRegionalRateBasedRule | AWS::WAF::RateBasedRule | aws_waf_rate_based_rule |
| wafv2 | ip_set | `arn:{partition}:wafv2:{region}:{account}:/ipset/{resource_scope}/{resource_id}` | Id | `^[a-zA-Z0-9-]+$` |  | AWS::WAFv2::IPSet | aws_wafv2_ip_set |
| wafv2 | regional_rule_group | `arn:{partition}:wafv2:{region}:{account}:regional/rulegroup/{resource_scope}/{resource_id}` | Id | `^[a-zA-Z0-9-]+$` | AwsWAFv2RuleGroup | AWS::WAFv2::RuleGroup | aws_wafv2_rule_group |
| wafv2 | regional_web_acl | `arn:{partition}:wafv2:{region}:{account}:regional/webacl/{resource_scope}/{resource_id}` | Id | `^[a-zA-Z0-9-]+$` | AwsWAFv2WebACL | AWS::WAFv2::WebACL | aws_wafv2_web_acl |
| wafv2 | rule_group | `arn:{partition}:wafv2:{region}:{account}:global/rulegroup/{resource_scope}/{resource_id}` | Id | `^[a-zA-Z0-9-]+$` | AwsWAFv2RuleGroup | AWS::WAFv2::RuleGroup | aws_wafv2_rule_group |
| wafv2 | web_acl | `arn:{partition}:wafv2:{region}:{account}:global/webacl/{resource_scope}/{resource_id}` | Id | `^[a-zA-Z0-9-]+$` | AwsWAFv2WebACL | AWS::WAFv2::WebACL | aws_wafv2_web_acl |
| wellarchitected | workload | `arn:{partition}:wellarchitected:{region}:{account}:workload/{resource_id}` | WorkloadId | `^[a-zA-Z0-9-]+$` |  | AWS::WellArchitected::Workload | aws_wellarchitected_workload |
| workdocs | document | `arn:{partition}:workdocs:{region}:{account}:{FolderHierarchy}/{resource_id}` | DocumentName | `^[a-zA-Z0-9-_.()]+$` |  | AWS::WorkDocs::Document | aws_workdocs_document |
| workdocs | folder | `arn:{partition}:workdocs:{region}:{account}:{FolderHierarchy}/{resource_id}` | FolderName | `^[a-zA-Z0-9-_.()]+$` |  | AWS::WorkDocs::Folder | aws_workdocs_folder |
| workdocs | user | `arn:{partition}:workdocs:{region}:{account}:user/{resource_id}` | UserId | `^[a-zA-Z0-9_-]+$` |  | AWS::WorkDocs::User | aws_workdocs_user |
| worklink | fleet | `arn:{partition}:worklink:{region}:{account}:fleet/{resource_id}` | FleetArnName | `^.+$` |  | AWS::WorkLink::Fleet | aws_worklink_fleet |
| worklink | website_certificate_authority_association | `arn:{partition}:worklink:{region}:{account}:website-certificate-authority-association/{resource_id}` | WebsiteCertificateAuthorityAssociationId | `^[a-zA-Z0-9]+$` |  | AWS::WorkLink::WebsiteCertificateAuthorityAssociation | aws_worklink_website_certificate_authority_association |
| workmail | organization | `arn:{partition}:workmail:{region}:{account}:organization/{resource_id}` | OrganizationId | `^[a-zA-Z0-9-_]+$` |  | AWS::WorkMail::Organization | aws_workmail_organization |
| workmail | resource | `arn:{partition}:workmail:{region}:{account}:resource/{resource_id}` | ResourceId | `^[a-zA-Z0-9-_]+$` |  | AWS::WorkMail::Resource | aws_workmail_resource |
| workmail | user | `arn:{partition}:workmail:{region}:{account}:user/{resource_id}` | UserId | `^[a-zA-Z0-9-_@.]+$` |  | AWS::WorkMail::User | aws_workmail_user |
| workspaces | directory | `arn:{partition}:workspaces:{region}:{account}:directory/{resource_id}` | DirectoryId | `^[a-zA-Z0-9_-]{10,64}$` |  | AWS::WorkSpaces::Directory | aws_workspaces_directory |
| workspaces | workspace | `arn:{partition}:workspaces:{region}:{account}:workspace/{resource_id}` | WorkspaceId | `^[a-zA-Z0-9_-]{13,68}$` |  | AWS::WorkSpaces::Workspace | aws_workspaces_workspace |

# Projects using this library

- [MetaHub](https://github.com/gabrielsoltz/metahub)
