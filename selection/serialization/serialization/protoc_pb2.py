# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serialization.protoc
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14serialization.protoc\x12\tselection\"\x8e\x01\n\x06Sample\x12/\n\x0bsample_type\x18\x01 \x01(\x0e\x32\x15.selection.SampleTypeH\x00\x88\x01\x01\x12\x16\n\tsample_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x15mswc_embedding_vector\x18\x03 \x03(\x02\x42\x0e\n\x0c_sample_typeB\x0c\n\n_sample_id\"-\n\x07Samples\x12\"\n\x07samples\x18\x01 \x03(\x0b\x32\x11.selection.Sample*\'\n\nSampleType\x12\n\n\x06TARGET\x10\x00\x12\r\n\tNONTARGET\x10\x01\x62\x06proto3')

_SAMPLETYPE = DESCRIPTOR.enum_types_by_name['SampleType']
SampleType = enum_type_wrapper.EnumTypeWrapper(_SAMPLETYPE)
TARGET = 0
NONTARGET = 1


_SAMPLE = DESCRIPTOR.message_types_by_name['Sample']
_SAMPLES = DESCRIPTOR.message_types_by_name['Samples']
Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLE,
  '__module__' : 'serialization.protoc_pb2'
  # @@protoc_insertion_point(class_scope:selection.Sample)
  })
_sym_db.RegisterMessage(Sample)

Samples = _reflection.GeneratedProtocolMessageType('Samples', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLES,
  '__module__' : 'serialization.protoc_pb2'
  # @@protoc_insertion_point(class_scope:selection.Samples)
  })
_sym_db.RegisterMessage(Samples)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SAMPLETYPE._serialized_start=227
  _SAMPLETYPE._serialized_end=266
  _SAMPLE._serialized_start=36
  _SAMPLE._serialized_end=178
  _SAMPLES._serialized_start=180
  _SAMPLES._serialized_end=225
# @@protoc_insertion_point(module_scope)
