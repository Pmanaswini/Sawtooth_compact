# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_validator/protobuf/network.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_validator/protobuf/network.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\025sawtooth.sdk.protobufP\001Z\013network_pb2'),
  serialized_pb=_b('\n)sawtooth_validator/protobuf/network.proto\"\x13\n\x11\x44isconnectMessage\"A\n\x13PeerRegisterRequest\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x18\n\x10protocol_version\x18\x02 \x01(\r\"\x17\n\x15PeerUnregisterRequest\"\x11\n\x0fGetPeersRequest\"*\n\x10GetPeersResponse\x12\x16\n\x0epeer_endpoints\x18\x01 \x03(\t\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\"\xb4\x01\n\rGossipMessage\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x30\n\x0c\x63ontent_type\x18\x02 \x01(\x0e\x32\x1a.GossipMessage.ContentType\x12\x14\n\x0ctime_to_live\x18\x03 \x01(\r\"J\n\x0b\x43ontentType\x12\x16\n\x12\x43ONTENT_TYPE_UNSET\x10\x00\x12\t\n\x05\x42LOCK\x10\x01\x12\t\n\x05\x42\x41TCH\x10\x02\x12\r\n\tCONSENSUS\x10\x03\"w\n\x16NetworkAcknowledgement\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.NetworkAcknowledgement.Status\"-\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"K\n\x12GossipBlockRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\t\x12\r\n\x05nonce\x18\x02 \x01(\t\x12\x14\n\x0ctime_to_live\x18\x03 \x01(\r\"&\n\x13GossipBlockResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"&\n\x13GossipBatchResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"N\n\x1bGossipBatchByBatchIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05nonce\x18\x02 \x01(\t\x12\x14\n\x0ctime_to_live\x18\x03 \x01(\r\"U\n!GossipBatchByTransactionIdRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x12\r\n\x05nonce\x18\x02 \x01(\t\x12\x14\n\x0ctime_to_live\x18\x03 \x01(\rB&\n\x15sawtooth.sdk.protobufP\x01Z\x0bnetwork_pb2b\x06proto3')
)



_GOSSIPMESSAGE_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='GossipMessage.ContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTENT_TYPE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATCH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSENSUS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=359,
  serialized_end=433,
)
_sym_db.RegisterEnumDescriptor(_GOSSIPMESSAGE_CONTENTTYPE)

_NETWORKACKNOWLEDGEMENT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='NetworkAcknowledgement.Status',
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
  serialized_start=509,
  serialized_end=554,
)
_sym_db.RegisterEnumDescriptor(_NETWORKACKNOWLEDGEMENT_STATUS)


_DISCONNECTMESSAGE = _descriptor.Descriptor(
  name='DisconnectMessage',
  full_name='DisconnectMessage',
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
  serialized_start=45,
  serialized_end=64,
)


_PEERREGISTERREQUEST = _descriptor.Descriptor(
  name='PeerRegisterRequest',
  full_name='PeerRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='PeerRegisterRequest.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='PeerRegisterRequest.protocol_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=66,
  serialized_end=131,
)


_PEERUNREGISTERREQUEST = _descriptor.Descriptor(
  name='PeerUnregisterRequest',
  full_name='PeerUnregisterRequest',
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
  serialized_start=133,
  serialized_end=156,
)


_GETPEERSREQUEST = _descriptor.Descriptor(
  name='GetPeersRequest',
  full_name='GetPeersRequest',
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
  serialized_start=158,
  serialized_end=175,
)


_GETPEERSRESPONSE = _descriptor.Descriptor(
  name='GetPeersResponse',
  full_name='GetPeersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer_endpoints', full_name='GetPeersResponse.peer_endpoints', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=177,
  serialized_end=219,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='PingRequest',
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
  serialized_start=221,
  serialized_end=234,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='PingResponse',
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
  serialized_start=236,
  serialized_end=250,
)


_GOSSIPMESSAGE = _descriptor.Descriptor(
  name='GossipMessage',
  full_name='GossipMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='GossipMessage.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='GossipMessage.content_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_to_live', full_name='GossipMessage.time_to_live', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GOSSIPMESSAGE_CONTENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=433,
)


_NETWORKACKNOWLEDGEMENT = _descriptor.Descriptor(
  name='NetworkAcknowledgement',
  full_name='NetworkAcknowledgement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='NetworkAcknowledgement.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKACKNOWLEDGEMENT_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=554,
)


_GOSSIPBLOCKREQUEST = _descriptor.Descriptor(
  name='GossipBlockRequest',
  full_name='GossipBlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_id', full_name='GossipBlockRequest.block_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='GossipBlockRequest.nonce', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_to_live', full_name='GossipBlockRequest.time_to_live', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=556,
  serialized_end=631,
)


_GOSSIPBLOCKRESPONSE = _descriptor.Descriptor(
  name='GossipBlockResponse',
  full_name='GossipBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='GossipBlockResponse.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=633,
  serialized_end=671,
)


_GOSSIPBATCHRESPONSE = _descriptor.Descriptor(
  name='GossipBatchResponse',
  full_name='GossipBatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='GossipBatchResponse.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=673,
  serialized_end=711,
)


_GOSSIPBATCHBYBATCHIDREQUEST = _descriptor.Descriptor(
  name='GossipBatchByBatchIdRequest',
  full_name='GossipBatchByBatchIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GossipBatchByBatchIdRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='GossipBatchByBatchIdRequest.nonce', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_to_live', full_name='GossipBatchByBatchIdRequest.time_to_live', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=713,
  serialized_end=791,
)


