# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 25.0.0


from troposphere import Tags

from . import AWSObject


class Domain(AWSObject):
    resource_type = "AWS::CodeArtifact::Domain"

    props = {
        "DomainName": (str, True),
        "EncryptionKey": (str, False),
        "PermissionsPolicyDocument": (dict, False),
        "Tags": (Tags, False),
    }


class Repository(AWSObject):
    resource_type = "AWS::CodeArtifact::Repository"

    props = {
        "Description": (str, False),
        "DomainName": (str, True),
        "DomainOwner": (str, False),
        "ExternalConnections": ([str], False),
        "PermissionsPolicyDocument": (dict, False),
        "RepositoryName": (str, True),
        "Tags": (Tags, False),
        "Upstreams": ([str], False),
    }