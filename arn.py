aws_arn = {
    "acm": {
        "certificate": "arn:${Partition}:acm:${Region}:${Account}:certificate/${CertificateId}"
    },
    "acm-pca": {
        "certificate_authority": "arn:${Partition}:acm-pca:${Region}:${Account}:certificate-authority/${CertificateAuthorityId}"
    },
    "alexaforbusiness": {
        "skill": "arn:${Partition}:aplb:${Region}:${Account}:skill/${SkillId}"
    },
    "apigateway": {
        "api": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}",
        "api_key": "arn:${Partition}:apigateway:${Region}::/apikeys/${ApiKeyId}",
        "authorizer": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/authorizers/${AuthorizerId}",
        "base_path_mapping": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/basepathmappings/${BasePathMappingId}",
        "client_certificate": "arn:${Partition}:apigateway:${Region}::/clientcertificates/${ClientCertificateId}",
        "deployment": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/deployments/${DeploymentId}",
        "documentation_part": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/documentation/parts/${DocumentationPartId}",
        "documentation_version": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/documentation/versions/${DocumentationVersion}",
        "domain_name": "arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName}",
        "gateway_response": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/gatewayresponses/${GatewayResponseId}",
        "integration": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/resources/${ResourceId}/methods/${HttpMethod}/integrations/${IntegrationId}",
        "method": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/resources/${ResourceId}/methods/${HttpMethod}",
        "model": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/models/${ModelName}",
        "request_validator": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/requestvalidators/${RequestValidatorId}",
        "resource": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/resources/${ResourceId}",
        "rest_api": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}",
        "stage": "arn:${Partition}:apigateway:${Region}::/restapis/${ApiId}/stages/${StageName}",
        "usage_plan": "arn:${Partition}:apigateway:${Region}::/usageplans/${UsagePlanId}",
        "usage_plan_key": "arn:${Partition}:apigateway:${Region}::/usageplans/${UsagePlanId}/keys/${KeyId}",
        "vpc_link": "arn:${Partition}:apigateway:${Region}::/vpclinks/${VpcLinkId}",
    },
    "appflow": {
        "connector_profile": "arn:${Partition}:appflow:${Region}:${Account}:connectorprofile/${ConnectorProfileName}",
        "flow": "arn:${Partition}:appflow:${Region}:${Account}:flow/${FlowName}",
    },
    "appstream": {
        "directory_config": "arn:${Partition}:appstream:${Region}:${Account}:directoryconfig/${DirectoryConfigName}",
        "fleet": "arn:${Partition}:appstream:${Region}:${Account}:fleet/${FleetName}",
        "image": "arn:${Partition}:appstream:${Region}:${Account}:image/${ImageName}",
        "image_builder": "arn:${Partition}:appstream:${Region}:${Account}:imagebuilder/${ImageBuilderName}",
        "stack": "arn:${Partition}:appstream:${Region}:${Account}:stack/${StackName}",
    },
    "athena": {
        "workgroup": "arn:${Partition}:athena:${Region}:${Account}:workgroup/${WorkGroupName}"
    },
    "augmentedairuntime": {
        "human_loop": "arn:${Partition}:sagemaker:${Region}:${Account}:human-loop/${HumanLoopName}"
    },
    "autoscaling": {
        "auto_scaling_group": "arn:${Partition}:autoscaling:${Region}:${Account}:autoScalingGroup:${AutoScalingGroupName}",
        "launch_configuration": "arn:${Partition}:autoscaling:${Region}:${Account}:launchConfiguration:${LaunchConfigurationName}",
    },
    "batch": {
        "compute_environment": "arn:${Partition}:batch:${Region}:${Account}:compute-environment/${ComputeEnvironmentName}",
        "job_definition": "arn:${Partition}:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${JobDefinitionVersion}",
        "job_queue": "arn:${Partition}:batch:${Region}:${Account}:job-queue/${JobQueueName}",
    },
    "budgets": {
        "budget": "arn:${Partition}:budgets:${Region}:${Account}:budget/${BudgetName}"
    },
    "cloud9": {
        "environment": "arn:${Partition}:cloud9:${Region}:${Account}:environment:${EnvironmentId}"
    },
    "cloudformation": {
        "change_set": "arn:${Partition}:cloudformation:${Region}:${Account}:changeSet/${ChangeSetId}",
        "stack": "arn:${Partition}:cloudformation:${Region}:${Account}:stack/${StackName}/${StackId}",
    },
    "cloudfront": {
        "distribution": "arn:${Partition}:cloudfront::${Account}:distribution/${DistributionId}",
        "field_level_encryption_config": "arn:${Partition}:cloudfront::${Account}:field-level-encryption-config/${FieldLevelEncryptionConfigId}",
        "field_level_encryption_profile": "arn:${Partition}:cloudfront::${Account}:field-level-encryption-profile/${FieldLevelEncryptionProfileId}",
        "realtime_log_config": "arn:${Partition}:cloudfront::${Account}:realtime-log-config/${RealtimeLogConfigId}",
    },
    "cloudhsmv2": {
        "cluster": "arn:${Partition}:cloudhsmv2:${Region}:${Account}:cluster/${ClusterId}",
        "backup": "arn:${Partition}:cloudhsmv2:${Region}:${Account}:backup/${BackupId}",
        "hsm": "arn:${Partition}:cloudhsmv2:${Region}:${Account}:cluster/${ClusterId}/hsm/${HsmId}",
    },
    "cloudtrail": {
        "trail": "arn:${Partition}:cloudtrail:${Region}:${Account}:trail/${TrailName}"
    },
    "cloudwatch": {
        "alarm": "arn:${Partition}:cloudwatch:${Region}:${Account}:alarm:${AlarmName}",
        "dashboard": "arn:${Partition}:cloudwatch::${Account}:dashboard/${DashboardName}",
    },
    "codeartifact": {
        "domain": "arn:${Partition}:codeartifact:${Region}:${Account}:domain/${DomainName}",
        "package": "arn:${Partition}:codeartifact:${Region}:${Account}:repository/${DomainName}/${RepositoryName}/package/${PackageFormat}/${PackageName}@${PackageVersion}",
        "repository": "arn:${Partition}:codeartifact:${Region}:${Account}:repository/${DomainName}/${RepositoryName}",
    },
    "codebuild": {
        "project": "arn:${Partition}:codebuild:${Region}:${Account}:project/${ProjectName}"
    },
    "codecommit": {
        "repository": "arn:${Partition}:codecommit:${Region}:${Account}:${RepositoryName}"
    },
    "codedeploy": {
        "application": "arn:${Partition}:codedeploy:${Region}:${Account}:application:${ApplicationName}",
        "deployment_config": "arn:${Partition}:codedeploy:${Region}:${Account}:deploymentconfig:${DeploymentConfigName}",
        "deployment_group": "arn:${Partition}:codedeploy:${Region}:${Account}:deploymentgroup:${ApplicationName}/${DeploymentGroupName}",
    },
    "codepipeline": {
        "pipeline": "arn:${Partition}:codepipeline:${Region}:${Account}:${PipelineName}"
    },
    "codestar-connections": {
        "connection": "arn:${Partition}:codestar-connections:${Region}:${Account}:connection/${ConnectionName}"
    },
    "codestar-notifications": {
        "rule": "arn:${Partition}:codestar-notifications:${Region}:${Account}:notificationrule/${NotificationRuleId}"
    },
    "cognito-idp": {
        "identity_provider": "arn:${Partition}:cognito-idp:${Region}:${Account}:userpool/${UserPoolId}:identityprovider/${ProviderName}",
        "resource_server": "arn:${Partition}:cognito-idp:${Region}:${Account}:userpool/${UserPoolId}/resource-server/${ResourceServerId}",
        "user_pool": "arn:${Partition}:cognito-idp:${Region}:${Account}:userpool/${UserPoolId}",
    },
    "comprehend": {
        "document_classifier": "arn:${Partition}:comprehend:${Region}:${Account}:document-classifier/${DocumentClassifierName}",
        "entity_recognizer": "arn:${Partition}:comprehend:${Region}:${Account}:entity-recognizer/${EntityRecognizerName}",
        "key_phrases_detection_job": "arn:${Partition}:comprehend:${Region}:${Account}:key-phrases-detection-job/${KeyPhrasesDetectionJobName}",
        "sentiment_detection_job": "arn:${Partition}:comprehend:${Region}:${Account}:sentiment-detection-job/${SentimentDetectionJobName}",
        "topic_detection_job": "arn:${Partition}:comprehend:${Region}:${Account}:topic-detection-job/${TopicDetectionJobName}",
    },
    "compute-optimizer": {
        "recommendation_export_job": "arn:${Partition}:compute-optimizer:${Region}:${Account}:recommendation-export-job/${ExportJobId}"
    },
    "config": {
        "aggregator": "arn:${Partition}:config:${Region}:${Account}:config-aggregator/${ConfigAggregatorName}",
        "conformance_pack": "arn:${Partition}:config:${Region}:${Account}:conformance-pack/${ConformancePackName}",
        "config_rule": "arn:${Partition}:config:${Region}:${Account}:config-rule/${ConfigRuleName}",
        "organization_config_rule": "arn:${Partition}:config:${Region}:${Account}:organization-config-rule/${OrganizationConfigRuleName}",
        "remediation_configuration": "arn:${Partition}:config:${Region}:${Account}:remediation-configuration/${RemediationConfigurationName}",
    },
    "cur": {
        "report_definition": "arn:${Partition}:cur:${ReportName}-${YYYYMM}-${AdditionalArtifact}-${Region}-${Account}"
    },
    "dataexchange": {
        "asset": "arn:${Partition}:dataexchange:${Region}:${Account}:asset/${AssetId}",
        "data_set": "arn:${Partition}:dataexchange:${Region}:${Account}:data-sets/${DataSetId}",
        "job": "arn:${Partition}:dataexchange:${Region}:${Account}:job/${JobId}",
        "revision": "arn:${Partition}:dataexchange:${Region}:${Account}:revision/${RevisionId}",
    },
    "datapipeline": {
        "pipeline": "arn:${Partition}:datapipeline:${Region}:${Account}:${PipelineId}"
    },
    "dax": {
        "cluster": "arn:${Partition}:dax:${Region}:${Account}:cluster:${ClusterName}"
    },
    "devicefarm": {
        "project": "arn:${Partition}:devicefarm:${Region}:${Account}:project:${ProjectArnSuffix}",
        "device_instance": "arn:${Partition}:devicefarm:${Region}:${Account}:device-instance:${DeviceInstanceArnSuffix}",
        "device_pool": "arn:${Partition}:devicefarm:${Region}:${Account}:devicepool:${DevicePoolArnSuffix}",
        "run": "arn:${Partition}:devicefarm:${Region}:${Account}:run:${RunArnSuffix}",
        "job": "arn:${Partition}:devicefarm:${Region}:${Account}:job:${JobArnSuffix}",
        "suite": "arn:${Partition}:devicefarm:${Region}:${Account}:suite:${SuiteArnSuffix}",
        "test": "arn:${Partition}:devicefarm:${Region}:${Account}:test:${TestArnSuffix}",
    },
    "directconnect": {
        "connection": "arn:${Partition}:directconnect:${Region}:${Account}:dxcon:${ConnectionId}",
        "link_aggregation_group": "arn:${Partition}:directconnect:${Region}:${Account}:linkaggregations:${LagId}",
        "private_virtual_interface": "arn:${Partition}:directconnect:${Region}:${Account}:dxvif:${VirtualInterfaceId}",
        "public_virtual_interface": "arn:${Partition}:directconnect:${Region}:${Account}:dxvif:${VirtualInterfaceId}",
        "transit_virtual_interface": "arn:${Partition}:directconnect:${Region}:${Account}:dxvif:${VirtualInterfaceId}",
    },
    "dynamodb": {
        "table": "arn:${Partition}:dynamodb:${Region}:${Account}:table/${TableName}"
    },
    "ec2": {
        "customer_gateway": "arn:${Partition}:ec2:${Region}:${Account}:customer-gateway/${CustomerGatewayId}",
        "dedicated_host": "arn:${Partition}:ec2:${Region}:${Account}:host/${DedicatedHostId}",
        "dhcp_options": "arn:${Partition}:ec2:${Region}:${Account}:dhcp-options/${DhcpOptionsId}",
        "egress_only_internet_gateway": "arn:${Partition}:ec2:${Region}:${Account}:egress-only-internet-gateway/${EgressOnlyInternetGatewayId}",
        "elastic_gpu": "arn:${Partition}:ec2:${Region}:${Account}:elastic-gpu/${ElasticGpuId}",
        "elastic_inference_accelerator": "arn:${Partition}:elastic-inference:${Region}:${Account}:accelerator/${AcceleratorId}",
        "flow_log": "arn:${Partition}:ec2:${Region}:${Account}:flow-log/${FlowLogId}",
        "image": "arn:${Partition}:ec2:${Region}:${Account}:image/${ImageId}",
        "instance": "arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}",
        "internet_gateway": "arn:${Partition}:ec2:${Region}:${Account}:internet-gateway/${InternetGatewayId}",
        "key_pair": "arn:${Partition}:ec2:${Region}:${Account}:key-pair/${KeyName}",
        "launch_template": "arn:${Partition}:ec2:${Region}:${Account}:launch-template/${LaunchTemplateId}",
        "nat_gateway": "arn:${Partition}:ec2:${Region}:${Account}:natgateway/${NatGatewayId}",
        "network_acl": "arn:${Partition}:ec2:${Region}:${Account}:network-acl/${NetworkAclId}",
        "network_interface": "arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}",
        "placement_group": "arn:${Partition}:ec2:${Region}:${Account}:placement-group/${PlacementGroupName}",
        "reserved_instances": "arn:${Partition}:ec2:${Region}:${Account}:reserved-instances/${ReservedInstancesId}",
        "route_table": "arn:${Partition}:ec2:${Region}:${Account}:route-table/${RouteTableId}",
        "security_group": "arn:${Partition}:ec2:${Region}:${Account}:security-group/${SecurityGroupId}",
        "snapshot": "arn:${Partition}:ec2:${Region}:${Account}:snapshot/${SnapshotId}",
        "spot_fleet_request": "arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}",
        "spot_instance_request": "arn:${Partition}:ec2:${Region}:${Account}:spot-instances-request/${SpotInstanceRequestId}",
        "subnet": "arn:${Partition}:ec2:${Region}:${Account}:subnet/${SubnetId}",
        "traffic_mirror_filter": "arn:${Partition}:ec2:${Region}:${Account}:traffic-mirror-filter/${TrafficMirrorFilterId}",
        "traffic_mirror_session": "arn:${Partition}:ec2:${Region}:${Account}:traffic-mirror-session/${TrafficMirrorSessionId}",
        "traffic_mirror_target": "arn:${Partition}:ec2:${Region}:${Account}:traffic-mirror-target/${TrafficMirrorTargetId}",
        "transit_gateway": "arn:${Partition}:ec2:${Region}:${Account}:transit-gateway/${TransitGatewayId}",
        "transit_gateway_attachment": "arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-attachment/${TransitGatewayAttachmentId}",
        "transit_gateway_multicast_domain": "arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-multicast-domain/${TransitGatewayMulticastDomainId}",
        "transit_gateway_route_table": "arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-route-table/${TransitGatewayRouteTableId}",
        "volume": "arn:${Partition}:ec2:${Region}:${Account}:volume/${VolumeId}",
        "vpc": "arn:${Partition}:ec2:${Region}:${Account}:vpc/${VpcId}",
        "vpc_endpoint": "arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint/${VpcEndpointId}",
        "vpc_endpoint_service": "arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint-service/${VpcEndpointServiceId}",
        "vpc_peering_connection": "arn:${Partition}:ec2:${Region}:${Account}:vpc-peering-connection/${VpcPeeringConnectionId}",
        "vpn_connection": "arn:${Partition}:ec2:${Region}:${Account}:vpn-connection/${VpnConnectionId}",
        "vpn_gateway": "arn:${Partition}:ec2:${Region}:${Account}:vpn-gateway/${VpnGatewayId}",
    },
    "ec2-instance-connect": {
        "connect": "arn:${Partition}:ec2-instance-connect:${Region}:${Account}:connect/${InstanceId}"
    },
    "ecr": {
        "repository": "arn:${Partition}:ecr:${Region}:${Account}:repository/${RepositoryName}"
    },
    "ecs": {
        "cluster": "arn:${Partition}:ecs:${Region}:${Account}:cluster/${ClusterName}",
        "task_definition": "arn:${Partition}:ecs:${Region}:${Account}:task-definition/${TaskDefinitionFamily}:${TaskDefinitionRevision}",
        "task": "arn:${Partition}:ecs:${Region}:${Account}:task/${TaskId}",
        "service": "arn:${Partition}:ecs:${Region}:${Account}:service/${ClusterName}/${ServiceName}",
        "container_instance": "arn:${Partition}:ecs:${Region}:${Account}:container-instance/${ContainerInstanceId}",
    },
    "efs": {
        "file_system": "arn:${Partition}:elasticfilesystem:${Region}:${Account}:file-system/${FileSystemId}"
    },
    "eks": {
        "cluster": "arn:${Partition}:eks:${Region}:${Account}:cluster/${ClusterName}"
    },
    "elastic-inference": {
        "accelerator_type": "arn:${Partition}:elastic-inference:${Region}:${Account}:accelerator-type/${AcceleratorTypeName}"
    },
    "elasticache": {
        "cache_cluster": "arn:${Partition}:elasticache:${Region}:${Account}:cluster:${CacheClusterId}",
        "cache_parameter_group": "arn:${Partition}:elasticache:${Region}:${Account}:parameter-group:${CacheParameterGroupName}",
        "cache_security_group": "arn:${Partition}:elasticache:${Region}:${Account}:security-group:${CacheSecurityGroupName}",
        "cache_subnet_group": "arn:${Partition}:elasticache:${Region}:${Account}:subnet-group:${CacheSubnetGroupName}",
        "global_replication_group": "arn:${Partition}:elasticache:${Region}:${Account}:global-replication-group:${GlobalReplicationGroupId}",
        "replication_group": "arn:${Partition}:elasticache:${Region}:${Account}:cluster:${ReplicationGroupId}",
        "user_group": "arn:${Partition}:elasticache:${Region}:${Account}:user-group:${UserGroupId}",
    },
    "elasticbeanstalk": {
        "application": "arn:${Partition}:elasticbeanstalk:${Region}:${Account}:application/${ApplicationName}",
        "application_version": "arn:${Partition}:elasticbeanstalk:${Region}:${Account}:applicationversion/${ApplicationName}/${ApplicationVersionName}",
        "environment": "arn:${Partition}:elasticbeanstalk:${Region}:${Account}:environment/${EnvironmentId}",
    },
    "elasticfilesystem": {
        "file_system": "arn:${Partition}:elasticfilesystem:${Region}:${Account}:file-system/${FileSystemId}",
        "mount_target": "arn:${Partition}:elasticfilesystem:${Region}:${Account}:mount-target/${MountTargetId}",
    },
    "elasticloadbalancing": {
        "load_balancer": "arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/${LoadBalancerName}",
        "target_group": "arn:${Partition}:elasticloadbalancing:${Region}:${Account}:targetgroup/${TargetGroupName}/${TargetGroupID}",
        "listener": "arn:${Partition}:elasticloadbalancing:${Region}:${Account}:listener/${LoadBalancerName}/${ListenerId}",
        "listener_rule": "arn:${Partition}:elasticloadbalancing:${Region}:${Account}:listener-rule/${LoadBalancerName}/${ListenerRuleId}",
    },
    "elasticmapreduce": {
        "cluster": "arn:${Partition}:elasticmapreduce:${Region}:${Account}:cluster/${ClusterId}",
        "security_configuration": "arn:${Partition}:elasticmapreduce:${Region}:${Account}:security-configuration/${SecurityConfigurationName}",
        "step": "arn:${Partition}:elasticmapreduce:${Region}:${Account}:cluster/${ClusterId}/step/${StepId}",
    },
    "elastictranscoder": {
        "pipeline": "arn:${Partition}:elastictranscoder:${Region}:${Account}:pipeline/${PipelineId}",
        "preset": "arn:${Partition}:elastictranscoder:${Region}:${Account}:preset/${PresetId}",
    },
    "es": {"domain": "arn:${Partition}:es:${Region}:${Account}:domain/${DomainName}"},
    "events": {
        "archive": "arn:${Partition}:events:${Region}:${Account}:archive/${ArchiveName}",
        "bus": "arn:${Partition}:events:${Region}:${Account}:event-bus/${EventBusName}",
        "rule": "arn:${Partition}:events:${Region}:${Account}:rule/${RuleName}",
    },
    "firehose": {
        "delivery_stream": "arn:${Partition}:firehose:${Region}:${Account}:deliverystream/${DeliveryStreamName}"
    },
    "fms": {"policy": "arn:${Partition}:fms:${Region}:${Account}:policy/${PolicyName}"},
    "fsx": {
        "backup": "arn:${Partition}:fsx:${Region}:${Account}:backup/${BackupId}",
        "file_system": "arn:${Partition}:fsx:${Region}:${Account}:file-system/${FileSystemId}",
    },
    "gamelift": {
        "alias": "arn:${Partition}:gamelift:${Region}:${Account}:alias/${AliasId}",
        "build": "arn:${Partition}:gamelift:${Region}:${Account}:build/${BuildId}",
        "fleet": "arn:${Partition}:gamelift:${Region}:${Account}:fleet/${FleetId}",
    },
    "glacier": {
        "vault": "arn:${Partition}:glacier:${Region}:${Account}:vaults/${VaultName}"
    },
    "globalaccelerator": {
        "accelerator": "arn:${Partition}:globalaccelerator::${Account}:accelerator/${AcceleratorId}",
        "listener": "arn:${Partition}:globalaccelerator::${Account}:listener/${AcceleratorId}/${ListenerId}",
        "endpoint_group": "arn:${Partition}:globalaccelerator::${Account}:endpoint-group/${EndpointGroupId}",
    },
    "glue": {
        "catalog": "arn:${Partition}:glue:${Region}:${Account}:catalog",
        "crawler": "arn:${Partition}:glue:${Region}:${Account}:crawler:${CrawlerName}",
        "database": "arn:${Partition}:glue:${Region}:${Account}:database/${DatabaseName}",
        "dev_endpoint": "arn:${Partition}:glue:${Region}:${Account}:devEndpoint/${DevEndpointName}",
        "job": "arn:${Partition}:glue:${Region}:${Account}:job/${JobName}",
        "partition": "arn:${Partition}:glue:${Region}:${Account}:table/${DatabaseName}/${TableName}/partition/${PartitionValues}",
        "trigger": "arn:${Partition}:glue:${Region}:${Account}:trigger/${TriggerName}",
        "workflow": "arn:${Partition}:glue:${Region}:${Account}:workflow/${WorkflowName}",
    },
    "greengrass": {
        "group": "arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/groups/${GroupId}"
    },
    "guardduty": {
        "detector": "arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}",
        "filter": "arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/filter/${FilterName}",
        "ipset": "arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/ipset/${IpSetId}",
        "member": "arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/member/${MemberId}",
        "threatintelset": "arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/threatintelset/${ThreatIntelSetId}",
    },
    "health": {
        "event": "arn:${Partition}:health:${Region}:${Account}:event/${EventArn}",
        "health_check": "arn:${Partition}:health:${Region}:${Account}:healthcheck/${HealthCheckId}",
        "organization_event_detail": "arn:${Partition}:health:${Region}:${Account}:event-organization/${EventTypeCode}/${Service}/${EventTypeVersion}/${EventId}",
        "service": "arn:${Partition}:health:${Region}:${Account}:service/${Service}",
    },
    "iam": {
        "access_key": "arn:${Partition}:iam::${Account}:accesskey/${AccessKeyId}",
        "account_alias": "arn:${Partition}:iam::${Account}:alias/${AccountAlias}",
        "group": "arn:${Partition}:iam::${Account}:group/${GroupName}",
        "instance_profile": "arn:${Partition}:iam::${Account}:instance-profile/${InstanceProfileName}",
        "policy": "arn:${Partition}:iam::${Account}:policy/${PolicyName}",
        "role": "arn:${Partition}:iam::${Account}:role/${RoleName}",
        "server_certificate": "arn:${Partition}:iam::${Account}:server-certificate/${ServerCertificateName}",
        "user": "arn:${Partition}:iam::${Account}:user/${UserName}",
        "virtual_mfa_device": "arn:${Partition}:iam::${Account}:mfa/${VirtualMFADeviceName}",
        "group_policy": "arn:${Partition}:iam::${Account}:group/${GroupName}/policy/${PolicyName}",
        "role_policy": "arn:${Partition}:iam::${Account}:role/${RoleName}/policy/${PolicyName}",
        "user_policy": "arn:${Partition}:iam::${Account}:user/${UserName}/policy/${PolicyName}",
    },
    "imagebuilder": {
        "component": "arn:${Partition}:imagebuilder:${Region}:${Account}:component/${ComponentBuildVersionArn}",
        "distribution_configuration": "arn:${Partition}:imagebuilder:${Region}:${Account}:distribution-configuration/${DistributionConfigurationArn}",
        "image": "arn:${Partition}:imagebuilder:${Region}:${Account}:image/${ImageBuildVersionArn}",
        "image_pipeline": "arn:${Partition}:imagebuilder:${Region}:${Account}:image-pipeline/${ImagePipelineArn}",
        "infrastructure_configuration": "arn:${Partition}:imagebuilder:${Region}:${Account}:infrastructure-configuration/${InfrastructureConfigurationArn}",
    },
    "inspector": {
        "assessment_target": "arn:${Partition}:inspector:${Region}:${Account}:target/${AssessmentTargetArn}",
        "assessment_template": "arn:${Partition}:inspector:${Region}:${Account}:template/${AssessmentTemplateArn}",
        "assessment_run": "arn:${Partition}:inspector:${Region}:${Account}:run/${AssessmentRunArn}",
    },
    "iot": {
        "authorizer": "arn:${Partition}:iot:${Region}:${Account}:authorizer/${AuthorizerName}",
        "billing_group": "arn:${Partition}:iot:${Region}:${Account}:billinggroup/${BillingGroupName}",
        "certificate": "arn:${Partition}:iot:${Region}:${Account}:cert/${CertificateId}",
        "dimension": "arn:${Partition}:iot:${Region}:${Account}:dimension/${DimensionName}",
        "policy": "arn:${Partition}:iot:${Region}:${Account}:policy/${PolicyName}",
        "provisioning_template": "arn:${Partition}:iot:${Region}:${Account}:provisioningtemplate/${TemplateName}",
        "rule": "arn:${Partition}:iot:${Region}:${Account}:rule/${RuleName}",
        "scheduled_audit": "arn:${Partition}:iot:${Region}:${Account}:scheduledaudit/${ScheduledAuditName}",
        "thing": "arn:${Partition}:iot:${Region}:${Account}:thing/${ThingName}",
        "thing_group": "arn:${Partition}:iot:${Region}:${Account}:thinggroup/${ThingGroupName}",
        "thing_type": "arn:${Partition}:iot:${Region}:${Account}:thingtype/${ThingTypeName}",
        "topic_rule_destination": "arn:${Partition}:iot:${Region}:${Account}:topic-rule-destination/${TopicRuleDestinationName}",
        "topic_rule": "arn:${Partition}:iot:${Region}:${Account}:rule/${RuleName}",
        "domain_configuration": "arn:${Partition}:iot:${Region}:${Account}:domainconfiguration/${DomainConfigurationName}",
        "fleet_indexing_configuration": "arn:${Partition}:iot:${Region}:${Account}:fleet-indexing-configuration/${IndexingConfigurationName}",
        "job": "arn:${Partition}:iot:${Region}:${Account}:job/${JobId}",
    },
    "iot-device-tester": {
        "test_suite_run": "arn:${Partition}:iot-device-tester:${Region}:${Account}:test-suite-run:${SuiteDefinitionId}/${SuiteRunId}"
    },
    "iot1click": {
        "device": "arn:${Partition}:iot1click:${Region}:${Account}:device/${DeviceId}",
        "placement": "arn:${Partition}:iot1click:${Region}:${Account}:placement/${PlacementName}",
        "project": "arn:${Partition}:iot1click:${Region}:${Account}:project/${ProjectName}",
    },
    "iotanalytics": {
        "channel": "arn:${Partition}:iotanalytics:${Region}:${Account}:channel/${ChannelName}",
        "dataset": "arn:${Partition}:iotanalytics:${Region}:${Account}:dataset/${DatasetName}",
        "datastore": "arn:${Partition}:iotanalytics:${Region}:${Account}:datastore/${DatastoreName}",
        "pipeline": "arn:${Partition}:iotanalytics:${Region}:${Account}:pipeline/${PipelineName}",
    },
    "iotevents": {
        "input": "arn:${Partition}:iotevents:${Region}:${Account}:input/${InputName}",
        "detector_model": "arn:${Partition}:iotevents:${Region}:${Account}:detector-model/${DetectorModelName}",
    },
    "iotsitewise": {
        "asset_model": "arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}",
        "gateway": "arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}",
    },
    "kafka": {
        "cluster": "arn:${Partition}:kafka:${Region}:${Account}:cluster/${ClusterName}"
    },
    "kinesis": {
        "stream": "arn:${Partition}:kinesis:${Region}:${Account}:stream/${StreamName}",
        "firehose_delivery_stream": "arn:${Partition}:firehose:${Region}:${Account}:deliverystream/${DeliveryStreamName}",
    },
    "kinesis-video-archived-media": {
        "archive": "arn:${Partition}:kinesisvideo:${Region}:${Account}:archive/${StreamName}/${ArchiveId}",
        "stream": "arn:${Partition}:kinesisvideo:${Region}:${Account}:stream/${StreamName}/${StreamARN}",
    },
    "kinesis-video-media": {
        "stream": "arn:${Partition}:kinesisvideo:${Region}:${Account}:stream/${StreamName}/${StreamARN}"
    },
    "kinesis-video-signaling": {
        "channel": "arn:${Partition}:kinesisvideo:${Region}:${Account}:channel/${ChannelName}/${ChannelARN}"
    },
    "kms": {
        "key": "arn:${Partition}:kms:${Region}:${Account}:key/${KeyId}",
        "alias": "arn:${Partition}:kms:${Region}:${Account}:alias/${AliasName}",
    },
    "lakeformation": {
        "data_lake_settings": "arn:${Partition}:lakeformation:${Region}:${Account}:datalake/${DataLakeId}/settings",
        "permissions": "arn:${Partition}:lakeformation:${Region}:${Account}:permissions/${DataLakePrincipalId}/${ResourceType}/${ResourceId}",
    },
    "lambda": {
        "function": "arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName}",
        "layer": "arn:${Partition}:lambda:${Region}:${Account}:layer:${LayerName}:${LayerVersion}",
        "event_source_mapping": "arn:${Partition}:lambda:${Region}:${Account}:event-source-mapping:${UUID}",
        "event_invoke_config": "arn:${Partition}:lambda:${Region}:${Account}:event-invoke-config:${UUID}:${FunctionName}",
    },
    "lex": {
        "bot": "arn:${Partition}:lex:${Region}:${Account}:bot:${BotName}",
        "bot_alias": "arn:${Partition}:lex:${Region}:${Account}:bot:${BotName}:alias:${BotAlias}",
        "bot_channel": "arn:${Partition}:lex:${Region}:${Account}:bot-channel:${BotName}:${BotAlias}:${ChannelName}",
    },
    "license-manager": {
        "license_configuration": "arn:${Partition}:license-manager:${Region}:${Account}:license-configuration/${LicenseConfigurationId}"
    },
    "lightsail": {
        "instance": "arn:${Partition}:lightsail:${Region}:${Account}:instance/${InstanceName}",
        "key_pair": "arn:${Partition}:lightsail:${Region}:${Account}:key-pair/${KeyName}",
        "static_ip": "arn:${Partition}:lightsail:${Region}:${Account}:static-ip/${StaticIpName}",
        "load_balancer": "arn:${Partition}:lightsail:${Region}:${Account}:loadbalancer/${LoadBalancerName}",
        "bucket": "arn:${Partition}:lightsail:${Region}:${Account}:bucket/${BucketName}",
    },
    "logs": {
        "log_group": "arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}",
        "log_stream": "arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}",
        "metric_filter": "arn:${Partition}:logs:${Region}:${Account}:metric-filter:${MetricFilterName}",
        "destination": "arn:${Partition}:logs:${Region}:${Account}:destination:${DestinationName}",
        "query_definition": "arn:${Partition}:logs:${Region}:${Account}:query-definition:${QueryDefinitionName}",
    },
    "machinelearning": {
        "batch_prediction": "arn:${Partition}:machinelearning:${Region}:${Account}:batchprediction/${BatchPredictionId}",
        "data_source": "arn:${Partition}:machinelearning:${Region}:${Account}:datasource/${DataSourceId}",
        "evaluation": "arn:${Partition}:machinelearning:${Region}:${Account}:evaluation/${EvaluationId}",
        "ml_model": "arn:${Partition}:machinelearning:${Region}:${Account}:mlmodel/${MLModelId}",
    },
    "macie": {
        "classification_job": "arn:${Partition}:macie:${Region}:${Account}:classification-job/${ClassificationJobId}",
        "custom_data_identifier": "arn:${Partition}:macie:${Region}:${Account}:custom-data-identifier/${CustomDataIdentifierId}",
        "findings_filter": "arn:${Partition}:macie:${Region}:${Account}:findings-filter/${FindingsFilterId}",
        "member_account": "arn:${Partition}:macie:${Region}:${Account}:member-account/${MemberAccountId}",
        "s3_object": "arn:${Partition}:macie:${Region}:${Account}:s3-object/${S3BucketName}/${S3ObjectKey}",
    },
    "managedblockchain": {
        "network": "arn:${Partition}:managedblockchain:${Region}:${Account}:network/${NetworkId}",
        "node": "arn:${Partition}:managedblockchain:${Region}:${Account}:node/${NetworkId}/${MemberId}/${NodeId}",
        "proposal": "arn:${Partition}:managedblockchain:${Region}:${Account}:proposal/${NetworkId}/${ProposalId}",
    },
    "mediaconnect": {
        "flow": "arn:${Partition}:mediaconnect:${Region}:${Account}:flow/${FlowArn}"
    },
    "mediaconvert": {
        "queue": "arn:${Partition}:mediaconvert:${Region}:${Account}:queue/${QueueName}",
        "preset": "arn:${Partition}:mediaconvert:${Region}:${Account}:preset/${PresetName}",
        "job_template": "arn:${Partition}:mediaconvert:${Region}:${Account}:jobTemplate/${JobTemplateName}",
    },
    "medialive": {
        "channel": "arn:${Partition}:medialive:${Region}:${Account}:channel:${ChannelId}"
    },
    "mediapackage": {
        "channel": "arn:${Partition}:mediapackage:${Region}:${Account}:channel/${ChannelId}",
        "origin_endpoint": "arn:${Partition}:mediapackage:${Region}:${Account}:origin_endpoint/${OriginEndpointId}",
    },
    "mediastore": {
        "container": "arn:${Partition}:mediastore:${Region}:${Account}:container/${ContainerName}"
    },
    "mediastore-data": {
        "object": "arn:${Partition}:mediastore-data:${Region}:${Account}:object/${Path}"
    },
    "meteringmarketplace": {
        "product": "arn:${Partition}:meteringmarketplace:${Region}:${Account}:product/${ProductCode}",
        "usage_record": "arn:${Partition}:meteringmarketplace:${Region}:${Account}:usage-record:${ProductCode}/${Timestamp}/${CustomerIdentifier}",
    },
    "mgh": {
        "home_region_control": "arn:${Partition}:mgh:${Region}:${Account}:homeRegionControl/${HomeRegionControlId}",
        "migration_task": "arn:${Partition}:mgh:${Region}:${Account}:migrationTask/${MigrationTaskName}",
        "progress_update_stream": "arn:${Partition}:mgh:${Region}:${Account}:progressUpdateStream/${ProgressUpdateStreamName}",
    },
    "mobilehub": {
        "project": "arn:${Partition}:mobilehub:${Region}:${Account}:project/${ProjectId}"
    },
    "mq": {
        "broker": "arn:${Partition}:mq:${Region}:${Account}:broker:${BrokerId}",
        "configuration": "arn:${Partition}:mq:${Region}:${Account}:configuration:${ConfigurationId}",
    },
    "mturk": {
        "hit_type": "arn:${Partition}:mturk:${Region}:${Account}:hittype/${HITTypeId}",
        "hit": "arn:${Partition}:mturk:${Region}:${Account}:hit/${HITId}",
        "qualification_type": "arn:${Partition}:mturk:${Region}:${Account}:qualificationtype/${QualificationTypeId}",
    },
    "neptune-db": {
        "cluster": "arn:${Partition}:neptune-db:${Region}:${Account}:cluster:${ClusterResourceId}"
    },
    "network-firewall": {
        "firewall_policy": "arn:${Partition}:network-firewall:${Region}:${Account}:policy/${FirewallPolicyName}",
        "firewall": "arn:${Partition}:network-firewall:${Region}:${Account}:firewall/${FirewallName}",
        "rule_group": "arn:${Partition}:network-firewall:${Region}:${Account}:rulegroup/${RuleGroupName}",
    },
    "networkmanager": {
        "global_network": "arn:${Partition}:networkmanager:${Region}:${Account}:global-network/${GlobalNetworkId}",
        "device": "arn:${Partition}:networkmanager:${Region}:${Account}:device/${DeviceId}",
        "link": "arn:${Partition}:networkmanager:${Region}:${Account}:link/${LinkId}",
        "site": "arn:${Partition}:networkmanager:${Region}:${Account}:site/${SiteId}",
    },
    "opsworks": {
        "stack": "arn:${Partition}:opsworks:${Region}:${Account}:stack/${StackId}",
        "layer": "arn:${Partition}:opsworks:${Region}:${Account}:layer/${LayerId}",
        "app": "arn:${Partition}:opsworks:${Region}:${Account}:app/${AppId}",
        "instance": "arn:${Partition}:opsworks:${Region}:${Account}:instance/${InstanceId}",
        "user_profile": "arn:${Partition}:opsworks:${Region}:${Account}:user-profile/${UserProfileId}",
        "permission": "arn:${Partition}:opsworks:${Region}:${Account}:permission/${PermissionId}",
        "deployment": "arn:${Partition}:opsworks:${Region}:${Account}:deployment/${DeploymentId}",
    },
    "organizations": {
        "organization": "arn:${Partition}:organizations::${Account}:organization/${OrganizationId}",
        "account": "arn:${Partition}:organizations::${Account}:account/${AccountId}",
        "organizational_unit": "arn:${Partition}:organizations::${Account}:ou/${OrganizationalUnitId}",
    },
    "outposts": {
        "outpost": "arn:${Partition}:outposts:${Region}:${Account}:outpost/${OutpostId}"
    },
    "personalize": {
        "dataset_group": "arn:${Partition}:personalize:${Region}:${Account}:dataset-group/${DatasetGroupId}",
        "dataset": "arn:${Partition}:personalize:${Region}:${Account}:dataset/${DatasetGroupArn}/dataset/${DatasetArn}",
        "solution": "arn:${Partition}:personalize:${Region}:${Account}:solution/${SolutionArn}",
        "campaign": "arn:${Partition}:personalize:${Region}:${Account}:campaign/${CampaignArn}",
        "event_tracker": "arn:${Partition}:personalize:${Region}:${Account}:event-tracker/${EventTrackerArn}",
    },
    "pi": {
        "dimension": "arn:${Partition}:pi:${Region}:${Account}:dimension:${DimensionName}"
    },
    "pinpoint": {
        "app": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}",
        "adm_channel": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}/channels/adm",
        "apns_channel": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}/channels/apns",
        "apns_sandbox_channel": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}/channels/apns_sandbox",
        "baidu_channel": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}/channels/baidu",
        "email_channel": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}/channels/email",
        "gcm_channel": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}/channels/gcm",
        "sms_channel": "arn:${Partition}:mobiletargeting:${Region}:${Account}:apps/${ApplicationId}/channels/sms}",
    },
    "polly": {
        "lexicon": "arn:${Partition}:polly:${Region}:${Account}:lexicon/${LexiconName}"
    },
    "qldb": {
        "ledger": "arn:${Partition}:qldb:${Region}:${Account}:ledger/${LedgerName}"
    },
    "quickSight": {
        "group": "arn:${Partition}:quicksight:${Region}:${Account}:group/${GroupName}",
        "user": "arn:${Partition}:quicksight:${Region}:${Account}:user/${UserName}",
    },
    "ram": {
        "resource_share": "arn:${Partition}:ram:${Region}:${Account}:resource-share/${ResourceShareName}",
        "resource_share_invitation": "arn:${Partition}:ram:${Region}:${Account}:resource-share-invitation/${ResourceShareInvitationId}",
    },
    "rds": {
        "db_instance": "arn:${Partition}:rds:${Region}:${Account}:db:${DBInstanceIdentifier}",
        "db_snapshot": "arn:${Partition}:rds:${Region}:${Account}:snapshot:${DBSnapshotIdentifier}",
        "db_cluster": "arn:${Partition}:rds:${Region}:${Account}:cluster:${DBClusterIdentifier}",
        "db_cluster_snapshot": "arn:${Partition}:rds:${Region}:${Account}:cluster-snapshot:${DBClusterSnapshotIdentifier}",
        "option_group": "arn:${Partition}:rds:${Region}:${Account}:og:${OptionGroupName}",
        "parameter_group": "arn:${Partition}:rds:${Region}:${Account}:pg:${DBParameterGroupName}",
        "subgroup": "arn:${Partition}:rds:${Region}:${Account}:sub-group:${DBSubnetGroupName}",
        "event_subscription": "arn:${Partition}:rds:${Region}:${Account}:es:${EventSubscriptionName}",
        "global_cluster": "arn:${Partition}:rds:${Region}:${Account}:global-cluster:${GlobalClusterIdentifier}",
    },
    "rds-data": {
        "secret": "arn:${Partition}:secretsmanager:${Region}:${Account}:secret:${SecretId}"
    },
    "redshift": {
        "cluster": "arn:${Partition}:redshift:${Region}:${Account}:cluster:${ClusterName}",
        "snapshot": "arn:${Partition}:redshift:${Region}:${Account}:snapshot:${SnapshotName}",
    },
    "rekognition": {
        "collection": "arn:${Partition}:rekognition:${Region}:${Account}:collection/${CollectionId}",
        "stream_processor": "arn:${Partition}:rekognition:${Region}:${Account}:stream-processor/${StreamProcessorName}",
    },
    "resource-groups": {
        "group": "arn:${Partition}:resource-groups:${Region}:${Account}:group/${GroupName}"
    },
    "robomaker": {
        "robot_application": "arn:${Partition}:robomaker:${Region}:${Account}:robot-application/${ApplicationName}/${ApplicationVersion}",
        "simulation_application": "arn:${Partition}:robomaker:${Region}:${Account}:simulation-application/${ApplicationName}/${ApplicationVersion}",
        "robot": "arn:${Partition}:robomaker:${Region}:${Account}:robot/${RobotName}",
        "simulation_job": "arn:${Partition}:robomaker:${Region}:${Account}:simulation-job/${SimulationJobArn}",
        "fleet": "arn:${Partition}:robomaker:${Region}:${Account}:fleet/${FleetName}",
    },
    "route53": {
        "health_check": "arn:${Partition}:route53:::healthcheck/${HealthCheckId}",
        "hosted_zone": "arn:${Partition}:route53:::hostedzone/${HostedZoneId}",
        "vpc_association_authorization": "arn:${Partition}:route53:::vpc/${VPCRegion}:${VPCId}:authorizevpcassociation/${HostedZoneId}/${VPCId}",
        "resolver_endpoint": "arn:${Partition}:route53resolver:${Region}:${Account}:resolver-endpoint/${ResolverEndpointId}",
        "resolver_rule": "arn:${Partition}:route53resolver:${Region}:${Account}:resolver-rule/${ResolverRuleId}",
        "resolver_rule_association": "arn:${Partition}:route53resolver:${Region}:${Account}:resolver-rule-association/${ResolverRuleAssociationId}",
    },
    "s3": {
        "bucket": "arn:${Partition}:s3:::${BucketName}",
        "object": "arn:${Partition}:s3:::${BucketName}/${ObjectName}",
    },
    "s3-object-lambda": {
        "access_point": "arn:${Partition}:s3-object-lambda:${Region}:${Account}:accesspoint/${AccessPointName}",
        "access_point_policy": "arn:${Partition}:s3-object-lambda:${Region}:${Account}:accesspoint-policy/${AccessPointName}",
        "access_point_configuration": "arn:${Partition}:s3-object-lambda:${Region}:${Account}:accesspoint/${AccessPointName}/configuration",
    },
    "sagemaker": {
        "notebook_instance": "arn:${Partition}:sagemaker:${Region}:${Account}:notebook-instance/${NotebookInstanceName}",
        "notebook_instance_lifecycle_configuration": "arn:${Partition}:sagemaker:${Region}:${Account}:notebook-instance-lifecycle-config/${NotebookInstanceLifecycleConfigName}",
        "training_job": "arn:${Partition}:sagemaker:${Region}:${Account}:training-job/${TrainingJobName}",
        "processing_job": "arn:${Partition}:sagemaker:${Region}:${Account}:processing-job/${ProcessingJobName}",
        "transform_job": "arn:${Partition}:sagemaker:${Region}:${Account}:transform-job/${TransformJobName}",
        "model": "arn:${Partition}:sagemaker:${Region}:${Account}:model/${ModelName}",
        "endpoint_config": "arn:${Partition}:sagemaker:${Region}:${Account}:endpoint-config/${EndpointConfigName}",
        "endpoint": "arn:${Partition}:sagemaker:${Region}:${Account}:endpoint/${EndpointName}",
        "feature_group": "arn:${Partition}:sagemaker:${Region}:${Account}:feature-group/${FeatureGroupName}",
    },
    "sdb": {"domain": "arn:${Partition}:sdb:${Region}:${Account}:domain/${DomainName}"},
    "secretsmanager": {
        "secret": "arn:${Partition}:secretsmanager:${Region}:${Account}:secret:${SecretId}"
    },
    "securityhub": {
        "hub": "arn:${Partition}:securityhub:${Region}:${Account}:hub/default",
        "product_subscription": "arn:${Partition}:securityhub:${Region}:${Account}:subscription/${SubscriptionId}",
    },
    "serverlessrepo": {
        "application": "arn:${Partition}:serverlessrepo:${Region}:${Account}:applications/${ApplicationId}/${SemanticVersion}"
    },
    "servicecatalog": {
        "product": "arn:${Partition}:catalog:${Region}:${Account}:product/${ProductId}",
        "portfolio": "arn:${Partition}:catalog:${Region}:${Account}:portfolio/${PortfolioId}",
        "portfolio_share": "arn:${Partition}:catalog:${Region}:${Account}:share/${ShareId}",
        "cloudformation_stack_set_constraint": "arn:${Partition}:cloudformation:${Region}:${Account}:stack-set/${StackSetName}:constraint/${ConstraintId}",
    },
    "servicediscovery": {
        "namespace": "arn:${Partition}:servicediscovery:${Region}:${Account}:namespace/${NamespaceId}",
        "service": "arn:${Partition}:servicediscovery:${Region}:${Account}:service/${ServiceId}",
    },
    "ses": {
        "configuration_set": "arn:${Partition}:ses:${Region}:${Account}:configuration-set/${ConfigurationSetName}"
    },
    "shield": {
        "protection": "arn:${Partition}:shield::${Account}:protection/${ProtectionId}"
    },
    "signer": {
        "signing_profile": "arn:${Partition}:signer:${Region}:${Account}:signing-profiles/${SigningProfileName}"
    },
    "sms": {
        "app": "arn:${Partition}:sms:${Region}:${Account}:app/${AppId}",
        "server": "arn:${Partition}:sms:${Region}:${Account}:server/${ServerId}",
        "replication_job": "arn:${Partition}:sms:${Region}:${Account}:replication-job/${ReplicationJobId}",
    },
    "snowball": {"job": "arn:${Partition}:snowball:${Region}:${Account}:job/${JobId}"},
    "sns": {
        "topic": "arn:${Partition}:sns:${Region}:${Account}:${TopicName}",
        "subscription": "arn:${Partition}:sns:${Region}:${Account}:${TopicName}:${SubscriptionId}",
        "platform_application_endpoint": "arn:${Partition}:sns:${Region}:${Account}:app/${PlatformApplicationArn}/${EndpointId}",
    },
    "sqs": {"queue": "arn:${Partition}:sqs:${Region}:${Account}:${QueueName}"},
    "ssm": {
        "document": "arn:${Partition}:ssm:${Region}:${Account}:document/${DocumentName}",
        "parameter": "arn:${Partition}:ssm:${Region}:${Account}:parameter/${ParameterName}",
        "maintenance_window": "arn:${Partition}:ssm:${Region}:${Account}:maintenancewindow/${WindowId}",
        "maintenance_window_task": "arn:${Partition}:ssm:${Region}:${Account}:maintenancewindow/${WindowId}/task/${WindowTaskId}",
        "patch_baseline": "arn:${Partition}:ssm:${Region}:${Account}:patchbaseline/${BaselineId}",
    },
    "sso": {
        "instance": "arn:${Partition}:sso:${Region}:${Account}:instance/${InstanceId}",
        "permission_set": "arn:${Partition}:sso:${Region}:${Account}:permissionSet/${PermissionSetId}",
    },
    "sso-directory": {
        "directory": "arn:${Partition}:sso-directory:${Region}:${Account}:directory/${DirectoryId}"
    },
    "stepfunctions": {
        "state_machine": "arn:${Partition}:states:${Region}:${Account}:stateMachine:${StateMachineName}"
    },
    "storagegateway": {
        "gateway": "arn:${Partition}:storagegateway:${Region}:${Account}:gateway/${GatewayId}",
        "share": "arn:${Partition}:storagegateway:${Region}:${Account}:share/${ShareId}",
        "tape": "arn:${Partition}:storagegateway:${Region}:${Account}:tape/${TapeARN}",
        "volume": "arn:${Partition}:storagegateway:${Region}:${Account}:gateway/${GatewayId}/volume/${VolumeId}",
    },
    "sts": {
        "assumed_role": "arn:${Partition}:sts::${Account}:assumed-role/${RoleName}/${RoleSessionName}",
        "federated_user": "arn:${Partition}:sts::${Account}:federated-user/${UserName}",
        "oidc_provider": "arn:${Partition}:iam::${Account}:oidc-provider/${Url}",
        "saml_provider": "arn:${Partition}:iam::${Account}:saml-provider/${Name}",
        "user": "arn:${Partition}:iam::${Account}:user/${UserName}",
    },
    "swf": {
        "domain": "arn:${Partition}:swf:${Region}:${Account}:domain/${DomainName}",
        "workflow_type": "arn:${Partition}:swf:${Region}:${Account}:workflowType/${DomainName}/${WorkflowTypeName}",
        "activity_type": "arn:${Partition}:swf:${Region}:${Account}:activityType/${DomainName}/${ActivityTypeName}",
        "workflow_execution": "arn:${Partition}:swf:${Region}:${Account}:workflow/${DomainName}/${WorkflowExecutionType}:${WorkflowExecutionId}",
        "activity_execution": "arn:${Partition}:swf:${Region}:${Account}:activity/${DomainName}/${ActivityTypeName}:${ActivityId}",
    },
    "synthetics": {
        "canary": "arn:${Partition}:synthetics:${Region}:${Account}:canary:${CanaryName}",
        "canary_run": "arn:${Partition}:synthetics:${Region}:${Account}:canary:${CanaryName}:run:${CanaryRunId}",
    },
    "textract": {
        "document": "arn:${Partition}:textract:${Region}:${Account}:document/${DocumentId}"
    },
    "transcribe": {
        "vocabulary": "arn:${Partition}:transcribe:${Region}:${Account}:vocabulary/${VocabularyName}"
    },
    "transfer": {
        "server": "arn:${Partition}:transfer:${Region}:${Account}:server/${ServerId}",
        "user": "arn:${Partition}:transfer:${Region}:${Account}:user/${ServerId}/${UserName}",
        "role": "arn:${Partition}:iam::${Account}:role/service-role/${RoleName}",
    },
    "translate": {
        "terminology": "arn:${Partition}:translate:${Region}:${Account}:terminology/${TerminologyName}"
    },
    "waf": {
        "ipset": "arn:${Partition}:waf:${Region}:${Account}:ipset/${IpSetId}",
        "rule": "arn:${Partition}:waf:${Region}:${Account}:rule/${RuleId}",
        "web_acl": "arn:${Partition}:waf:${Region}:${Account}:webacl/${WebACLId}",
        "regional_rule_group": "arn:${Partition}:waf::${Account}:regional-rulegroup/${RuleGroupName}/${RuleGroupId}",
        "regional_web_acl": "arn:${Partition}:waf::${Account}:webacl/${WebACLName}/${WebACLId}",
        "global_web_acl": "arn:${Partition}:waf::${Account}:global-webacl/${WebACLName}/${WebACLId}",
    },
    "waf-regional": {
        "ipset": "arn:${Partition}:waf-regional:${Region}:${Account}:ipset/${IpSetId}",
        "rule": "arn:${Partition}:waf-regional:${Region}:${Account}:rule/${RuleId}",
        "web_acl": "arn:${Partition}:waf-regional:${Region}:${Account}:webacl/${WebACLId}",
        "regional_rule_group": "arn:${Partition}:waf-regional:${Region}:${Account}:rulegroup/${RuleGroupName}/${RuleGroupId}",
        "regional_web_acl": "arn:${Partition}:waf-regional:${Region}:${Account}:webacl/${WebACLName}/${WebACLId}",
    },
    "wafv2": {
        "ip_set": "arn:${Partition}:wafv2:${Region}:${Account}:/ipset/${Scope}/${Id}",
        "rule_group": "arn:${Partition}:wafv2:${Region}:${Account}:/rulegroup/${Scope}/${Id}",
        "web_acl": "arn:${Partition}:wafv2:${Region}:${Account}:/webacl/${Scope}/${Id}",
    },
    "wellarchitected": {
        "workload": "arn:${Partition}:wellarchitected:${Region}:${Account}:workload/${WorkloadId}"
    },
    "workdocs": {
        "document": "arn:${Partition}:workdocs:${Region}:${Account}:${FolderHierarchy}/${DocumentName}",
        "folder": "arn:${Partition}:workdocs:${Region}:${Account}:${FolderHierarchy}/${FolderName}",
        "user": "arn:${Partition}:workdocs:${Region}:${Account}:user/${UserId}",
    },
    "worklink": {
        "fleet": "arn:${Partition}:worklink:${Region}:${Account}:fleet/${FleetArnName}",
        "website_certificate_authority_association": "arn:${Partition}:worklink:${Region}:${Account}:website-certificate-authority-association/${WebsiteCertificateAuthorityAssociationId}",
    },
    "workmail": {
        "organization": "arn:${Partition}:workmail:${Region}:${Account}:organization/${OrganizationId}",
        "resource": "arn:${Partition}:workmail:${Region}:${Account}:resource/${ResourceId}",
        "user": "arn:${Partition}:workmail:${Region}:${Account}:user/${UserId}",
    },
    "workspaces": {
        "directory": "arn:${Partition}:workspaces:${Region}:${Account}:directory/${DirectoryId}",
        "workspace": "arn:${Partition}:workspaces:${Region}:${Account}:workspace/${WorkspaceId}",
    },
}