_GOSSIPBATCHBYTRANSACTIONIDREQUEST = _descriptor.Descriptor(
  name='GossipBatchByTransactionIdRequest',
  full_name='GossipBatchByTransactionIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='GossipBatchByTransactionIdRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='GossipBatchByTransactionIdRequest.nonce', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_to_live', full_name='GossipBatchByTransactionIdRequest.time_to_live', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=793,
  serialized_end=878,
)

_GOSSIPMESSAGE.fields_by_name['content_type'].enum_type = _GOSSIPMESSAGE_CONTENTTYPE
_GOSSIPMESSAGE_CONTENTTYPE.containing_type = _GOSSIPMESSAGE
_NETWORKACKNOWLEDGEMENT.fields_by_name['status'].enum_type = _NETWORKACKNOWLEDGEMENT_STATUS
_NETWORKACKNOWLEDGEMENT_STATUS.containing_type = _NETWORKACKNOWLEDGEMENT
DESCRIPTOR.message_types_by_name['DisconnectMessage'] = _DISCONNECTMESSAGE
DESCRIPTOR.message_types_by_name['PeerRegisterRequest'] = _PEERREGISTERREQUEST
DESCRIPTOR.message_types_by_name['PeerUnregisterRequest'] = _PEERUNREGISTERREQUEST
DESCRIPTOR.message_types_by_name['GetPeersRequest'] = _GETPEERSREQUEST
DESCRIPTOR.message_types_by_name['GetPeersResponse'] = _GETPEERSRESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
DESCRIPTOR.message_types_by_name['GossipMessage'] = _GOSSIPMESSAGE
DESCRIPTOR.message_types_by_name['NetworkAcknowledgement'] = _NETWORKACKNOWLEDGEMENT
DESCRIPTOR.message_types_by_name['GossipBlockRequest'] = _GOSSIPBLOCKREQUEST
DESCRIPTOR.message_types_by_name['GossipBlockResponse'] = _GOSSIPBLOCKRESPONSE
DESCRIPTOR.message_types_by_name['GossipBatchResponse'] = _GOSSIPBATCHRESPONSE
DESCRIPTOR.message_types_by_name['GossipBatchByBatchIdRequest'] = _GOSSIPBATCHBYBATCHIDREQUEST
DESCRIPTOR.message_types_by_name['GossipBatchByTransactionIdRequest'] = _GOSSIPBATCHBYTRANSACTIONIDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DisconnectMessage = _reflection.GeneratedProtocolMessageType('DisconnectMessage', (_message.Message,), dict(
  DESCRIPTOR = _DISCONNECTMESSAGE,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:DisconnectMessage)
  ))
_sym_db.RegisterMessage(DisconnectMessage)

PeerRegisterRequest = _reflection.GeneratedProtocolMessageType('PeerRegisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _PEERREGISTERREQUEST,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:PeerRegisterRequest)
  ))
_sym_db.RegisterMessage(PeerRegisterRequest)

PeerUnregisterRequest = _reflection.GeneratedProtocolMessageType('PeerUnregisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _PEERUNREGISTERREQUEST,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:PeerUnregisterRequest)
  ))
_sym_db.RegisterMessage(PeerUnregisterRequest)

GetPeersRequest = _reflection.GeneratedProtocolMessageType('GetPeersRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPEERSREQUEST,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GetPeersRequest)
  ))
_sym_db.RegisterMessage(GetPeersRequest)

GetPeersResponse = _reflection.GeneratedProtocolMessageType('GetPeersResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPEERSRESPONSE,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GetPeersResponse)
  ))
_sym_db.RegisterMessage(GetPeersResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESPONSE,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:PingResponse)
  ))
_sym_db.RegisterMessage(PingResponse)

GossipMessage = _reflection.GeneratedProtocolMessageType('GossipMessage', (_message.Message,), dict(
  DESCRIPTOR = _GOSSIPMESSAGE,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GossipMessage)
  ))
_sym_db.RegisterMessage(GossipMessage)

NetworkAcknowledgement = _reflection.GeneratedProtocolMessageType('NetworkAcknowledgement', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKACKNOWLEDGEMENT,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:NetworkAcknowledgement)
  ))
_sym_db.RegisterMessage(NetworkAcknowledgement)

GossipBlockRequest = _reflection.GeneratedProtocolMessageType('GossipBlockRequest', (_message.Message,), dict(
  DESCRIPTOR = _GOSSIPBLOCKREQUEST,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GossipBlockRequest)
  ))
_sym_db.RegisterMessage(GossipBlockRequest)

GossipBlockResponse = _reflection.GeneratedProtocolMessageType('GossipBlockResponse', (_message.Message,), dict(
  DESCRIPTOR = _GOSSIPBLOCKRESPONSE,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GossipBlockResponse)
  ))
_sym_db.RegisterMessage(GossipBlockResponse)

GossipBatchResponse = _reflection.GeneratedProtocolMessageType('GossipBatchResponse', (_message.Message,), dict(
  DESCRIPTOR = _GOSSIPBATCHRESPONSE,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GossipBatchResponse)
  ))
_sym_db.RegisterMessage(GossipBatchResponse)

GossipBatchByBatchIdRequest = _reflection.GeneratedProtocolMessageType('GossipBatchByBatchIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _GOSSIPBATCHBYBATCHIDREQUEST,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GossipBatchByBatchIdRequest)
  ))
_sym_db.RegisterMessage(GossipBatchByBatchIdRequest)

GossipBatchByTransactionIdRequest = _reflection.GeneratedProtocolMessageType('GossipBatchByTransactionIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _GOSSIPBATCHBYTRANSACTIONIDREQUEST,
  __module__ = 'sawtooth_validator.protobuf.network_pb2'
  # @@protoc_insertion_point(class_scope:GossipBatchByTransactionIdRequest)
  ))
_sym_db.RegisterMessage(GossipBatchByTransactionIdRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)