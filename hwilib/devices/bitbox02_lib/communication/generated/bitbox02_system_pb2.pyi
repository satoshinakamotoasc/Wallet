"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CheckSDCardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CheckSDCardRequest = CheckSDCardRequest

class CheckSDCardResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INSERTED_FIELD_NUMBER: builtins.int
    inserted: builtins.bool
    def __init__(self,
        *,
        inserted: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["inserted",b"inserted"]) -> None: ...
global___CheckSDCardResponse = CheckSDCardResponse

class DeviceInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DeviceInfoRequest = DeviceInfoRequest

class DeviceInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    INITIALIZED_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    MNEMONIC_PASSPHRASE_ENABLED_FIELD_NUMBER: builtins.int
    MONOTONIC_INCREMENTS_REMAINING_FIELD_NUMBER: builtins.int
    SECURECHIP_MODEL_FIELD_NUMBER: builtins.int
    name: typing.Text
    initialized: builtins.bool
    version: typing.Text
    mnemonic_passphrase_enabled: builtins.bool
    monotonic_increments_remaining: builtins.int
    securechip_model: typing.Text
    """From v9.6.0: "ATECC608A" or "ATECC608B"."""

    def __init__(self,
        *,
        name: typing.Text = ...,
        initialized: builtins.bool = ...,
        version: typing.Text = ...,
        mnemonic_passphrase_enabled: builtins.bool = ...,
        monotonic_increments_remaining: builtins.int = ...,
        securechip_model: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["initialized",b"initialized","mnemonic_passphrase_enabled",b"mnemonic_passphrase_enabled","monotonic_increments_remaining",b"monotonic_increments_remaining","name",b"name","securechip_model",b"securechip_model","version",b"version"]) -> None: ...
global___DeviceInfoResponse = DeviceInfoResponse

class InsertRemoveSDCardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _SDCardAction:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SDCardActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[InsertRemoveSDCardRequest._SDCardAction.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        REMOVE_CARD: InsertRemoveSDCardRequest._SDCardAction.ValueType  # 0
        INSERT_CARD: InsertRemoveSDCardRequest._SDCardAction.ValueType  # 1
    class SDCardAction(_SDCardAction, metaclass=_SDCardActionEnumTypeWrapper):
        pass

    REMOVE_CARD: InsertRemoveSDCardRequest.SDCardAction.ValueType  # 0
    INSERT_CARD: InsertRemoveSDCardRequest.SDCardAction.ValueType  # 1

    ACTION_FIELD_NUMBER: builtins.int
    action: global___InsertRemoveSDCardRequest.SDCardAction.ValueType
    def __init__(self,
        *,
        action: global___InsertRemoveSDCardRequest.SDCardAction.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action",b"action"]) -> None: ...
global___InsertRemoveSDCardRequest = InsertRemoveSDCardRequest

class ResetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ResetRequest = ResetRequest

class SetDeviceLanguageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LANGUAGE_FIELD_NUMBER: builtins.int
    language: typing.Text
    def __init__(self,
        *,
        language: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language",b"language"]) -> None: ...
global___SetDeviceLanguageRequest = SetDeviceLanguageRequest

class SetDeviceNameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___SetDeviceNameRequest = SetDeviceNameRequest

class SetPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTROPY_FIELD_NUMBER: builtins.int
    entropy: builtins.bytes
    def __init__(self,
        *,
        entropy: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entropy",b"entropy"]) -> None: ...
global___SetPasswordRequest = SetPasswordRequest
