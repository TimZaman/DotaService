# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dotaservice/protos/DotaService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dotaservice.protos import dota_gcmessages_common_bot_script_pb2 as dotaservice_dot_protos_dot_dota__gcmessages__common__bot__script__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dotaservice/protos/DotaService.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$dotaservice/protos/DotaService.proto\x1a:dotaservice/protos/dota_gcmessages_common_bot_script.proto\"3\n\x06\x41\x63tion\x12)\n\x06\x61\x63tion\x18\x01 \x02(\x0b\x32\x19.CMsgBotWorldState.Action\"6\n\x0bObservation\x12\'\n\x0bworld_state\x18\x01 \x02(\x0b\x32\x12.CMsgBotWorldState\"g\n\x06\x43onfig\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x16\n\x0ehost_timescale\x18\x02 \x02(\r\x12\x1d\n\x15ticks_per_observation\x18\x03 \x02(\r\x12\x15\n\x06render\x18\x04 \x01(\x08:\x05\x66\x61lse2P\n\x0b\x44otaService\x12 \n\x05reset\x12\x07.Config\x1a\x0c.Observation\"\x00\x12\x1f\n\x04step\x12\x07.Action\x1a\x0c.Observation\"\x00')
  ,
  dependencies=[dotaservice_dot_protos_dot_dota__gcmessages__common__bot__script__pb2.DESCRIPTOR,])




_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='Action.action', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=151,
)


_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world_state', full_name='Observation.world_state', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=207,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_id', full_name='Config.game_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_timescale', full_name='Config.host_timescale', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticks_per_observation', full_name='Config.ticks_per_observation', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='render', full_name='Config.render', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=312,
)

_ACTION.fields_by_name['action'].message_type = dotaservice_dot_protos_dot_dota__gcmessages__common__bot__script__pb2._CMSGBOTWORLDSTATE_ACTION
_OBSERVATION.fields_by_name['world_state'].message_type = dotaservice_dot_protos_dot_dota__gcmessages__common__bot__script__pb2._CMSGBOTWORLDSTATE
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'dotaservice.protos.DotaService_pb2'
  # @@protoc_insertion_point(class_scope:Action)
  ))
_sym_db.RegisterMessage(Action)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), dict(
  DESCRIPTOR = _OBSERVATION,
  __module__ = 'dotaservice.protos.DotaService_pb2'
  # @@protoc_insertion_point(class_scope:Observation)
  ))
_sym_db.RegisterMessage(Observation)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'dotaservice.protos.DotaService_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  ))
_sym_db.RegisterMessage(Config)



_DOTASERVICE = _descriptor.ServiceDescriptor(
  name='DotaService',
  full_name='DotaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=314,
  serialized_end=394,
  methods=[
  _descriptor.MethodDescriptor(
    name='reset',
    full_name='DotaService.reset',
    index=0,
    containing_service=None,
    input_type=_CONFIG,
    output_type=_OBSERVATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='step',
    full_name='DotaService.step',
    index=1,
    containing_service=None,
    input_type=_ACTION,
    output_type=_OBSERVATION,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOTASERVICE)

DESCRIPTOR.services_by_name['DotaService'] = _DOTASERVICE

# @@protoc_insertion_point(module_scope)