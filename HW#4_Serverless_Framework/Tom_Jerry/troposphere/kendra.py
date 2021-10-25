# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class ConfluenceAttachmentToIndexFieldMapping(AWSProperty):
    props = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluenceAttachmentFieldMappingsList(AWSProperty):
    props = {
        "ConfluenceAttachmentFieldMappingsList": (
            [ConfluenceAttachmentToIndexFieldMapping],
            False,
        ),
    }


class ConfluenceAttachmentConfiguration(AWSProperty):
    props = {
        "AttachmentFieldMappings": (ConfluenceAttachmentFieldMappingsList, False),
        "CrawlAttachments": (boolean, False),
    }


class ConfluenceBlogToIndexFieldMapping(AWSProperty):
    props = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluenceBlogFieldMappingsList(AWSProperty):
    props = {
        "ConfluenceBlogFieldMappingsList": ([ConfluenceBlogToIndexFieldMapping], False),
    }


class ConfluenceBlogConfiguration(AWSProperty):
    props = {
        "BlogFieldMappings": (ConfluenceBlogFieldMappingsList, False),
    }


class ConfluencePageToIndexFieldMapping(AWSProperty):
    props = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluencePageFieldMappingsList(AWSProperty):
    props = {
        "ConfluencePageFieldMappingsList": ([ConfluencePageToIndexFieldMapping], False),
    }


class ConfluencePageConfiguration(AWSProperty):
    props = {
        "PageFieldMappings": (ConfluencePageFieldMappingsList, False),
    }


class ConfluenceSpaceToIndexFieldMapping(AWSProperty):
    props = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluenceSpaceFieldMappingsList(AWSProperty):
    props = {
        "ConfluenceSpaceFieldMappingsList": (
            [ConfluenceSpaceToIndexFieldMapping],
            False,
        ),
    }


class ConfluenceSpaceList(AWSProperty):
    props = {
        "ConfluenceSpaceList": ([str], False),
    }


class ConfluenceSpaceConfiguration(AWSProperty):
    props = {
        "CrawlArchivedSpaces": (boolean, False),
        "CrawlPersonalSpaces": (boolean, False),
        "ExcludeSpaces": (ConfluenceSpaceList, False),
        "IncludeSpaces": (ConfluenceSpaceList, False),
        "SpaceFieldMappings": (ConfluenceSpaceFieldMappingsList, False),
    }


class DataSourceInclusionsExclusionsStrings(AWSProperty):
    props = {
        "DataSourceInclusionsExclusionsStrings": ([str], False),
    }


class DataSourceVpcConfiguration(AWSProperty):
    props = {
        "SecurityGroupIds": ([str], True),
        "SubnetIds": ([str], True),
    }


class ConfluenceConfiguration(AWSProperty):
    props = {
        "AttachmentConfiguration": (ConfluenceAttachmentConfiguration, False),
        "BlogConfiguration": (ConfluenceBlogConfiguration, False),
        "ExclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "InclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "PageConfiguration": (ConfluencePageConfiguration, False),
        "SecretArn": (str, True),
        "ServerUrl": (str, True),
        "SpaceConfiguration": (ConfluenceSpaceConfiguration, False),
        "Version": (str, True),
        "VpcConfiguration": (DataSourceVpcConfiguration, False),
    }


class AclConfiguration(AWSProperty):
    props = {
        "AllowedGroupsColumnName": (str, True),
    }


class ChangeDetectingColumns(AWSProperty):
    props = {
        "ChangeDetectingColumns": ([str], False),
    }


class DataSourceToIndexFieldMapping(AWSProperty):
    props = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class DataSourceToIndexFieldMappingList(AWSProperty):
    props = {
        "DataSourceToIndexFieldMappingList": ([DataSourceToIndexFieldMapping], False),
    }


