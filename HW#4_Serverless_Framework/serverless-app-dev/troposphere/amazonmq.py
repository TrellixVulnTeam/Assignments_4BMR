# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 18.7.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class ConfigurationId(AWSProperty):
    props = {
        "Id": (str, True),
        "Revision": (integer, True),
    }


class EncryptionOptions(AWSProperty):
    props = {
        "KmsKeyId": (str, False),
        "UseAwsOwnedKey": (boolean, True),
    }


class InterBrokerCred(AWSProperty):
    props = {
        "Password": (str, True),
        "Username": (str, True),
    }


class ServerMetadata(AWSProperty):
    props = {
        "Hosts": ([str], True),
        "RoleBase": (str, True),
        "RoleName": (str, False),
        "RoleSearchMatching": (str, True),
        "RoleSearchSubtree": (boolean, False),
        "ServiceAccountPassword": (str, True),
        "ServiceAccountUsername": (str, True),
        "UserBase": (str, True),
        "UserRoleName": (str, False),
        "UserSearchMatching": (str, True),
        "UserSearchSubtree": (boolean, False),
    }


class LdapMetadata(AWSProperty):
    props = {
        "InterBrokerCreds": ([InterBrokerCred], False),
        "ServerMetadata": (ServerMetadata, True),
    }


class LdapServerMetadata(AWSProperty):
    props = {
        "Hosts": ([str], True),
        "RoleBase": (str, True),
        "RoleName": (str, False),
        "RoleSearchMatching": (str, True),
        "RoleSearchSubtree": (boolean, False),
        "ServiceAccountPassword": (str, True),
        "ServiceAccountUsername": (str, True),
        "UserBase": (str, True),
        "UserRoleName": (str, False),
        "UserSearchMatching": (str, True),
        "UserSearchSubtree": (boolean, False),
    }


class LogsConfiguration(AWSProperty):
    props = {
        "Audit": (boolean, False),
        "General": (boolean, False),
    }


class MaintenanceWindow(AWSProperty):
    props = {
        "DayOfWeek": (str, True),
        "TimeOfDay": (str, True),
        "TimeZone": (str, True),
    }


class User(AWSProperty):
    props = {
        "ConsoleAccess": (boolean, False),
        "Groups": ([str], False),
        "Password": (str, True),
        "Username": (str, True),
    }


class Broker(AWSObject):
    resource_type = "AWS::AmazonMQ::Broker"

    props = {
        "AuthenticationStrategy": (str, False),
        "AutoMinorVersionUpgrade": (boolean, True),
        "BrokerName": (str, True),
        "Configuration": (ConfigurationId, False),
        "DeploymentMode": (str, True),
        "EncryptionOptions": (EncryptionOptions, False),
        "EngineType": (str, True),
        "EngineVersion": (str, True),
        "HostInstanceType": (str, True),
        "LdapMetadata": (LdapMetadata, False),
        "LdapServerMetadata": (LdapServerMetadata, False),
        "Logs": (LogsConfiguration, False),
        "MaintenanceWindowStartTime": (MaintenanceWindow, False),
        "PubliclyAccessible": (boolean, True),
        "SecurityGroups": ([str], False),
        "StorageType": (str, False),
        "SubnetIds": ([str], False),
        "Tags": ((Tags, list), False),
        "Users": ([User], True),
    }


class Configuration(AWSObject):
    resource_type = "AWS::AmazonMQ::Configuration"

    props = {
        "Data": (str, True),
        "Description": (str, False),
        "EngineType": (str, True),
        "EngineVersion": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class ConfigurationAssociation(AWSObject):
    resource_type = "AWS::AmazonMQ::ConfigurationAssociation"

    props = {
        "Broker": (str, True),
        "Configuration": (ConfigurationId, True),
    }