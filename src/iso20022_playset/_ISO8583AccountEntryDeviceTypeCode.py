from . import base_types

class ISO8583AccountEntryDeviceTypeCode(base_types._BaseDataType_String):

	_pattern = r"[0-9A-Z]{1,1}"