class ColumnConfiguration(AWSProperty):
    props = {
        "ChangeDetectingColumns": (ChangeDetectingColumns, True),
        "DocumentDataColumnName": (str, True),
        "DocumentIdColumnName": (str, True),
        "DocumentTitleColumnName": (str, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
    }


class ConnectionConfiguration(AWSProperty):
    props = {
        "DatabaseHost": (str, True),
        "DatabaseName": (str, True),
        "DatabasePort": (integer, True),
        "SecretArn": (str, True),
        "TableName": (str, True),
    }


class SqlConfiguration(AWSProperty):
    props = {
        "QueryIdentifiersEnclosingOption": (str, False),
    }


class DatabaseConfiguration(AWSProperty):
    props = {
        "AclConfiguration": (AclConfiguration, False),
        "ColumnConfiguration": (ColumnConfiguration, True),
        "ConnectionConfiguration": (ConnectionConfiguration, True),
        "DatabaseEngineType": (str, True),
        "SqlConfiguration": (SqlConfiguration, False),
        "VpcConfiguration": (DataSourceVpcConfiguration, False),
    }


class ExcludeMimeTypesList(AWSProperty):
    props = {
        "ExcludeMimeTypesList": ([str], False),
    }


class ExcludeSharedDrivesList(AWSProperty):
    props = {
        "ExcludeSharedDrivesList": ([str], False),
    }


class ExcludeUserAccountsList(AWSProperty):
    props = {
        "ExcludeUserAccountsList": ([str], False),
    }


class GoogleDriveConfiguration(AWSProperty):
    props = {
        "ExcludeMimeTypes": (ExcludeMimeTypesList, False),
        "ExcludeSharedDrives": (ExcludeSharedDrivesList, False),
        "ExcludeUserAccounts": (ExcludeUserAccountsList, False),
        "ExclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "InclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "SecretArn": (str, True),
    }


class OneDriveUserList(AWSProperty):
    props = {
        "OneDriveUserList": ([str], False),
    }


class S3Path(AWSProperty):
    props = {
        "Bucket": (str, True),
        "Key": (str, True),
    }


class OneDriveUsers(AWSProperty):
    props = {
        "OneDriveUserList": (OneDriveUserList, False),
        "OneDriveUserS3Path": (S3Path, False),
    }


class OneDriveConfiguration(AWSProperty):
    props = {
        "DisableLocalGroups": (boolean, False),
        "ExclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "InclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "OneDriveUsers": (OneDriveUsers, True),
        "SecretArn": (str, True),
        "TenantDomain": (str, True),
    }


class AccessControlListConfiguration(AWSProperty):
    props = {
        "KeyPath": (str, False),
    }


class DocumentsMetadataConfiguration(AWSProperty):
    props = {
        "S3Prefix": (str, False),
    }


class S3DataSourceConfiguration(AWSProperty):
    props = {
        "AccessControlListConfiguration": (AccessControlListConfiguration, False),
        "BucketName": (str, True),
        "DocumentsMetadataConfiguration": (DocumentsMetadataConfiguration, False),
        "ExclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "InclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "InclusionPrefixes": (DataSourceInclusionsExclusionsStrings, False),
    }


class SalesforceChatterFeedIncludeFilterTypes(AWSProperty):
    props = {
        "SalesforceChatterFeedIncludeFilterTypes": ([str], False),
    }


class SalesforceChatterFeedConfiguration(AWSProperty):
    props = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "IncludeFilterTypes": (SalesforceChatterFeedIncludeFilterTypes, False),
    }


class SalesforceCustomKnowledgeArticleTypeConfiguration(AWSProperty):
    props = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "Name": (str, True),
    }


class SalesforceCustomKnowledgeArticleTypeConfigurationList(AWSProperty):
    props = {
        "SalesforceCustomKnowledgeArticleTypeConfigurationList": (
            [SalesforceCustomKnowledgeArticleTypeConfiguration],
            False,
        ),
    }


class SalesforceKnowledgeArticleStateList(AWSProperty):
    props = {
        "SalesforceKnowledgeArticleStateList": ([str], False),
    }


class SalesforceStandardKnowledgeArticleTypeConfiguration(AWSProperty):
    props = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
    }


class SalesforceKnowledgeArticleConfiguration(AWSProperty):
    props = {
        "CustomKnowledgeArticleTypeConfigurations": (
            SalesforceCustomKnowledgeArticleTypeConfigurationList,
            False,
        ),
        "IncludedStates": (SalesforceKnowledgeArticleStateList, True),
        "StandardKnowledgeArticleTypeConfiguration": (
            SalesforceStandardKnowledgeArticleTypeConfiguration,
            False,
        ),
    }


class SalesforceStandardObjectAttachmentConfiguration(AWSProperty):
    props = {
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
    }


class SalesforceStandardObjectConfiguration(AWSProperty):
    props = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "Name": (str, True),
    }


class SalesforceStandardObjectConfigurationList(AWSProperty):
    props = {
        "SalesforceStandardObjectConfigurationList": (
            [SalesforceStandardObjectConfiguration],
            False,
        ),
    }


class SalesforceConfiguration(AWSProperty):
    props = {
        "ChatterFeedConfiguration": (SalesforceChatterFeedConfiguration, False),
        "CrawlAttachments": (boolean, False),
        "ExcludeAttachmentFilePatterns": (DataSourceInclusionsExclusionsStrings, False),
        "IncludeAttachmentFilePatterns": (DataSourceInclusionsExclusionsStrings, False),
        "KnowledgeArticleConfiguration": (
            SalesforceKnowledgeArticleConfiguration,
            False,
        ),
        "SecretArn": (str, True),
        "ServerUrl": (str, True),
        "StandardObjectAttachmentConfiguration": (
            SalesforceStandardObjectAttachmentConfiguration,
            False,
        ),
        "StandardObjectConfigurations": (
            SalesforceStandardObjectConfigurationList,
            False,
        ),
    }


