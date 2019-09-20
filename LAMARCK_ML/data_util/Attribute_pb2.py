# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LAMARCK_ML/data_util/Attribute.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from LAMARCK_ML.data_util import Shape_pb2 as LAMARCK__ML_dot_data__util_dot_Shape__pb2
from LAMARCK_ML.data_util import DType_pb2 as LAMARCK__ML_dot_data__util_dot_DType__pb2
from LAMARCK_ML.data_util import TypeShape_pb2 as LAMARCK__ML_dot_data__util_dot_TypeShape__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='LAMARCK_ML/data_util/Attribute.proto',
  package='LAMARCK_ML',
  syntax='proto3',
  serialized_pb=_b('\n$LAMARCK_ML/data_util/Attribute.proto\x12\nLAMARCK_ML\x1a LAMARCK_ML/data_util/Shape.proto\x1a LAMARCK_ML/data_util/DType.proto\x1a$LAMARCK_ML/data_util/TypeShape.proto\"\x92\x05\n\x0e\x41ttributeProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x01v\x18\n \x01(\x0b\x32 .LAMARCK_ML.AttributeProto.Value\x1a\xd0\x03\n\x05Value\x12\x12\n\x08\x62ool_val\x18\n \x01(\x08H\x00\x12\x14\n\nstring_val\x18\x0b \x01(\tH\x00\x12\x13\n\tbytes_val\x18\x0c \x01(\x0cH\x00\x12\x11\n\x07int_val\x18\r \x01(\x03H\x00\x12\x14\n\ndouble_val\x18\x0e \x01(\x01H\x00\x12+\n\tshape_val\x18\x0f \x01(\x0b\x32\x16.LAMARCK_ML.ShapeProtoH\x00\x12*\n\x08type_val\x18\x10 \x01(\x0b\x32\x16.LAMARCK_ML.DTypeProtoH\x00\x12-\n\x07nts_val\x18\x11 \x01(\x0b\x32\x1a.LAMARCK_ML.TypeShapeProtoH\x00\x12\x33\n\x08list_val\x18\x12 \x01(\x0b\x32\x1f.LAMARCK_ML.AttributeProto.ListH\x00\x12\x32\n\x07set_val\x18\x13 \x01(\x0b\x32\x1f.LAMARCK_ML.AttributeProto.ListH\x00\x12\x34\n\ttuple_val\x18\x14 \x01(\x0b\x32\x1f.LAMARCK_ML.AttributeProto.ListH\x00\x12\x33\n\x08\x64ict_val\x18\x15 \x01(\x0b\x32\x1f.LAMARCK_ML.AttributeProto.DictH\x00\x42\x03\n\x01v\x1a\x42\n\x04List\x12+\n\x01v\x18\x01 \x03(\x0b\x32 .LAMARCK_ML.AttributeProto.Value\x12\r\n\x05numpy\x18\x02 \x01(\x08\x1a.\n\x04\x44ict\x12&\n\x02vs\x18\x01 \x03(\x0b\x32\x1a.LAMARCK_ML.AttributeProtob\x06proto3')
  ,
  dependencies=[LAMARCK__ML_dot_data__util_dot_Shape__pb2.DESCRIPTOR,LAMARCK__ML_dot_data__util_dot_DType__pb2.DESCRIPTOR,LAMARCK__ML_dot_data__util_dot_TypeShape__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ATTRIBUTEPROTO_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='LAMARCK_ML.AttributeProto.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bool_val', full_name='LAMARCK_ML.AttributeProto.Value.bool_val', index=0,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='LAMARCK_ML.AttributeProto.Value.string_val', index=1,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_val', full_name='LAMARCK_ML.AttributeProto.Value.bytes_val', index=2,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='LAMARCK_ML.AttributeProto.Value.int_val', index=3,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='LAMARCK_ML.AttributeProto.Value.double_val', index=4,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape_val', full_name='LAMARCK_ML.AttributeProto.Value.shape_val', index=5,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_val', full_name='LAMARCK_ML.AttributeProto.Value.type_val', index=6,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nts_val', full_name='LAMARCK_ML.AttributeProto.Value.nts_val', index=7,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list_val', full_name='LAMARCK_ML.AttributeProto.Value.list_val', index=8,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_val', full_name='LAMARCK_ML.AttributeProto.Value.set_val', index=9,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tuple_val', full_name='LAMARCK_ML.AttributeProto.Value.tuple_val', index=10,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dict_val', full_name='LAMARCK_ML.AttributeProto.Value.dict_val', index=11,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='v', full_name='LAMARCK_ML.AttributeProto.Value.v',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=237,
  serialized_end=701,
)

