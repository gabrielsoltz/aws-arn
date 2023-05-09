# aws-arn
A complete list of all AWS ARNs

Isn't anyoning trying to guess the ARN for a specific AWS resource? This is a complete list of all AWS ARNs. The list is sorted alphabetically by service and resource.  This is the only complete list of AWS ARNs available anywhere.

> :warning: **Work in progress**: This is a work in progress.  Not all services and resources are included yet.  Please open an issue or pull request if you find any errors or omissions.

- Total number of services:  153
- Total number of resources:  468

See the full list of ARNs [here](#full-list-of-arns).

# Features

- Generate ARNs for any AWS resource by passing in the resource ID, region and partition
    - Using service and resoruce name
    - Using Terraform resource name
    - Using Cloudformation resource name
- Get the ASFF Resource Name for any AWS resource (e.g. `AwsCertificateManagerCertificate`)
- Get the Cloudformation Resource Name for any AWS resource (e.g. `AWS::CertificateManager::Certificate`)
- Get the Terraform Resource Name for any AWS resource (e.g. `aws_acm_certificate`)

# Contributing to this list

ARNs are defined under [aws_arn/data.py](aws_arn/data.py). 

Format:

```
    "acm": { --> The Service Name (we follow boto3 naming conventions)
        "certificate": {  --> The Resource Name (we follow boto3 naming conventions)
            "arn_format": "arn:{partition}:acm:{region}:{account}:certificate/{resource_id}",
            "id_name": "CertificateId",  --> The Resource Id name
            "id_regexp": "([a-z0-9-]+)", --> The Resource Id regexp
            "asff_name": "AwsCertificateManagerCertificate",   --> The ASFF Resource Name
            "cloudformation": "AWS::CertificateManager::Certificate",  --> The CloudFormation Resource Name
            "terraform": "aws_acm_certificate",  --> The Terraform Resource Name
        }
    },
```

# Use it as a module

## Generate ARN using service and resource name

```
import aws_arn

arn = aws_arn.generate_arn('i-1234568901', 'ec2', 'instance', 'us-east-1', '012345789012', 'aws')

print (arn)
```

## Generate ARN using Terraform resource name
```
arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

arn = aws_arn.generate_arn_from_terraform('i-1234568901', 'aws_instance', 'us-east-1', '012345789012', 'aws')

print (arn)

arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
```

## Generate ARN using Cloudformation resource name
```
arn = aws_arn.generate_arn_from_cloudformation('i-1234568901', 'AWS::EC2::Instance', 'us-east-1', '012345789012', 'aws')

print (arn)

arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

```

# Use it as CLI

## Generate ARN using service and resource name
```
./aws-arn --generate-arn --id test --service ec2 --sub-service instance --region us-east-1 --account 012345789012 --partition aws

arn:aws:ec2:us-east-1:012345789012:instance/test
```

## Generate ARN using Terraform resource name
```
./aws-arn --generate-arn-from-terraform --id test --terraform aws_instance --region us-east-1 --account 012345789012 --partition aws

arn:aws:ec2:us-east-1:012345789012:instance/test
```

## Generate ARN using Cloudformation resource name
```
./aws-arn --generate-arn-from-cloudformation --id test --cloudformation AWS::EC2::Instance --region us-east-1 --account 012345789012 --partition aws

arn:aws:ec2:us-east-1:012345789012:instance/test

```

## Full List of ARNs

| Service | Resource | ARN Format | ID Name | ID Regexp | ASFF Name | CloudFormation | Terraform |
|----|----|----|----|----|----|----|----|
| acm | certificate | arn:{partition}:acm:{region}:{account}:certificate/{resource_id} | CertificateId | ([a-z0-9-]+) | AwsCertificateManagerCertificate | AWS::CertificateManager::Certificate | aws_acm_certificate |
| acm-pca | certificate_authority | arn:{partition}:acm-pca:{region}:{account}:certificate-authority/{resource_id} | CertificateAuthorityId | ([a-z0-9-]+) |  | AWS::ACMPCA::CertificateAuthority | aws_acm_certificate_authority |
| alexaforbusiness | skill | arn:{partition}:aplb:{region}:{account}:skill/{resource_id} | SkillId | ([a-zA-Z0-9_\-]+) |  | AWS::AlexaForBusiness::Skill | aws_alexa_skill |
| apigateway | api | arn:{partition}:apigateway:{region}::/restapis/{resource_id} | ApiId | [a-zA-Z0-9\-]+ | AwsApiGatewayV2Api | AWS::ApiGateway::RestApi | aws_api_gateway_rest_api |
| apigateway | api_key | arn:{partition}:apigateway:{region}::/apikeys/{resource_id} | ApiKeyId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::ApiKey | aws_api_gateway_api_key |
| apigateway | authorizer | arn:{partition}:apigateway:{region}::/restapis/{api_id}/authorizers/{resource_id} | AuthorizerId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::Authorizer | aws_api_gateway_authorizer |
| apigateway | base_path_mapping | arn:{partition}:apigateway:{region}::/restapis/{api_id}/basepathmappings/{resource_id} | BasePathMappingId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::BasePathMapping | aws_api_gateway_base_path_mapping |
| apigateway | client_certificate | arn:{partition}:apigateway:{region}::/clientcertificates/{resource_id} | ClientCertificateId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::ClientCertificate | aws_api_gateway_client_certificate |
| apigateway | deployment | arn:{partition}:apigateway:{region}::/restapis/{api_id}/deployments/{resource_id} | DeploymentId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::Deployment | aws_api_gateway_deployment |
| apigateway | documentation_part | arn:{partition}:apigateway:{region}::/restapis/{api_id}/documentation/parts/{resource_id} | DocumentationPartId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::DocumentationPart | aws_api_gateway_documentation_part |
| apigateway | documentation_version | arn:{partition}:apigateway:{region}::/restapis/{api_id}/documentation/versions/{resource_id} | DocumentationVersion | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::DocumentationVersion | aws_api_gateway_documentation_version |
| apigateway | domain_name | arn:{partition}:apigateway:{region}::/domainnames/{resource_id} | DomainName | [a-zA-Z0-9\.\-_]+ |  | AWS::ApiGateway::DomainName | aws_api_gateway_domain_name |
| apigateway | gateway_response | arn:{partition}:apigateway:{region}::/restapis/{ApiId}/gatewayresponses/{resource_id} | GatewayResponseId | [a-zA-Z0-9\.\-_]+ |  | AWS::ApiGateway::GatewayResponse | aws_api_gateway_gateway_response |
| apigateway | integration | arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{ResourceId}/methods/{HttpMethod}/integrations/{resource_id} | IntegrationId | [a-zA-Z0-9\.\-_]+ |  | AWS::ApiGateway::Integration | aws_api_gateway_integration |
| apigateway | method | arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{ResourceId}/methods/{resource_id} | HttpMethod | [a-zA-Z0-9\.\-_]+ |  | AWS::ApiGateway::Method | aws_api_gateway_method |
| apigateway | model | arn:{partition}:apigateway:{region}::/restapis/{ApiId}/models/{resource_id} | ModelName | [a-zA-Z0-9\.\-_]+ |  | AWS::ApiGateway::Model | aws_api_gateway_model |
| apigateway | request_validator | arn:{partition}:apigateway:{region}::/restapis/{ApiId}/requestvalidators/{resource_id} | RequestValidatorId | [a-zA-Z0-9\.\-_]+ |  | AWS::ApiGateway::RequestValidator | aws_api_gateway_request_validator |
| apigateway | resource | arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{resource_id} | ResourceId | [a-zA-Z0-9\.\-_]+ |  | AWS::ApiGateway::Resource | aws_api_gateway_resource |
| apigateway | rest_api | arn:{partition}:apigateway:{region}::/restapis/{resource_id} | ApiId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::RestApi | aws_api_gateway_rest_api |
| apigateway | stage | arn:{partition}:apigateway:{region}::/restapis/{rest_api_id}/stages/{resource_id} | StageName | [a-zA-Z0-9\-_]+ | AwsApiGatewayV2Stage | AWS::ApiGateway::Stage | aws_api_gateway_stage |
| apigateway | usage_plan | arn:{partition}:apigateway:{region}::/usageplans/{resource_id} | UsagePlanId | [a-zA-Z0-9\-]+ |  | AWS::ApiGateway::UsagePlan | aws_api_gateway_usage_plan |
| apigateway | usage_plan_key | arn:{partition}:apigateway:{region}::/usageplans/{usage_plan_id}/keys/{resource_id} | KeyId | [a-zA-Z0-9-_]+ |  | AWS::ApiGateway::UsagePlanKey | aws_api_gateway_usage_plan_key |
| apigateway | vpc_link | arn:{partition}:apigateway:{region}::/vpclinks/{resource_id} | VpcLinkId | [a-zA-Z0-9\-_]+ |  | AWS::ApiGateway::VpcLink | aws_api_gateway_vpc_link |
| appflow | connector_profile | arn:{partition}:appflow:{region}:{account}:connectorprofile/{resource_id} | ConnectorProfileName | ([a-zA-Z0-9-_]{1,256}) |  | AWS::AppFlow::ConnectorProfile | aws_appflow_connector_profile |
| appflow | flow | arn:{partition}:appflow:{region}:{account}:flow/{resource_id} | FlowName | ([a-zA-Z0-9-_]{1,256}) |  | AWS::AppFlow::Flow | aws_appflow_flow |
| appstream | directory_config | arn:{partition}:appstream:{region}:{account}:directoryconfig/{resource_id} | DirectoryConfigName | [a-zA-Z0-9-]+ |  | AWS::AppStream::DirectoryConfig | aws_appstream_directory_config |
| appstream | fleet | arn:{partition}:appstream:{region}:{account}:fleet/{resource_id} | FleetName | [a-zA-Z0-9-]+ |  | AWS::AppStream::Fleet | aws_appstream_fleet |
| appstream | image | arn:{partition}:appstream:{region}:{account}:image/{resource_id} | ImageName | [a-zA-Z0-9-]+ |  | AWS::AppStream::Image | aws_appstream_image |
| appstream | image_builder | arn:{partition}:appstream:{region}:{account}:imagebuilder/{resource_id} | ImageBuilderName | [a-zA-Z0-9-]+ |  | AWS::AppStream::ImageBuilder | aws_appstream_image_builder |
| appstream | stack | arn:{partition}:appstream:{region}:{account}:stack/{resource_id} | StackName | [a-zA-Z0-9-]+ |  | AWS::AppStream::Stack | aws_appstream_stack |
| athena | workgroup | arn:{partition}:athena:{region}:{account}:workgroup/{resource_id} | WorkGroupName | ([a-zA-Z0-9._-]+) |  | AWS::Athena::WorkGroup | aws_athena_workgroup |
| augmentedairuntime | human_loop | arn:{partition}:sagemaker:{region}:{account}:human-loop/{resource_id} | HumanLoopName | ^[a-zA-Z0-9](-*[a-zA-Z0-9])* |  | AWS::SageMaker::HumanTaskUi | aws_sagemaker_human_task_ui |
| autoscaling | auto_scaling_group | arn:{partition}:autoscaling:{region}:{account}:autoScalingGroup:{resource_id} | AutoScalingGroupName | [a-zA-Z0-9-]{1,255} | AwsAutoScalingAutoScalingGroup | AWS::AutoScaling::AutoScalingGroup | aws_autoscaling_group |
| autoscaling | launch_configuration | arn:{partition}:autoscaling:{region}:{account}:launchConfiguration:{resource_id} | LaunchConfigurationName | [a-zA-Z0-9-]{1,255} | AwsAutoScalingLaunchConfiguration | AWS::AutoScaling::LaunchConfiguration | aws_launch_configuration |
| backup | backup_plan | arn:{partition}:backup:{region}:{account}:backup-plan/{resource_id} | BackupPlanId | ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$ | AwsBackupBackupPlan | AWS::Backup::BackupPlan | aws_backup_plan |
| backup | backup_vault | arn:{partition}:backup:{region}:{account}:backup-vault/{resource_id} | BackupVaultName | ^[a-zA-Z0-9_-]{1,50}$ | AwsBackupBackupVault | AWS::Backup::BackupVault | aws_backup_vault |
| backup | recovery_plan | arn:{partition}:backup:{region}:{account}:recoveryplan/{resource_id} | RecoveryPlanName | ^[a-zA-Z0-9\-\_\.]+$ | AwsBackupRecoveryPoint | AWS::Backup::RecoveryPlan | aws_backup_recovery_point |
| batch | compute_environment | arn:{partition}:batch:{region}:{account}:compute-environment/{resource_id} | ComputeEnvironmentName | [a-zA-Z0-9_-]+ |  | AWS::Batch::ComputeEnvironment | aws_batch_compute_environment |
| batch | job_definition | arn:{partition}:batch:{region}:{account}:job-definition/{resource_id}:{version} | JobDefinitionName | [a-zA-Z0-9_-]+ |  | AWS::Batch::JobDefinition | aws_batch_job_definition |
| batch | job_queue | arn:{partition}:batch:{region}:{account}:job-queue/{resource_id} | JobQueueName | [a-zA-Z0-9_-]+ |  | AWS::Batch::JobQueue | aws_batch_job_queue |
| budgets | budget | arn:{partition}:budgets:{region}:{account}:budget/{resource_id} | BudgetName | ([a-zA-Z0-9-_.]+) |  | AWS::Budgets::Budget | aws_budgets_budget |
| cloud9 | environment | arn:{partition}:cloud9:{region}:{account}:environment:{resource_id} | EnvironmentId | [a-zA-Z0-9-]+ |  | AWS::Cloud9::EnvironmentEC2 | aws_cloud9_environment_ec2 |
| cloudformation | change_set | arn:{partition}:cloudformation:{region}:{account}:changeSet/{resource_id} | ChangeSetId | ([a-zA-Z0-9-]+) |  | AWS::CloudFormation::ChangeSet | aws_cloudformation_change_set |
| cloudformation | stack | arn:{partition}:cloudformation:{region}:{account}:stack/{stack_name}/{stack_id} | StackName | ([a-zA-Z][-a-zA-Z0-9]*) | AwsCloudFormationStack | AWS::CloudFormation::Stack | aws_cloudformation_stack |
| cloudfront | distribution | arn:{partition}:cloudfront::{account}:distribution/{resource_id} | DistributionId | [A-Z0-9]+ | AwsCloudFrontDistribution | AWS::CloudFront::Distribution | aws_cloudfront_distribution |
| cloudfront | field_level_encryption_config | arn:{partition}:cloudfront::{account}:field-level-encryption-config/{resource_id} | FieldLevelEncryptionConfigId | [A-Z0-9]+ |  | AWS::CloudFront::FieldLevelEncryptionConfig | aws_cloudfront_field_level_encryption_config |
| cloudfront | field_level_encryption_profile | arn:{partition}:cloudfront::{account}:field-level-encryption-profile/{resource_id} | FieldLevelEncryptionProfileId | [A-Z0-9]+ |  | AWS::CloudFront::FieldLevelEncryptionProfile | aws_cloudfront_field_level_encryption_profile |
| cloudfront | realtime_log_config | arn:{partition}:cloudfront::{account}:realtime-log-config/{resource_id} | RealtimeLogConfigId | [A-Z0-9]+ |  | AWS::CloudFront::RealtimeLogConfig | aws_cloudfront_realtime_log_config |
| cloudhsmv2 | cluster | arn:{partition}:cloudhsmv2:{region}:{account}:cluster/{resource_id} | ClusterId | [a-zA-Z0-9-]+ |  | AWS::CloudHSMV2::Cluster | aws_cloudhsmv2_cluster |
| cloudhsmv2 | backup | arn:{partition}:cloudhsmv2:{region}:{account}:backup/{resource_id} | BackupId | [a-zA-Z0-9-]+ |  | AWS::CloudHSMV2::Backup | aws_cloudhsmv2_backup |
| cloudhsmv2 | hsm | arn:{partition}:cloudhsmv2:{region}:{account}:cluster/{resource_id}/hsm/{hsm_id} | HsmId | [a-zA-Z0-9-]+ |  | AWS::CloudHSMV2::Hsm | aws_cloudhsmv2_hsm |
| cloudtrail | trail | arn:{partition}:cloudtrail:{region}:{account}:trail/{resource_id} | TrailName | [a-zA-Z0-9-_\.]+ | AwsCloudTrailTrail | AWS::CloudTrail::Trail | aws_cloudtrail |
| cloudwatch | alarm | arn:{partition}:cloudwatch:{region}:{account}:alarm:{resource_id} | AlarmName | ^[a-zA-Z0-9\-_]{1,255}$ | AwsCloudWatchAlarm | AWS::CloudWatch::Alarm | aws_cloudwatch_metric_alarm |
| cloudwatch | dashboard | arn:{partition}:cloudwatch::{account}:dashboard/{resource_id} | DashboardName | ^[a-zA-Z0-9-_ ]{3,255}$ |  | AWS::CloudWatch::Dashboard | aws_cloudwatch_dashboard |
| codeartifact | domain | arn:{partition}:codeartifact:{region}:{account}:domain/{resource_id} | DomainName | ([a-zA-Z0-9._-]+) |  | AWS::CodeArtifact::Domain | aws_codeartifact_domain |
| codeartifact | repository | arn:{partition}:codeartifact:{region}:{account}:repository/{domain_name}/{resource_id} | RepositoryName | ([a-zA-Z0-9._-]+) |  | AWS::CodeArtifact::Repository | aws_codeartifact_repository |
| codeartifact | package | arn:{partition}:codeartifact:{region}:{account}:repository/{domain_name}/{repository_name}/package/{package_format}/{package_name}@{package_version} | PackageName | ([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+) |  | AWS::CodeArtifact::Package | aws_codeartifact_package |
| codebuild | project | arn:{partition}:codebuild:{region}:{account}:project/{resource_id} | ProjectName | ([a-zA-Z0-9-_]+) | AwsCodeBuildProject | AWS::CodeBuild::Project | aws_codebuild_project |
| codecommit | repository | arn:{partition}:codecommit:{region}:{account}:{resource_id} | RepositoryName | ([a-zA-Z0-9_.-]+) |  | AWS::CodeCommit::Repository | aws_codecommit_repository |
| codedeploy | application | arn:{partition}:codedeploy:{region}:{account}:application:{resource_id} | ApplicationName | ([a-zA-Z0-9-_]+) |  | AWS::CodeDeploy::Application | aws_codedeploy_app |
| codedeploy | deployment_config | arn:{partition}:codedeploy:{region}:{account}:deploymentconfig:{resource_id} | DeploymentConfigName | ([a-zA-Z0-9-_]+) |  | AWS::CodeDeploy::DeploymentConfig | aws_codedeploy_deployment_config |
| codedeploy | deployment_group | arn:{partition}:codedeploy:{region}:{account}:deploymentgroup:{resource_id} | ApplicationName/DeploymentGroupName | ([a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+) |  | AWS::CodeDeploy::DeploymentGroup | aws_codedeploy_deployment_group |
| codepipeline | pipeline | arn:{partition}:codepipeline:{region}:{account}:{resource_type}/{resource_id} | PipelineName | ([a-zA-Z0-9_\-]+) |  | AWS::CodePipeline::Pipeline | aws_codepipeline |
| codestar-connections | connection | arn:{partition}:codestar-connections:{region}:{account}:connection/{resource_id} | ConnectionName | ([a-zA-Z0-9-]+) |  | AWS::CodeStarConnections::Connection | aws_codestarconnections_connection |
| codestar-notifications | rule | arn:{partition}:codestar-notifications:{region}:{account}:notificationrule/{resource_id} | NotificationRuleId | ([a-zA-Z0-9-_]+) |  | AWS::CodeStarNotifications::NotificationRule | aws_codestarnotifications_notification_rule |
| cognito-idp | identity_provider | arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id}:identityprovider/{identity_provider_name} | identity_provider_name | ([a-zA-Z0-9_\.\-]+) |  | AWS::Cognito::UserPoolIdentityProvider | aws_cognito_identity_provider |
| cognito-idp | resource_server | arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id}/resource-server/{resource_server_id} | resource_server_id | ([a-zA-Z0-9_\.\-]+) |  | AWS::Cognito::UserPoolResourceServer | aws_cognito_user_pool_resource_server |
| cognito-idp | user_pool | arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id} | user_pool_id | ([a-zA-Z0-9_\.\-]+) |  | AWS::Cognito::UserPool | aws_cognito_user_pool |
| comprehend | document_classifier | arn:{partition}:comprehend:{region}:{account}:document-classifier/{resource_id} | DocumentClassifierName | ([a-zA-Z0-9-_]+) |  | AWS::Comprehend::DocumentClassifier | aws_comprehend_document_classifier |
| comprehend | entity_recognizer | arn:{partition}:comprehend:{region}:{account}:entity-recognizer/{resource_id} | EntityRecognizerName | ([a-zA-Z0-9-_]+) |  | AWS::Comprehend::EntityRecognizer | aws_comprehend_entity_recognizer |
| comprehend | key_phrases_detection_job | arn:{partition}:comprehend:{region}:{account}:key-phrases-detection-job/{resource_id} | KeyPhrasesDetectionJobName | ([a-zA-Z0-9-_]+) |  | AWS::Comprehend::KeyPhrasesDetectionJob | aws_comprehend_key_phrases_detection_job |
| comprehend | sentiment_detection_job | arn:{partition}:comprehend:{region}:{account}:sentiment-detection-job/{resource_id} | SentimentDetectionJobName | ([a-zA-Z0-9-_]+) |  | AWS::Comprehend::SentimentDetectionJob | aws_comprehend_sentiment_detection_job |
| comprehend | topic_detection_job | arn:{partition}:comprehend:{region}:{account}:topic-detection-job/{resource_id} | TopicDetectionJobName | ([a-zA-Z0-9-_]+) |  | AWS::Comprehend::TopicDetectionJob | aws_comprehend_topic_detection_job |
| compute-optimizer | recommendation_export_job | arn:{partition}:compute-optimizer:{region}:{account}:recommendation-export-job/{resource_id} | ExportJobId | ([a-z0-9-]+) |  | AWS::ComputeOptimizer::RecommendationExportJob | aws_compute_optimizer_export_destination |
| config | aggregator | arn:{partition}:config:{region}:{account}:config-aggregator/{resource_id} | ConfigAggregatorName | ([a-zA-Z0-9-_]+) |  | AWS::Config::Aggregator | aws_config_configuration_aggregator |
| config | conformance_pack | arn:{partition}:config:{region}:{account}:conformance-pack/{resource_id} | ConformancePackName | ([a-zA-Z0-9-_]+) |  | AWS::Config::ConformancePack | aws_config_conformance_pack |
| config | config_rule | arn:{partition}:config:{region}:{account}:config-rule/{resource_id} | ConfigRuleName | ([a-zA-Z0-9-_]+) |  | AWS::Config::ConfigRule | aws_config_config_rule |
| config | organization_config_rule | arn:{partition}:config:{region}:{account}:organization-config-rule/{resource_id} | OrganizationConfigRuleName | ([a-zA-Z0-9-_]+) |  | AWS::Config::OrganizationConfigRule | aws_config_organization_custom_rule |
| config | remediation_configuration | arn:{partition}:config:{region}:{account}:remediation-configuration/{resource_id} | RemediationConfigurationName | ([a-zA-Z0-9-_]+) |  | AWS::Config::RemediationConfiguration | aws_config_remediation_configuration |
| cur | report_definition | arn:{partition}:cur:${ReportName}-${YYYYMM}-${AdditionalArtifact}-{region}-{account} | ReportName | ([a-zA-Z0-9-_.]+) |  | AWS::CUR::ReportDefinition | aws_cur_report_definition |
| dataexchange | asset | arn:{partition}:dataexchange:{region}:{account}:asset/{resource_id} | AssetId | ([a-zA-Z0-9-_.]+) |  | AWS::DataExchange::Asset | aws_dataexchange_asset |
| dataexchange | data_set | arn:{partition}:dataexchange:{region}:{account}:data-sets/{resource_id} | DataSetId | ([a-zA-Z0-9-_.]+) |  | AWS::DataExchange::DataSet | aws_dataexchange_data_set |
| dataexchange | job | arn:{partition}:dataexchange:{region}:{account}:job/{resource_id} | JobId | ([a-zA-Z0-9-_.]+) |  | AWS::DataExchange::Job | aws_dataexchange_job |
| dataexchange | revision | arn:{partition}:dataexchange:{region}:{account}:revision/{resource_id} | RevisionId | ([a-zA-Z0-9-_.]+) |  | AWS::DataExchange::Revision | aws_dataexchange_revision |
| datapipeline | pipeline | arn:{partition}:datapipeline:{region}:{account}:{resource_type}/{resource_id} | PipelineId | ([a-zA-Z0-9_-]+) |  | AWS::DataPipeline::Pipeline | aws_datapipeline_pipeline |
| dax | cluster | arn:{partition}:dax:{region}:{account}:cluster:{resource_id} | ClusterName | ([a-zA-Z0-9_.-]+) |  | AWS::DAX::Cluster | aws_dax_cluster |
| devicefarm | project | arn:{partition}:devicefarm:{region}:{account}:project:${resource_id} | ProjectArnSuffix | ([a-zA-Z0-9-_.]+) |  | AWS::DeviceFarm::Project | aws_devicefarm_project |
| devicefarm | device_instance | arn:{partition}:devicefarm:{region}:{account}:device-instance:${resource_id} | DeviceInstanceArnSuffix | ([a-zA-Z0-9-_.]+) |  | AWS::DeviceFarm::DeviceInstance | aws_devicefarm_device_instance |
| devicefarm | device_pool | arn:{partition}:devicefarm:{region}:{account}:devicepool:${resource_id} | DevicePoolArnSuffix | ([a-zA-Z0-9-_.]+) |  | AWS::DeviceFarm::DevicePool | aws_devicefarm_device_pool |
| devicefarm | run | arn:{partition}:devicefarm:{region}:{account}:run:${resource_id} | RunArnSuffix | ([a-zA-Z0-9-_.]+) |  | AWS::DeviceFarm::Run | aws_devicefarm_run |
| devicefarm | job | arn:{partition}:devicefarm:{region}:{account}:job:${resource_id} | JobArnSuffix | ([a-zA-Z0-9-_.]+) |  | AWS::DeviceFarm::Job | aws_devicefarm_job |
| devicefarm | suite | arn:{partition}:devicefarm:{region}:{account}:suite:${resource_id} | SuiteArnSuffix | ([a-zA-Z0-9-_.]+) |  | AWS::DeviceFarm::Suite | aws_devicefarm_suite |
| devicefarm | test | arn:{partition}:devicefarm:{region}:{account}:test:${resource_id} | TestArnSuffix | ([a-zA-Z0-9-_.]+) |  | AWS::DeviceFarm::Test | aws_devicefarm_test |
| directconnect | connection | arn:{partition}:directconnect:{region}:{account}:dxcon:{resource_id} | ConnectionId | ([a-zA-Z0-9-]+) |  | AWS::DirectConnect::Connection | aws_dx_connection |
| directconnect | link_aggregation_group | arn:{partition}:directconnect:{region}:{account}:linkaggregations:{resource_id} | LagId | ([a-zA-Z0-9-]+) |  | AWS::DirectConnect::LinkAggregationGroup | aws_dx_lag |
| directconnect | private_virtual_interface | arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id} | VirtualInterfaceId | ([a-zA-Z0-9-]+) |  | AWS::DirectConnect::PrivateVirtualInterface | aws_dx_private_virtual_interface |
| directconnect | public_virtual_interface | arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id} | VirtualInterfaceId | ([a-zA-Z0-9-]+) |  | AWS::DirectConnect::PublicVirtualInterface | aws_dx_public_virtual_interface |
| directconnect | transit_virtual_interface | arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id} | VirtualInterfaceId | ([a-zA-Z0-9-]+) |  | AWS::DirectConnect::TransitVirtualInterface | aws_dx_transit_virtual_interface |
| dynamodb | table | arn:{partition}:dynamodb:{region}:{account}:table/{resource_id} | TableName | ([a-zA-Z0-9_.-]+) | AwsDynamoDbTable | AWS::DynamoDB::Table | aws_dynamodb_table |
| ec2 | customer_gateway | arn:{partition}:ec2:{region}:{account}:customer-gateway/{resource_id} | CustomerGatewayId | ^cgw-[a-f0-9]{8}$ | AwsEc2CustomerGateway | AWS::EC2::CustomerGateway | aws_customer_gateway |
| ec2 | dedicated_host | arn:{partition}:ec2:{region}:{account}:host/{resource_id} | DedicatedHostId | ^h-[0-9a-f]{17}$ | AwsEc2DedicatedHost | AWS::EC2::Host | aws_ec2_host |
| ec2 | dhcp_options | arn:{partition}:ec2:{region}:{account}:dhcp-options/{resource_id} | DhcpOptionsId | ^dopt-[0-9a-fA-F]{8,17}$ | AwsEc2DhcpOptions | AWS::EC2::DHCPOptions | aws_dhcp_options |
| ec2 | egress_only_internet_gateway | arn:{partition}:ec2:{region}:{account}:egress-only-internet-gateway/{resource_id} | EgressOnlyInternetGatewayId | ^egress-only-igw-[a-f0-9]{8,17}$ | AwsEc2EgressOnlyInternetGateway | AWS::EC2::EgressOnlyInternetGateway | aws_egress_only_internet_gateway |
| ec2 | elastic_gpu | arn:{partition}:ec2:{region}:{account}:elastic-gpu/{resource_id} | ElasticGpuId | ^egp-[0-9a-f]{8,17}$ | AwsEc2ElasticGpu | AWS::EC2::ElasticGpu |  |
| ec2 | elastic_inference_accelerator | arn:{partition}:elastic-inference:{region}:{account}:accelerator/{resource_id} | AcceleratorId | ^eia-[0-9a-f]{17}$ | AwsElasticInferenceAccelerator | AWS::ElasticInference::Accelerator | aws_eia_accelerator |
| ec2 | elastic_ip | arn:{partition}:ec2:{region}:{account}:elastic-ip/{resource_id} | AllocationId | ^eipalloc-[0-9a-fA-F]{8,17}$ | AwsEc2Eip | AWS::EC2::EIP | aws_eip |
| ec2 | flow_log | arn:{partition}:ec2:{region}:{account}:flow-log/{resource_id} | FlowLogId | ^fl-[0-9a-f]{17}$ |  | AWS::EC2::FlowLog | aws_flow_log |
| ec2 | image | arn:{partition}:ec2:{region}:{account}:image/{resource_id} | ImageId | ^ami-[a-f0-9]{8}$|^ami-[a-f0-9]{17}$ |  | AWS::EC2::Image | aws_ami |
| ec2 | instance | arn:{partition}:ec2:{region}:{account}:instance/{resource_id} | InstanceId | ^i-[0-9a-f]{8,17}$ | AwsEc2Instance | AWS::EC2::Instance | aws_instance |
| ec2 | internet_gateway | arn:{partition}:ec2:{region}:{account}:internet-gateway/{resource_id} | InternetGatewayId | ^igw-[a-f0-9]{8,17}$ |  | AWS::EC2::InternetGateway | aws_internet_gateway |
| ec2 | key_pair | arn:{partition}:ec2:{region}:{account}:key-pair/{resource_id} | KeyName | ^[a-zA-Z0-9-_=,.@()]{1,255}$ |  | AWS::EC2::KeyPair | aws_key_pair |
| ec2 | launch_template | arn:{partition}:ec2:{region}:{account}:launch-template/{resource_id} | LaunchTemplateId | ^lt-[a-zA-Z0-9]{17}$ | AwsEc2LaunchTemplate | AWS::EC2::LaunchTemplate | aws_launch_template |
| ec2 | natgateway | arn:{partition}:ec2:{region}:{account}:natgateway/{resource_id} | NatGatewayId | ^nat-[a-f0-9]{8,}$ |  | AWS::EC2::NatGateway | aws_nat_gateway |
| ec2 | network_acl | arn:{partition}:ec2:{region}:{account}:network-acl/{resource_id} | NetworkAclId | ^acl-[0-9a-fA-F]{8,17}$ | AwsEc2NetworkAcl | AWS::EC2::NetworkAcl | aws_network_acl |
| ec2 | network_interface | arn:{partition}:ec2:{region}:{account}:network-interface/{resource_id} | NetworkInterfaceId | ^eni-[0-9a-f]{8}|eni-[0-9a-f]{17}$ | AwsEc2NetworkInterface | AWS::EC2::NetworkInterface | aws_network_interface |
| ec2 | placement_group | arn:{partition}:ec2:{region}:{account}:placement-group/{resource_id} | PlacementGroupName | ^pg-[a-z0-9]{8}$ | AwsEc2PlacementGroup | AWS::EC2::PlacementGroup | aws_placement_group |
| ec2 | reserved_instances | arn:{partition}:ec2:{region}:{account}:reserved-instances/{resource_id} | ReservedInstancesId | ^i-[a-zA-Z0-9]{12}$ | AwsEc2ReservedInstances | AWS::EC2::ReservedInstances | aws_instance |
| ec2 | route_table | arn:{partition}:ec2:{region}:{account}:route-table/{resource_id} | RouteTableId | ^rtb-[a-f0-9]{8,17}$ | AwsEc2RouteTable | AWS::EC2::RouteTable | aws_route_table |
| ec2 | security_group | arn:{partition}:ec2:{region}:{account}:security-group/{resource_id} | SecurityGroupId | ^sg-[0-9a-f]{8,17}$ | AwsEc2SecurityGroup | AWS::EC2::SecurityGroup | aws_security_group |
| ec2 | snapshot | arn:{partition}:ec2:{region}:{account}:snapshot/{resource_id} | SnapshotId | ^snap-[a-f0-9]{8,17}$ | AwsEc2Snapshot | AWS::EC2::Snapshot | aws_ebs_snapshot |
| ec2 | spot_fleet_request | arn:{partition}:ec2:{region}:{account}:spot-fleet-request/{resource_id} | SpotFleetRequestId | ^sfr-[0-9a-f]{8,17}$ | AwsEc2SpotFleetRequest | AWS::EC2::SpotFleet | aws_spot_fleet_request |
| ec2 | spot_instance_request | arn:{partition}:ec2:{region}:{account}:spot-instances-request/{resource_id} | SpotInstanceRequestId | ^sir-[0-9a-f]{8,17}$ | AwsEc2SpotInstanceRequest | AWS::EC2::SpotInstance | aws_spot_instance_request |
| ec2 | subnet | arn:{partition}:ec2:{region}:{account}:subnet/{resource_id} | SubnetId | ^subnet-[0-9a-f]{8,17}$ | AwsEc2Subnet | AWS::EC2::Subnet | aws_subnet |
| ec2 | traffic_mirror_filter | arn:{partition}:ec2:{region}:{account}:traffic-mirror-filter/{resource_id} | TrafficMirrorFilterId | ^tmf-[a-f0-9]{17}$ |  | AWS::EC2::TrafficMirrorFilter | aws_ec2_traffic_mirror_filter |
| ec2 | traffic_mirror_session | arn:{partition}:ec2:{region}:{account}:traffic-mirror-session/{resource_id} | TrafficMirrorSessionId | ^tmse-[a-f0-9]{17}$ |  | AWS::EC2::TrafficMirrorSession | aws_ec2_traffic_mirror_session |
| ec2 | traffic_mirror_target | arn:{partition}:ec2:{region}:{account}:traffic-mirror-target/{resource_id} | TrafficMirrorTargetId | ^tmt-[a-f0-9]{17}$ |  | AWS::EC2::TrafficMirrorTarget | aws_ec2_traffic_mirror_target |
| ec2 | transit_gateway | arn:{partition}:ec2:{region}:{account}:transit-gateway/{resource_id} | TransitGatewayId | ^tgw-\w{8,17}$ | AwsEc2TransitGateway | AWS::EC2::TransitGateway | aws_ec2_transit_gateway |
| ec2 | transit_gateway_attachment | arn:{partition}:ec2:{region}:{account}:transit-gateway-attachment/{resource_id} | TransitGatewayAttachmentId | ^tgw-attach-[0-9a-f]{17}$ |  | AWS::EC2::TransitGatewayAttachment | aws_ec2_transit_gateway_attachment |
| ec2 | transit_gateway_multicast_domain | arn:{partition}:ec2:{region}:{account}:transit-gateway-multicast-domain/{resource_id} | TransitGatewayMulticastDomainId | ^tgmd-[a-f0-9]{8,17}$ |  | AWS::EC2::TransitGatewayMulticastDomain | aws_ec2_transit_gateway_multicast_domain |
| ec2 | transit_gateway_route_table | arn:{partition}:ec2:{region}:{account}:transit-gateway-route-table/{resource_id} | TransitGatewayRouteTableId | ^tgw-rtb-[0-9a-f]{17}$ |  | AWS::EC2::TransitGatewayRouteTable | aws_ec2_transit_gateway_route_table |
| ec2 | volume | arn:{partition}:ec2:{region}:{account}:volume/{resource_id} | VolumeId | ^vol-[a-f0-9]{8}|vol-[a-f0-9]{17}$ | AwsEc2Volume | AWS::EC2::Volume | aws_ebs_volume |
| ec2 | vpc | arn:{partition}:ec2:{region}:{account}:vpc/{resource_id} | VpcId | ^vpc-[0-9a-f]{8,17}$ | AwsEc2Vpc | AWS::EC2::VPC | aws_vpc |
| ec2 | vpc_endpoint | arn:{partition}:ec2:{region}:{account}:vpc-endpoint/{resource_id} | VpcEndpointId | ^vpce-[a-z0-9]{8,}$ |  | AWS::EC2::VPCEndpoint | aws_vpc_endpoint |
| ec2 | vpc_endpoint_service | arn:{partition}:ec2:{region}:{account}:vpc-endpoint-service/{resource_id} | VpcEndpointServiceId | ^vpce-svc-[0-9a-f]{8,}$ | AwsEc2VpcEndpointService | AWS::EC2::VPCEndpointService | aws_vpc_endpoint_service |
| ec2 | vpc_peering_connection | arn:{partition}:ec2:{region}:{account}:vpc-peering-connection/{resource_id} | VpcPeeringConnectionId | ^pcx-[a-z0-9]{8,17}$ | AwsEc2VpcPeeringConnection | AWS::EC2::VPCPeeringConnection | aws_vpc_peering_connection |
| ec2 | vpn_connection | arn:{partition}:ec2:{region}:{account}:vpn-connection/{resource_id} | VpnConnectionId | ^vpn-[a-f0-9]{8}$ | AwsEc2VpnConnection | AWS::EC2::VPNConnection | aws_vpn_connection |
| ec2 | vpn_gateway | arn:{partition}:ec2:{region}:{account}:vpn-gateway/{resource_id} | VpnGatewayId | ^vgw-[0-9a-f]{8}$ |  | AWS::EC2::VPNGateway | aws_vpn_gateway |
| ec2-instance-connect | connect | arn:{partition}:ec2-instance-connect:{region}:{account}:connect/${InstanceId} | InstanceId | ([a-zA-Z0-9\-]+) |  | AWS::EC2::Instance | aws_instance |
| ecr | repository | arn:{partition}:ecr:{region}:{account}:repository/{resource_id} | RepositoryName | ([a-zA-Z0-9-_]+) |  | AwsEcrRepository | aws_ecr_repository |
| ecr | image | arn:{partition}:ecr:{region}:{account}:image/{resource_id} | ImageDigest | ([a-zA-Z0-9-_]+) | AwsEcrContainerImage | AWS::ECR::Image | aws_ecr_lifecycle_policy |
| ecs | cluster | arn:{partition}:ecs:{region}:{account}:cluster/{resource_id} | ClusterName | ([a-zA-Z0-9-_.]+) | AwsEcsCluster | AWS::ECS::Cluster | aws_ecs_cluster |
| ecs | task_definition | arn:{partition}:ecs:{region}:{account}:task-definition/{resource_id} | TaskDefinitionFamily | ([a-zA-Z0-9-_.]+) | AwsEcsTaskDefinition | AWS::ECS::TaskDefinition | aws_ecs_task_definition |
| ecs | task | arn:{partition}:ecs:{region}:{account}:task/{resource_id} | TaskId | ([a-zA-Z0-9-_.]+) | AwsEcsTask | AWS::ECS::Task | aws_ecs_task |
| ecs | service | arn:{partition}:ecs:{region}:{account}:service/{cluster_name}/{service_name} | ServiceName | ([a-zA-Z0-9-_.]+) | AwsEcsService | AWS::ECS::Service | aws_ecs_service |
| ecs | container_instance | arn:{partition}:ecs:{region}:{account}:container-instance/{resource_id} | ContainerInstanceId | ([a-zA-Z0-9-_.]+) | AwsEcsContainer | AWS::ECS::ContainerInstance | aws_ecs_container_instance |
| efs | file_system | arn:{partition}:elasticfilesystem:{region}:{account}:file-system/{resource_id} | FileSystemId | fs-[a-zA-Z0-9]{8} |  | AWS::EFS::FileSystem | aws_efs_file_system |
| efs | access_point | arn:{partition}:elasticfilesystem:{region}:{account}:access-point/{resource_id} | AccessPointId | fsap-[a-zA-Z0-9]{8} | AwsEfsAccessPoint | AWS::EFS::AccessPoint | aws_efs_access_point |
| eks | cluster | arn:{partition}:eks:{region}:{account}:cluster/{resource_id} | ClusterName | ([a-zA-Z0-9._-]+) | AwsEksCluster | AWS::EKS::Cluster | aws_eks_cluster |
| elastic-inference | accelerator_type | arn:{partition}:elastic-inference:{region}:{account}:accelerator-type/{resource_id} | AcceleratorTypeName | ([a-zA-Z0-9-_.]+) |  | AWS::ElasticInference::AcceleratorType | aws_ei_accelerator_type |
| elasticache | cache_cluster | arn:{partition}:elasticache:{region}:{account}:cluster:{resource_id} | CacheClusterId | ([a-zA-Z0-9-]+) |  | AWS::ElastiCache::CacheCluster | aws_elasticache_cluster |
| elasticache | cache_parameter_group | arn:{partition}:elasticache:{region}:{account}:parameter-group:{resource_id} | CacheParameterGroupName | ([a-zA-Z0-9-]+) |  | AWS::ElastiCache::CacheParameterGroup | aws_elasticache_parameter_group |
| elasticache | cache_security_group | arn:{partition}:elasticache:{region}:{account}:security-group:{resource_id} | CacheSecurityGroupName | ([a-zA-Z0-9-]+) |  | AWS::ElastiCache::SecurityGroup | aws_elasticache_security_group |
| elasticache | cache_subnet_group | arn:{partition}:elasticache:{region}:{account}:subnet-group:{resource_id} | CacheSubnetGroupName | ([a-zA-Z0-9-]+) |  | AWS::ElastiCache::SubnetGroup | aws_elasticache_subnet_group |
| elasticache | global_replication_group | arn:{partition}:elasticache:{region}:{account}:global-replication-group:{resource_id} | GlobalReplicationGroupId | ([a-zA-Z0-9-]+) |  | AWS::ElastiCache::GlobalReplicationGroup | aws_elasticache_global_replication_group |
| elasticache | replication_group | arn:{partition}:elasticache:{region}:{account}:cluster:{resource_id} | ReplicationGroupId | ([a-zA-Z0-9-]+) |  | AWS::ElastiCache::ReplicationGroup | aws_elasticache_replication_group |
| elasticache | user_group | arn:{partition}:elasticache:{region}:{account}:user-group:{resource_id} | UserGroupId | ([a-zA-Z0-9-]+) |  | AWS::ElastiCache::UserGroup | aws_elasticache_user_group |
| elasticbeanstalk | application | arn:{partition}:elasticbeanstalk:{region}:{account}:application/{resource_id} | ApplicationName | ([a-zA-Z0-9-_.]+) |  | AWS::ElasticBeanstalk::Application | aws_elastic_beanstalk_application |
| elasticbeanstalk | application_version | arn:{partition}:elasticbeanstalk:{region}:{account}:applicationversion/{resource_id} | ApplicationVersionName | ([a-zA-Z0-9-_.]+) |  | AWS::ElasticBeanstalk::ApplicationVersion | aws_elastic_beanstalk_application_version |
| elasticbeanstalk | environment | arn:{partition}:elasticbeanstalk:{region}:{account}:environment/{resource_id} | EnvironmentId | ([a-zA-Z0-9-_.]+) | AwsElasticBeanstalkEnvironment | AWS::ElasticBeanstalk::Environment | aws_elastic_beanstalk_environment |
| elb | loadbalancer | arn:{partition}:elasticloadbalancing:{region}:{account}:loadbalancer/{resource_id} | LoadBalancerName | [\w.-]{1,32} | AwsElbLoadBalancer | AWS::ElasticLoadBalancing::LoadBalancer | aws_elb |
| elbv2 | loadbalancer | arn:{partition}:elasticloadbalancing:{region}:{account}:loadbalancer/{resource_id} | LoadBalancerName | [\w.-]{1,32} | AwsElbv2LoadBalancer | AWS::ElasticLoadBalancingV2::LoadBalancer | aws_alb |
| elbv2 | targetgroup | arn:{partition}:elasticloadbalancing:{region}:{account}:targetgroup/{resource_id}/{tagergroup_id}} | TargetGroupID | [\w.-]{1,32} |  | AWS::ElasticLoadBalancingV2::TargetGroup | aws_alb_target_group |
| elbv2 | listener | arn:{partition}:elasticloadbalancing:{region}:{account}:listener/{resource_id}/{load_balancer_id}/{listener_id} | ListenerId | (?<=listener\/app\/)[^\/]+ |  | AWS::ElasticLoadBalancingV2::Listener | aws_alb_listener |
| elbv2 | listener_rule | arn:{partition}:elasticloadbalancing:{region}:{account}:listener-rule/{resource_id} | ListenerRuleId | [\w.-]{1,32} |  | AWS::ElasticLoadBalancingV2::ListenerRule | aws_alb_listener_rule |
| elasticmapreduce | cluster | arn:{partition}:elasticmapreduce:{region}:{account}:cluster/{resource_id} | ClusterId | j-[0-9a-zA-Z]+ |  | AWS::EMR::Cluster | aws_emr_cluster |
| elasticmapreduce | security_configuration | arn:{partition}:elasticmapreduce:{region}:{account}:security-configuration/{resource_id} | SecurityConfigurationName | [a-zA-Z0-9_.\-]+ |  | AWS::EMR::SecurityConfiguration | aws_emr_security_configuration |
| elasticmapreduce | step | arn:{partition}:elasticmapreduce:{region}:{account}:cluster/{resource_id}/step/{step_id} | StepId | s-[0-9a-zA-Z]+ |  | AWS::EMR::Step | aws_emr_step |
| elastictranscoder | pipeline | arn:{partition}:elastictranscoder:{region}:{account}:pipeline/{resource_id} | PipelineId | [0-9a-zA-Z-_]{1,255} |  | AWS::ElasticTranscoder::Pipeline | aws_elastictranscoder_pipeline |
| elastictranscoder | preset | arn:{partition}:elastictranscoder:{region}:{account}:preset/{resource_id} | PresetId | [0-9a-zA-Z-_]{1,255} |  | AWS::ElasticTranscoder::Preset | aws_elastictranscoder_preset |
| es | domain | arn:{partition}:es:{region}:{account}:domain/{resource_id} | DomainName | [a-z0-9][a-z0-9-]{2,28}[a-z0-9] | AwsElasticSearchDomain | AWS::Elasticsearch::Domain | aws_elasticsearch_domain |
| events | archive | arn:{partition}:events:{region}:{account}:archive/{resource_id} | ArchiveName | [0-9a-zA-Z_.:-]+ |  | AWS::Events::Archive | aws_cloudwatch_event_archive |
| events | bus | arn:{partition}:events:{region}:{account}:event-bus/{resource_id} | EventBusName | [0-9a-zA-Z_]+ |  | AWS::Events::EventBus | aws_cloudwatch_event_bus |
| events | rule | arn:{partition}:events:{region}:{account}:rule/{resource_id} | RuleName | [0-9a-zA-Z_]+ |  | AWS::Events::Rule | aws_cloudwatch_event_rule |
| firehose | delivery_stream | arn:{partition}:firehose:{region}:{account}:deliverystream/{resource_id} | DeliveryStreamName | [a-zA-Z0-9_-]+ |  | AWS::KinesisFirehose::DeliveryStream | aws_kinesis_firehose_delivery_stream |
| fms | policy | arn:{partition}:fms:{region}:{account}:policy/{resource_id} | PolicyName | [\w-]+ |  | AWS::FMS::Policy | aws_fms_policy |
| fsx | backup | arn:{partition}:fsx:{region}:{account}:backup/{resource_id} | BackupId | backup-[0-9a-f]+ |  | AWS::FSx::Backup | aws_fsx_backup |
| fsx | file_system | arn:{partition}:fsx:{region}:{account}:file-system/{resource_id} | FileSystemId | fs-[0-9a-f]+ |  | AWS::FSx::FileSystem | aws_fsx_lustre_file_system |
| gamelift | alias | arn:{partition}:gamelift:{region}:{account}:alias/{resource_id} | AliasId | ^[a-zA-Z0-9-]{1,128}$ |  | AWS::GameLift::Alias | aws_gamelift_alias |
| gamelift | build | arn:{partition}:gamelift:{region}:{account}:build/{resource_id} | BuildId | ^build-[a-z0-9]{14}$ |  | AWS::GameLift::Build | aws_gamelift_build |
| gamelift | fleet | arn:{partition}:gamelift:{region}:{account}:fleet/{resource_id} | FleetId | ^fleet-[a-z0-9]{14}$ |  | AWS::GameLift::Fleet | aws_gamelift_fleet |
| glacier | vault | arn:{partition}:glacier:{region}:{account}:vaults/{resource_id} | VaultName | ^[a-zA-Z0-9][a-zA-Z0-9-]{0,254}$ |  | AWS::Glacier::Vault | aws_glacier_vault |
| globalaccelerator | accelerator | arn:{partition}:globalaccelerator::{account}:accelerator/{resource_id} | AcceleratorId | [a-z0-9]{16} |  | AWS::GlobalAccelerator::Accelerator | aws_globalaccelerator_accelerator |
| globalaccelerator | listener | arn:{partition}:globalaccelerator::{account}:listener/{resource_id} | ListenerId | [a-z0-9]{16} |  | AWS::GlobalAccelerator::Listener | aws_globalaccelerator_listener |
| globalaccelerator | endpoint_group | arn:{partition}:globalaccelerator::{account}:endpoint-group/{resource_id} | EndpointGroupId | [a-z0-9]{16} |  | AWS::GlobalAccelerator::EndpointGroup | aws_globalaccelerator_endpoint_group |
| glue | catalog | arn:{partition}:glue:{region}:{account}:catalog | None | None |  | AWS::Glue::Catalog | aws_glue_catalog_database |
| glue | crawler | arn:{partition}:glue:{region}:{account}:crawler:{resource_name} | CrawlerName | [-0-9a-zA-Z]+ |  | AWS::Glue::Crawler | aws_glue_crawler |
| glue | database | arn:{partition}:glue:{region}:{account}:database/{resource_id} | DatabaseName | [-0-9a-zA-Z]+ |  | AWS::Glue::Database | aws_glue_catalog_database |
| glue | dev_endpoint | arn:{partition}:glue:{region}:{account}:devEndpoint/{resource_name} | DevEndpointName | [-0-9a-zA-Z]+ |  | AWS::Glue::DevEndpoint | aws_glue_dev_endpoint |
| glue | job | arn:{partition}:glue:{region}:{account}:job/{resource_name} | JobName | [-0-9a-zA-Z]+ |  | AWS::Glue::Job | aws_glue_job |
| glue | partition | arn:{partition}:glue:{region}:{account}:table/{DatabaseName}/{TableName}/partition/{PartitionValues} | None | None |  | AWS::Glue::Partition | aws_glue_catalog_partition |
| glue | trigger | arn:{partition}:glue:{region}:{account}:trigger/{resource_name} | TriggerName | [-0-9a-zA-Z]+ |  | AWS::Glue::Trigger | aws_glue_trigger |
| glue | workflow | arn:{partition}:glue:{region}:{account}:workflow/{resource_name} | WorkflowName | [-0-9a-zA-Z]+ |  | AWS::Glue::Workflow | aws_glue_workflow |
| greengrass | group | arn:{partition}:greengrass:{region}:{account}:/greengrass/groups/{resource_id} | GroupId | ^[a-zA-Z0-9-_]{1,128}$ |  | AWS::Greengrass::Group | aws_greengrass_group |
| guardduty | detector | arn:{partition}:guardduty:{region}:{account}:detector/{resource_id} | DetectorId | ^[0-9a-f]{8,}-[0-9a-f]{4,}-[0-9a-f]{4,}-[0-9a-f]{4,}-[0-9a-f]{12,}$ |  | AWS::GuardDuty::Detector | aws_guardduty_detector |
| guardduty | filter | arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/filter/{subresource_id} | FilterName | ^[a-zA-Z0-9-_]{1,64}$ |  | AWS::GuardDuty::Filter | aws_guardduty_filter |
| guardduty | ipset | arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/ipset/{subresource_id} | IpSetId | ^[a-zA-Z0-9-_]{1,64}$ |  | AWS::GuardDuty::IPSet | aws_guardduty_ipset |
| guardduty | member | arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/member/{subresource_id} | MemberId | ^[0-9a-zA-Z-_]{1,64}$ |  | AWS::GuardDuty::Member | aws_guardduty_member |
| guardduty | threatintelset | arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/threatintelset/{subresource_id} | ThreatIntelSetId | ^[a-zA-Z0-9-_]{1,64}$ |  | AWS::GuardDuty::ThreatIntelSet | aws_guardduty_threatintelset |
| health | event | arn:{partition}:health:{region}:{account}:event/{resource_id} | EventArn | arn:[^:]+:health:[^:]+:[^:]+:event\/[0-9a-f-]+ |  | AWS::Health::Event | aws_health_event |
| health | health_check | arn:{partition}:health:{region}:{account}:healthcheck/{resource_id} | HealthCheckId | [0-9a-f-]{8} |  | AWS::Health::HealthCheck | aws_health_check |
| health | organization_event_detail | arn:{partition}:health:{region}:{account}:event-organization/{event_type_code}/{service}/{event_type_version}/{event_id} | EventArn | arn:[^:]+:health:[^:]+:[^:]+:event\/[0-9a-f-]+ |  | AWS::Health::OrganizationEventDetail | aws_health_organization_event_detail |
| health | service | arn:{partition}:health:{region}:{account}:service/{resource_id} | Service | [a-zA-Z0-9_-]{1,64} |  | AWS::Health::Service | aws_health_service |
| iam | access_key | arn:{partition}:iam::{account}:accesskey/{resource_id} | AccessKeyId | ^[A-Z0-9]{16}$ | AwsIamAccessKey | AWS::IAM::AccessKey | aws_iam_access_key |
| iam | account_alias | arn:{partition}:iam::{account}:alias/{resource_id} | AccountAlias | ^[a-z0-9][a-z0-9.-]{0,62}$ |  | AWS::IAM::AccountAlias | aws_iam_account_alias |
| iam | group | arn:{partition}:iam::{account}:group/{resource_id} | GroupName | ^[a-zA-Z0-9+=,.@_-]{1,128}$ | AwsIamGroup | AWS::IAM::Group | aws_iam_group |
| iam | instance_profile | arn:{partition}:iam::{account}:instance-profile/{resource_id} | InstanceProfileName | ^[a-zA-Z0-9_/+=.@-]{1,128}$ |  | AWS::IAM::InstanceProfile | aws_iam_instance_profile |
| iam | policy | arn:{partition}:iam::{account}:policy/{resource_id} | PolicyName | ^[a-zA-Z0-9+=,.@-_]{1,128}$ | AwsIamPolicy | AWS::IAM::Policy | aws_iam_policy |
| iam | role | arn:{partition}:iam::{account}:role/{resource_id} | RoleName | ^[a-zA-Z_][a-zA-Z0-9_=@,.+-]{1,63}$ | AwsIamRole | AWS::IAM::Role | aws_iam_role |
| iam | server_certificate | arn:{partition}:iam::{account}:server-certificate/{resource_id} | ServerCertificateName | ^[a-zA-Z0-9_/+=.@-]{1,128}$ |  | AWS::IAM::ServerCertificate | aws_iam_server_certificate |
| iam | user | arn:{partition}:iam::{account}:user/{resource_id} | UserName | ^[a-zA-Z0-9_+=,.@-]{1,128}$ | AwsIamUser | AWS::IAM::User | aws_iam_user |
| iam | virtual_mfa_device | arn:{partition}:iam::{account}:mfa/{resource_id} | VirtualMFADeviceName | ^[\w+=,.@-]{1,64}$ |  | AWS::IAM::VirtualMFADevice | aws_iam_virtual_mfa_device |
| iam | group_policy | arn:{partition}:iam::{account}:group/{group_id}/policy/{policy_id} | ['GroupName', 'PolicyName'] | ^[\w+=,.@-]{1,128}$^[\w+=,.@-]{1,128}$ |  | AWS::IAM::Policy | aws_iam_group_policy_attachment |
| iam | role_policy | arn:{partition}:iam::{account}:role/{role_id}/policy/{policy_id} | ['RoleName', 'PolicyName'] | ^[\w+=,.@-]{1,64}$^[\w+=,.@-]{1,128}$ |  | AWS::IAM::Policy | aws_iam_role_policy_attachment |
| iam | user_policy | arn:{partition}:iam::{account}:user/{user_id}/policy/{policy_id} | ['UserName', 'PolicyName'] | ^[\w+=,.@-]{1,64}$^[\w+=,.@-]{1,128}$ |  | AWS::IAM::Policy | aws_iam_user_policy_attachment |
| imagebuilder | component | arn:{partition}:imagebuilder:{region}:{account}:component/{resource_id} | ComponentBuildVersionArn | ^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:component/.$ |  | AWS::ImageBuilder::Component | aws_imagebuilder_component |
| imagebuilder | distribution_configuration | arn:{partition}:imagebuilder:{region}:{account}:distribution-configuration/{resource_id} | DistributionConfigurationArn | ^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:distribution-configuration/.$ |  | AWS::ImageBuilder::DistributionConfiguration | aws_imagebuilder_distribution_configuration |
| imagebuilder | image | arn:{partition}:imagebuilder:{region}:{account}:image/{resource_id} | ImageBuildVersionArn | ^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:image/.$ |  | AWS::ImageBuilder::Image | aws_imagebuilder_image |
| imagebuilder | image_pipeline | arn:{partition}:imagebuilder:{region}:{account}:image-pipeline/{resource_id} | ImagePipelineArn | ^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:image-pipeline/.$ |  | AWS::ImageBuilder::ImagePipeline | aws_imagebuilder_image_pipeline |
| imagebuilder | infrastructure_configuration | arn:{partition}:imagebuilder:{region}:{account}:infrastructure-configuration/{resource_id} | InfrastructureConfigurationArn | ^arn:(aws[a-zA-Z-])?:imagebuilder:[^:]:[^:]:infrastructure-configuration/.$ |  | AWS::ImageBuilder::InfrastructureConfiguration | aws_imagebuilder_infrastructure_configuration |
| inspector | assessment_target | arn:{partition}:inspector:{region}:{account}:target/{resource_id} | AssessmentTargetArn | ^arn:aws:inspector:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:target/[a-zA-Z0-9_-]{36}$ |  | AWS::Inspector::AssessmentTarget | aws_inspector_assessment_target |
| inspector | assessment_template | arn:{partition}:inspector:{region}:{account}:template/{resource_id} | AssessmentTemplateArn | ^arn:aws:inspector:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:template/[a-zA-Z0-9_-]{36}$ |  | AWS::Inspector::AssessmentTemplate | aws_inspector_assessment_template |
| inspector | assessment_run | arn:{partition}:inspector:{region}:{account}:run/{resource_id} | AssessmentRunArn | ^arn:aws:inspector:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:run/[a-zA-Z0-9_-]{36}$ |  | AWS::Inspector::AssessmentRun | aws_inspector_assessment_run |
| iot | authorizer | arn:{partition}:iot:{region}:{account}:authorizer/${AuthorizerName} | AuthorizerName | ^([a-zA-Z0-9:_-]){1,128}$ |  | AWS::IoT::Authorizer | aws_iot_authorizer |
| iot | billing_group | arn:{partition}:iot:{region}:{account}:billinggroup/${BillingGroupName} | BillingGroupName | ^([a-zA-Z0-9:_-]){1,128}$ |  | AWS::IoT::BillingGroup | aws_iot_billing_group |
| iot | certificate | arn:{partition}:iot:{region}:{account}:cert/${CertificateId} | CertificateId | ^([a-f0-9]){64}$ |  | AWS::IoT::Certificate | aws_iot_certificate |
| iot | dimension | arn:{partition}:iot:{region}:{account}:dimension/${DimensionName} | DimensionName | ^([a-zA-Z0-9:_-]){1,128}$ |  | AWS::IoT::Dimension | aws_iot_dimension |
| iot | policy | arn:{partition}:iot:{region}:{account}:policy/${PolicyName} | PolicyName | ^([a-zA-Z0-9:_-]){1,128}$ |  | AWS::IoT::Policy | aws_iot_policy |
| iot | provisioning_template | arn:{partition}:iot:{region}:{account}:provisioningtemplate/${TemplateName} | TemplateName | ^([a-zA-Z0-9:_-]){1,128}$ |  | AWS::IoT::ProvisioningTemplate | aws_iot_provisioning_template |
| iot | rule | arn:{partition}:iot:{region}:{account}:rule/${RuleName} | RuleName | ^([a-zA-Z0-9:_-]){1,128}$ |  | AWS::IoT::TopicRule | aws_iot_topic_rule |
| iot | scheduled_audit | arn:{partition}:iot:{region}:{account}:scheduledaudit/${ScheduledAuditName} | ScheduledAuditName | ^([a-zA-Z0-9:_-]){1,128}$ |  | AWS::IoT::ScheduledAudit | aws_iot_scheduled_audit |
| iot | thing | arn:{partition}:iot:{region}:{account}:thing/{resource_id} | ThingName | ^[a-zA-Z0-9_-]+$ |  | AWS::IoT::Thing | aws_iot_thing |
| iot | thing_group | arn:{partition}:iot:{region}:{account}:thinggroup/{resource_id} | ThingGroupName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT::ThingGroup | aws_iot_thing_group |
| iot | thing_type | arn:{partition}:iot:{region}:{account}:thingtype/{resource_id} | ThingTypeName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT::ThingType | aws_iot_thing_type |
| iot | topic_rule_destination | arn:{partition}:iot:{region}:{account}:topic-rule-destination/{resource_id} | TopicRuleDestinationName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT::TopicRuleDestination | aws_iot_topic_rule_destination |
| iot | topic_rule | arn:{partition}:iot:{region}:{account}:rule/{resource_id} | RuleName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT::TopicRule | aws_iot_topic_rule |
| iot | domain_configuration | arn:{partition}:iot:{region}:{account}:domainconfiguration/{resource_id} | DomainConfigurationName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT::DomainConfiguration | aws_iot_domain_configuration |
| iot | fleet_indexing_configuration | arn:{partition}:iot:{region}:{account}:fleet-indexing-configuration/{resource_id} | IndexingConfigurationName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT::FleetIndexingConfiguration | aws_iot_fleet_indexing_configuration |
| iot | job | arn:{partition}:iot:{region}:{account}:job/{resource_id} | JobId | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT::Job | aws_iot_job |
| iot-device-tester | test_suite_run | arn:{partition}:iot-device-tester:{region}:{account}:test-suite-run:${SuiteDefinitionId}/{resource_id} | SuiteRunId | ^[a-zA-Z0-9-_]{1,128}$ |  | AWS::IoTDeviceTester::TestSuiteRun | aws_iot_device_tester_test_suite_run |
| iot1click-projects | device | arn:{partition}:iot1click:{region}:{account}:device/{resource_id} | DeviceId | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT1Click::Device | aws_iot1click_device |
| iot1click-projects | placement | arn:{partition}:iot1click:{region}:{account}:placement/{resource_id} | PlacementName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT1Click::Placement | aws_iot1click_placement |
| iot1click-projects | project | arn:{partition}:iot1click:{region}:{account}:project/{resource_id} | ProjectName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoT1Click::Project | aws_iot1click_project |
| iotanalytics | channel | arn:{partition}:iotanalytics:{region}:{account}:channel/{resource_id} | ChannelName | ^[a-zA-Z0-9_]+$ |  | AWS::IoTAnalytics::Channel | aws_iot_analytics_channel |
| iotanalytics | dataset | arn:{partition}:iotanalytics:{region}:{account}:dataset/{resource_id} | DatasetName | ^[a-zA-Z0-9_]+$ |  | AWS::IoTAnalytics::Dataset | aws_iot_analytics_dataset |
| iotanalytics | datastore | arn:{partition}:iotanalytics:{region}:{account}:datastore/{resource_id} | DatastoreName | ^[a-zA-Z0-9_]+$ |  | AWS::IoTAnalytics::Datastore | aws_iot_analytics_datastore |
| iotanalytics | pipeline | arn:{partition}:iotanalytics:{region}:{account}:pipeline/{resource_id} | PipelineName | ^[a-zA-Z0-9_]+$ |  | AWS::IoTAnalytics::Pipeline | aws_iot_analytics_pipeline |
| iotevents | input | arn:{partition}:iotevents:{region}:{account}:input/{resource_id} | InputName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoTEvents::Input | aws_iot_events_input |
| iotevents | detector_model | arn:{partition}:iotevents:{region}:{account}:detector-model/{resource_id} | DetectorModelName | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoTEvents::DetectorModel | aws_iot_events_detector_model |
| iotsitewise | asset_model | arn:{partition}:iotsitewise:{region}:{account}:asset-model/{resource_id} | AssetModelId | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoTSiteWise::AssetModel | aws_iotsitewise_asset_model |
| iotsitewise | gateway | arn:{partition}:iotsitewise:{region}:{account}:gateway/{resource_id} | GatewayId | ^[a-zA-Z0-9_-]{1,128}$ |  | AWS::IoTSiteWise::Gateway | aws_iotsitewise_gateway |
| kafka | cluster | arn:{partition}:kafka:{region}:{account}:cluster/{resource_id} | ClusterName | ^[a-zA-Z0-9_-]{1,64}$ |  | AWS::MSK::Cluster | aws_msk_cluster |
| kinesis | stream | arn:{partition}:kinesis:{region}:{account}:stream/{resource_id} | StreamName | ^[a-zA-Z0-9_.-]{1,128}$ | AwsKinesisStream | AWS::Kinesis::Stream | aws_kinesis_stream |
| kinesis | firehose_delivery_stream | arn:{partition}:firehose:{region}:{account}:deliverystream/{resource_id} | DeliveryStreamName | ^[a-zA-Z0-9_.-]{1,64}$ |  | AWS::Firehose::DeliveryStream | aws_kinesis_firehose_delivery_stream |
| kinesis-video-archived-media | archive | arn:{partition}:kinesisvideo:{region}:{account}:archive/{stream_id}/{archive_id} | ArchiveId | ^[a-zA-Z0-9_.-]{1,128}$ |  | AWS::KinesisVideo::Stream/Archive | aws_kinesis_video_archive |
| kinesis-video-archived-media | stream | arn:{partition}:kinesisvideo:{region}:{account}:stream/{stream_id}/{stream_arn} | StreamARN | ^arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:stream/[a-zA-Z0-9_.-]{1,256}/[0-9]+/[0-9]+$ |  | AWS::KinesisVideo::Stream | aws_kinesis_video_stream |
| kinesis-video-media | stream | arn:{partition}:kinesisvideo:{region}:{account}:stream/{stream_id}/{stream_arn} | StreamARN | ^arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:stream/[a-zA-Z0-9_.-]{1,256}/[0-9]+/[0-9]+$ |  | AWS::KinesisVideo::Stream | aws_kinesis_video_stream |
| kinesis-video-signaling | channel | arn:{partition}:kinesisvideo:{region}:{account}:channel/{channel_name}/{channel_arn} | ChannelARN | ^arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9_.-]{1,256}/[0-9]+/[0-9]+$ |  | AWS::KinesisVideo::Channel | aws_kinesis_video_channel |
| kms | key | arn:{partition}:kms:{region}:{account}:key/{resource_id} | KeyId | ^[a-zA-Z0-9-_]{1,64}$ | AwsKmsKey | AWS::KMS::Key | aws_kms_key |
| kms | alias | arn:{partition}:kms:{region}:{account}:alias/{resource_id} | AliasName | ^alias/[a-zA-Z0-9:/_-]{1,256}$ |  | AWS::KMS::Alias | aws_kms_alias |
| lakeformation | data_lake_settings | arn:{partition}:lakeformation:{region}:{account}:datalake/{resource_id}/settings | DataLakeId | ^[a-zA-Z0-9-]{1,255}$ |  | AWS::LakeFormation::DataLakeSettings | aws_lakeformation_data_lake_settings |
| lakeformation | permissions | arn:{partition}:lakeformation:{region}:{account}:permissions/{resource_id} | ResourceId | ^[a-zA-Z0-9-]{1,255}$ |  | AWS::LakeFormation::Permissions | aws_lakeformation_permissions |
| lambda | function | arn:{partition}:lambda:{region}:{account}:function:{resource_id} | FunctionName | ^[a-zA-Z0-9-_]{1,140}$ | AwsLambdaFunction | AWS::Lambda::Function | aws_lambda_function |
| lambda | layer | arn:{partition}:lambda:{region}:{account}:layer:{resource_id} | LayerName | ^[a-zA-Z0-9-_]{1,140}$ | AwsLambdaLayerVersion | AWS::Lambda::LayerVersion | aws_lambda_layer_version |
| lambda | event_source_mapping | arn:{partition}:lambda:{region}:{account}:event-source-mapping:{resource_id} | UUID | ^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$ |  | AWS::Lambda::EventSourceMapping | aws_lambda_event_source_mapping |
| lambda | event_invoke_config | arn:{partition}:lambda:{region}:{account}:event-invoke-config:{resource_id} | UUID | ^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$ |  | AWS::Lambda::EventInvokeConfig | aws_lambda_event_invoke_config |
| lex | bot | arn:{partition}:lex:{region}:{account}:bot:{resource_id} | BotName | ^[a-zA-Z0-9_-]{1,50}$ |  | AWS::Lex::Bot | aws_lex_bot |
| lex | bot_alias | arn:{partition}:lex:{region}:{account}:bot:{BotName}:alias:{resource_id} | BotAlias | ^[a-zA-Z0-9_-]{1,50}$ |  | AWS::Lex::BotAlias | aws_lex_bot_alias |
| lex | bot_channel | arn:{partition}:lex:{region}:{account}:bot-channel:{BotName}:{BotAlias}:{ChannelName} | ChannelName | ^[a-zA-Z0-9_-]{1,50}$ |  | AWS::Lex::BotChannel | aws_lex_bot_channel |
| license-manager | license_configuration | arn:{partition}:license-manager:{region}:{account}:license-configuration/{resource_id} | LicenseConfigurationId | ^[a-zA-Z0-9_-]{1,100}$ |  | AWS::LicenseManager::LicenseConfiguration | aws_licensemanager_license_configuration |
| lightsail | instance | arn:{partition}:lightsail:{region}:{account}:instance/{resource_id} | InstanceName | ^[a-zA-Z0-9-]{1,64}$ |  | AWS::Lightsail::Instance | aws_lightsail_instance |
| lightsail | key_pair | arn:{partition}:lightsail:{region}:{account}:key-pair/{resource_id} | KeyName | ^[a-zA-Z0-9-]{1,64}$ |  | AWS::Lightsail::KeyPair | aws_lightsail_key_pair |
| lightsail | static_ip | arn:{partition}:lightsail:{region}:{account}:static-ip/{resource_id} | StaticIpName | ^[a-zA-Z0-9-]{1,64}$ |  | AWS::Lightsail::StaticIp | aws_lightsail_static_ip |
| lightsail | load_balancer | arn:{partition}:lightsail:{region}:{account}:loadbalancer/{resource_id} | LoadBalancerName | ^[a-zA-Z0-9-]{1,64}$ |  | AWS::Lightsail::LoadBalancer | aws_lightsail_load_balancer |
| lightsail | bucket | arn:{partition}:lightsail:{region}:{account}:bucket/{resource_id} | BucketName | ^[a-zA-Z0-9-]{1,64}$ |  | AWS::Lightsail::Bucket | aws_lightsail_bucket |
| logs | log_group | arn:{partition}:logs:{region}:{account}:log-group:{resource_id} | LogGroupName | ^[a-zA-Z0-9._/-]{1,512}$ |  | AWS::Logs::LogGroup | aws_cloudwatch_log_group |
| logs | log_stream | arn:{partition}:logs:{region}:{account}:log-group:{LogGroupName}:log-stream:{resource_id} | LogStreamName | ^[^:*]*$ |  | AWS::Logs::LogStream | aws_cloudwatch_log_stream |
| logs | metric_filter | arn:{partition}:logs:{region}:{account}:metric-filter:{resource_id} | MetricFilterName | ^[a-zA-Z0-9._/-]{1,512}$ |  | AWS::Logs::MetricFilter | aws_cloudwatch_log_metric_filter |
| logs | destination | arn:{partition}:logs:{region}:{account}:destination:{resource_id} | DestinationName | ^[a-zA-Z0-9._/-]{1,512}$ |  | AWS::Logs::Destination | aws_cloudwatch_log_destination |
| logs | query_definition | arn:{partition}:logs:{region}:{account}:query-definition:{resource_id} | QueryDefinitionName | ^[a-zA-Z0-9._/-]{1,512}$ |  | AWS::Logs::QueryDefinition | aws_cloudwatch_log_query_definition |
| machinelearning |