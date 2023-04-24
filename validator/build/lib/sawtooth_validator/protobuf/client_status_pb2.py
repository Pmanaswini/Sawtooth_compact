# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_validator/protobuf/client_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_validator/protobuf/client_status.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\025sawtooth.sdk.protobufP\001Z\rclient_status'),
  serialized_pb=_b('\n/sawtooth_validator/protobuf/client_status.proto\"\x18\n\x16\x43lientStatusGetRequest\"\xd3\x01\n\x17\x43lientStatusGetResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.ClientStatusGetResponse.Status\x12,\n\x05peers\x18\x02 \x03(\x0b\x32\x1d.ClientStatusGetResponse.Peer\x12\x10\n\x08\x65ndpoint\x18\x03 \x01(\t\x1a\x18\n\x04Peer\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\"-\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x42(\n\x15sawtooth.sdk.protobufP\x01Z\rclient_statusb\x06proto3')
)



_CLIENTSTATUSGETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientStatusGetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=244,
  serialized_end=289,
)
_sym_db.RegisterEnumDescriptor(_CLIENTSTATUSGETRESPONSE_STATUS)


_CLIENTSTATUSGETREQUEST = _descriptor.Descriptor(
  name='ClientStatusGetRequest',
  full_name='ClientStatusGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=75,
)


_CLIENTSTATUSGETRESPONSE_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='ClientStatusGetResponse.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='ClientStatusGetResponse.Peer.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=242,
)

_CLIENTSTATUSGETRESPONSE = _descriptor.Descriptor(
  name='ClientStatusGetResponse',
  full_name='ClientStatusGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientStatusGetResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peers', full_name='ClientStatusGetResponse.peers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='ClientStatusGetResponse.endpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTSTATUSGETRESPONSE_PEER, ],
  enum_types=[
    _CLIENTSTATUSGETRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=289,
)

_CLIENTSTATUSGETRESPONSE_PEER.containing_type = _CLIENTSTATUSGETRESPONSE
_CLIENTSTATUSGETRESPONSE.fields_by_name['status'].enum_type = _CLIENTSTATUSGETRESPONSE_STATUS
_CLIENTSTATUSGETRESPONSE.fields_by_name['peers'].message_type = _CLIENTSTATUSGETRESPONSE_PEER
_CLIENTSTATUSGETRESPONSE_STATUS.containing_type = _CLIENTSTATUSGETRESPONSE
DESCRIPTOR.message_types_by_name['ClientStatusGetRequest'] = _CLIENTSTATUSGETREQUEST
DESCRIPTOR.message_types_by_name['ClientStatusGetResponse'] = _CLIENTSTATUSGETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientStatusGetRequest = _reflection.GeneratedProtocolMessageType('ClientStatusGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSTATUSGETREQUEST,
  __module__ = 'sawtooth_validator.protobuf.client_status_pb2'
  # @@protoc_insertion_point(class_scope:ClientStatusGetRequest)
  ))
_sym_db.RegisterMessage(ClientStatusGetRequest)

ClientStatusGetResponse = _reflection.GeneratedProtocolMessageType('ClientStatusGetResponse', (_message.Message,), dict(

  Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTSTATUSGETRESPONSE_PEER,
    __module__ = 'sawtooth_validator.protobuf.client_status_pb2'
    # @@protoc_insertion_point(class_scope:ClientStatusGetResponse.Peer)
    ))
  ,
  DESCRIPTOR = _CLIENTSTATUSGETRESPONSE,
  __module__ = 'sawtooth_validator.protobuf.client_status_pb2'
  # @@protoc_insertion_point(class_scope:ClientStatusGetResponse)
  ))
_sym_db.RegisterMessage(ClientStatusGetResponse)
_sym_db.RegisterMessage(ClientStatusGetResponse.Peer)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