class ServiceNowKnowledgeArticleConfiguration(AWSProperty):
    props = {
        "CrawlAttachments": (boolean, False),
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "ExcludeAttachmentFilePatterns": (DataSourceInclusionsExclusionsStrings, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "IncludeAttachmentFilePatterns": (DataSourceInclusionsExclusionsStrings, False),
    }


class ServiceNowServiceCatalogConfiguration(AWSProperty):
    props = {
        "CrawlAttachments": (boolean, False),
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "ExcludeAttachmentFilePatterns": (DataSourceInclusionsExclusionsStrings, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "IncludeAttachmentFilePatterns": (DataSourceInclusionsExclusionsStrings, False),
    }


class ServiceNowConfiguration(AWSProperty):
    props = {
        "HostUrl": (str, True),
        "KnowledgeArticleConfiguration": (
            ServiceNowKnowledgeArticleConfiguration,
            False,
        ),
        "SecretArn": (str, True),
        "ServiceCatalogConfiguration": (ServiceNowServiceCatalogConfiguration, False),
        "ServiceNowBuildVersion": (str, True),
    }


class SharePointConfiguration(AWSProperty):
    props = {
        "CrawlAttachments": (boolean, False),
        "DisableLocalGroups": (boolean, False),
        "DocumentTitleFieldName": (str, False),
        "ExclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "FieldMappings": (DataSourceToIndexFieldMappingList, False),
        "InclusionPatterns": (DataSourceInclusionsExclusionsStrings, False),
        "SecretArn": (str, True),
        "SharePointVersion": (str, True),
        "Urls": ([str], True),
        "UseChangeLog": (boolean, False),
        "VpcConfiguration": (DataSourceVpcConfiguration, False),
    }


class DataSourceConfiguration(AWSProperty):
    props = {
        "ConfluenceConfiguration": (ConfluenceConfiguration, False),
        "DatabaseConfiguration": (DatabaseConfiguration, False),
        "GoogleDriveConfiguration": (GoogleDriveConfiguration, False),
        "OneDriveConfiguration": (OneDriveConfiguration, False),
        "S3Configuration": (S3DataSourceConfiguration, False),
        "SalesforceConfiguration": (SalesforceConfiguration, False),
        "ServiceNowConfiguration": (ServiceNowConfiguration, False),
        "SharePointConfiguration": (SharePointConfiguration, False),
    }


class DataSource(AWSObject):
    resource_type = "AWS::Kendra::DataSource"

    props = {
        "DataSourceConfiguration": (DataSourceConfiguration, False),
        "Description": (str, False),
        "IndexId": (str, True),
        "Name": (str, True),
        "RoleArn": (str, False),
        "Schedule": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class Faq(AWSObject):
    resource_type = "AWS::Kendra::Faq"

    props = {
        "Description": (str, False),
        "FileFormat": (str, False),
        "IndexId": (str, True),
        "Name": (str, True),
        "RoleArn": (str, True),
        "S3Path": (S3Path, True),
        "Tags": (Tags, False),
    }


class CapacityUnitsConfiguration(AWSProperty):
    props = {
        "QueryCapacityUnits": (integer, True),
        "StorageCapacityUnits": (integer, True),
    }


class ValueImportanceItem(AWSProperty):
    props = {
        "Key": (str, False),
        "Value": (integer, False),
    }


class ValueImportanceItems(AWSProperty):
    props = {
        "ValueImportanceItems": ([ValueImportanceItem], False),
    }


class Relevance(AWSProperty):
    props = {
        "Duration": (str, False),
        "Freshness": (boolean, False),
        "Importance": (integer, False),
        "RankOrder": (str, False),
        "ValueImportanceItems": (ValueImportanceItems, False),
    }


class Search(AWSProperty):
    props = {
        "Displayable": (boolean, False),
        "Facetable": (boolean, False),
        "Searchable": (boolean, False),
        "Sortable": (boolean, False),
    }


class DocumentMetadataConfiguration(AWSProperty):
    props = {
        "Name": (str, True),
        "Relevance": (Relevance, False),
        "Search": (Search, False),
        "Type": (str, True),
    }


class ServerSideEncryptionConfiguration(AWSProperty):
    props = {
        "KmsKeyId": (str, False),
    }


class JsonTokenTypeConfiguration(AWSProperty):
    props = {
        "GroupAttributeField": (str, True),
        "UserNameAttributeField": (str, True),
    }


class JwtTokenTypeConfiguration(AWSProperty):
    props = {
        "ClaimRegex": (str, False),
        "GroupAttributeField": (str, False),
        "Issuer": (str, False),
        "KeyLocation": (str, True),
        "SecretManagerArn": (str, False),
        "URL": (str, False),
        "UserNameAttributeField": (str, False),
    }


class UserTokenConfiguration(AWSProperty):
    props = {
        "JsonTokenTypeConfiguration": (JsonTokenTypeConfiguration, False),
        "JwtTokenTypeConfiguration": (JwtTokenTypeConfiguration, False),
    }


class Index(AWSObject):
    resource_type = "AWS::Kendra::Index"

    props = {
        "CapacityUnits": (CapacityUnitsConfiguration, False),
        "Description": (str, False),
        "DocumentMetadataConfigurations": ([DocumentMetadataConfiguration], False),
        "Edition": (str, True),
        "Name": (str, True),
        "RoleArn": (str, True),
        "ServerSideEncryptionConfiguration": (ServerSideEncryptionConfiguration, False),
        "Tags": (Tags, False),
        "UserContextPolicy": (str, False),
        "UserTokenConfigurations": ([UserTokenConfiguration], False),
    }