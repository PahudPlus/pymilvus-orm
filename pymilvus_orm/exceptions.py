# Copyright (C) 2019-2020 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.


class ParamError(ValueError):
    """
    Param of interface is illegal
    """


class ConnectError(ValueError):
    """
    Connect server failed
    """


class NotConnectError(ConnectError):
    """
    Disconnect error
    """


class RepeatingConnectError(ConnectError):
    """
    Try to connect repeatedly
    """


class ConnectionPoolError(ConnectError):
    """
    Waiting timeout error
    """


class FutureTimeoutError(TimeoutError):
    """
    Future timeout
    """


class DeprecatedError(AttributeError):
    """
    Deprecated
    """


class VersionError(AttributeError):
    """
    Version not match
    """


class MilvusException(Exception):

    def __init__(self, code, message):
        super(MilvusException, self).__init__(message)
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

    def __str__(self):
        return f"<{type(self).__name__}: (code={self._code}, message={self._message})>"


class CollectionExistException(MilvusException):
    pass


class CollectionNotExistException(MilvusException):
    pass


class InvalidDimensionException(MilvusException):
    pass


class InvalidMetricTypeException(MilvusException):
    pass


class IllegalCollectionNameException(MilvusException):
    pass


class DescribeCollectionException(MilvusException):
    pass


class PartitionNotExistException(MilvusException):
    pass


class InvalidArgumentException(MilvusException):
    pass


class IndexConflictException(MilvusException):
    pass


class IndexNotExistException(MilvusException):
    pass


class CannotInferSchemaException(MilvusException):
    pass


class SchemaNotReadyException(MilvusException):
    pass


class DataTypeNotMatchException(MilvusException):
    pass


class DataTypeNotSupport(MilvusException):
    pass


class DataNotMatch(MilvusException):
    pass