_ATTRIBUTEPROTO_LIST = _descriptor.Descriptor(
  name='List',
  full_name='LAMARCK_ML.AttributeProto.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v', full_name='LAMARCK_ML.AttributeProto.List.v', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numpy', full_name='LAMARCK_ML.AttributeProto.List.numpy', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=703,
  serialized_end=769,
)

_ATTRIBUTEPROTO_DICT = _descriptor.Descriptor(
  name='Dict',
  full_name='LAMARCK_ML.AttributeProto.Dict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vs', full_name='LAMARCK_ML.AttributeProto.Dict.vs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=771,
  serialized_end=817,
)

_ATTRIBUTEPROTO = _descriptor.Descriptor(
  name='AttributeProto',
  full_name='LAMARCK_ML.AttributeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='LAMARCK_ML.AttributeProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v', full_name='LAMARCK_ML.AttributeProto.v', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTEPROTO_VALUE, _ATTRIBUTEPROTO_LIST, _ATTRIBUTEPROTO_DICT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=817,
)

_ATTRIBUTEPROTO_VALUE.fields_by_name['shape_val'].message_type = LAMARCK__ML_dot_data__util_dot_Shape__pb2._SHAPEPROTO
_ATTRIBUTEPROTO_VALUE.fields_by_name['type_val'].message_type = LAMARCK__ML_dot_data__util_dot_DType__pb2._DTYPEPROTO
_ATTRIBUTEPROTO_VALUE.fields_by_name['nts_val'].message_type = LAMARCK__ML_dot_data__util_dot_TypeShape__pb2._TYPESHAPEPROTO
_ATTRIBUTEPROTO_VALUE.fields_by_name['list_val'].message_type = _ATTRIBUTEPROTO_LIST
_ATTRIBUTEPROTO_VALUE.fields_by_name['set_val'].message_type = _ATTRIBUTEPROTO_LIST
_ATTRIBUTEPROTO_VALUE.fields_by_name['tuple_val'].message_type = _ATTRIBUTEPROTO_LIST
_ATTRIBUTEPROTO_VALUE.fields_by_name['dict_val'].message_type = _ATTRIBUTEPROTO_DICT
_ATTRIBUTEPROTO_VALUE.containing_type = _ATTRIBUTEPROTO
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['bool_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['bool_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['string_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['string_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['bytes_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['bytes_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['int_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['int_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['double_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['double_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['shape_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['shape_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['type_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['type_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['nts_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['nts_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['list_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['list_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['set_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['set_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['tuple_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['tuple_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_VALUE.oneofs_by_name['v'].fields.append(
  _ATTRIBUTEPROTO_VALUE.fields_by_name['dict_val'])
_ATTRIBUTEPROTO_VALUE.fields_by_name['dict_val'].containing_oneof = _ATTRIBUTEPROTO_VALUE.oneofs_by_name['v']
_ATTRIBUTEPROTO_LIST.fields_by_name['v'].message_type = _ATTRIBUTEPROTO_VALUE
_ATTRIBUTEPROTO_LIST.containing_type = _ATTRIBUTEPROTO
_ATTRIBUTEPROTO_DICT.fields_by_name['vs'].message_type = _ATTRIBUTEPROTO
_ATTRIBUTEPROTO_DICT.containing_type = _ATTRIBUTEPROTO
_ATTRIBUTEPROTO.fields_by_name['v'].message_type = _ATTRIBUTEPROTO_VALUE
DESCRIPTOR.message_types_by_name['AttributeProto'] = _ATTRIBUTEPROTO

AttributeProto = _reflection.GeneratedProtocolMessageType('AttributeProto', (_message.Message,), dict(

  Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTEPROTO_VALUE,
    __module__ = 'LAMARCK_ML.data_util.Attribute_pb2'
    # @@protoc_insertion_point(class_scope:LAMARCK_ML.AttributeProto.Value)
    ))
  ,

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTEPROTO_LIST,
    __module__ = 'LAMARCK_ML.data_util.Attribute_pb2'
    # @@protoc_insertion_point(class_scope:LAMARCK_ML.AttributeProto.List)
    ))
  ,

  Dict = _reflection.GeneratedProtocolMessageType('Dict', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTEPROTO_DICT,
    __module__ = 'LAMARCK_ML.data_util.Attribute_pb2'
    # @@protoc_insertion_point(class_scope:LAMARCK_ML.AttributeProto.Dict)
    ))
  ,
  DESCRIPTOR = _ATTRIBUTEPROTO,
  __module__ = 'LAMARCK_ML.data_util.Attribute_pb2'
  # @@protoc_insertion_point(class_scope:LAMARCK_ML.AttributeProto)
  ))
_sym_db.RegisterMessage(AttributeProto)
_sym_db.RegisterMessage(AttributeProto.Value)
_sym_db.RegisterMessage(AttributeProto.List)
_sym_db.RegisterMessage(AttributeProto.Dict)


# @@protoc_insertion_point(module_scope)
