# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: material_request/material_request.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'material_request/material_request.proto\x12\x10material_request\x1a\x1fgoogle/protobuf/timestamp.proto\"\x84\x06\n\x0fMaterialRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x0c\x64\x61te_created\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rdate_modified\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x13\n\x0bmodified_by\x18\x05 \x01(\t\x12T\n\x15material_request_type\x18\x06 \x01(\x0e\x32\x35.material_request.MaterialRequest.MaterialRequestType\x12\x18\n\x10transaction_date\x18\x07 \x01(\t\x12\x16\n\x0escheduled_date\x18\x08 \x01(\t\x12\x38\n\x06status\x18\t \x01(\x0e\x32(.material_request.MaterialRequest.Status\x12\x12\n\ncompany_id\x18\n \x01(\t\x12\x18\n\x10set_warehouse_id\x18\x0b \x01(\t\x12%\n\x1dtarget_warehouse_territory_id\x18\x0c \x01(\t\x12\x34\n\x05items\x18\r \x03(\x0b\x32%.material_request.MaterialRequestItem\"v\n\x13MaterialRequestType\x12\x0c\n\x08PURCHASE\x10\x00\x12\x15\n\x11MATERIAL_TRANSFER\x10\x01\x12\x12\n\x0eMATERIAL_ISSUE\x10\x02\x12\x0f\n\x0bMANUFACTURE\x10\x03\x12\x15\n\x11\x43USTOMER_PROVIDED\x10\x04\"\x96\x01\n\x06Status\x12\t\n\x05\x44RAFT\x10\x00\x12\x0b\n\x07STOPPED\x10\x01\x12\r\n\tCANCELLED\x10\x02\x12\x15\n\x11PARTIALLY_ORDERED\x10\x03\x12\x16\n\x12PARTIALLY_RECEIVED\x10\x04\x12\x0b\n\x07ORDERED\x10\x05\x12\n\n\x06ISSUED\x10\x06\x12\x0f\n\x0bTRANSFERRED\x10\x07\x12\x0c\n\x08RECEIVED\x10\x08\"\x81\x03\n\x13MaterialRequestItem\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x11\n\titem_code\x18\x02 \x01(\t\x12\x11\n\titem_name\x18\x03 \x01(\t\x12\x12\n\nitem_group\x18\x04 \x01(\t\x12\r\n\x05\x62rand\x18\x05 \x01(\t\x12\x0b\n\x03qty\x18\x06 \x01(\x02\x12\x11\n\tstock_uom\x18\x07 \x01(\t\x12\x0b\n\x03uom\x18\x08 \x01(\t\x12\x14\n\x0cwarehouse_id\x18\t \x01(\t\x12\x19\n\x11\x63onversion_factor\x18\n \x01(\x02\x12\x11\n\tstock_qty\x18\x0b \x01(\x02\x12\x15\n\rmin_order_qty\x18\x0c \x01(\x02\x12\x15\n\rprojected_qty\x18\r \x01(\x02\x12\x12\n\nactual_qty\x18\x0e \x01(\x02\x12\x13\n\x0bordered_qty\x18\x0f \x01(\x02\x12\x14\n\x0creceived_qty\x18\x10 \x01(\x02\x12\x0c\n\x04rate\x18\x11 \x01(\x02\x12\x0e\n\x06\x61mount\x18\x12 \x01(\x02\x12\x14\n\x0cterritory_id\x18\x13 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'material_request.material_request_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MATERIALREQUEST']._serialized_start=95
  _globals['_MATERIALREQUEST']._serialized_end=867
  _globals['_MATERIALREQUEST_MATERIALREQUESTTYPE']._serialized_start=596
  _globals['_MATERIALREQUEST_MATERIALREQUESTTYPE']._serialized_end=714
  _globals['_MATERIALREQUEST_STATUS']._serialized_start=717
  _globals['_MATERIALREQUEST_STATUS']._serialized_end=867
  _globals['_MATERIALREQUESTITEM']._serialized_start=870
  _globals['_MATERIALREQUESTITEM']._serialized_end=1255
# @@protoc_insertion_point(module_scope)
