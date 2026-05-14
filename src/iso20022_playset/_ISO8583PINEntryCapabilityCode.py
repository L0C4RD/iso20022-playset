from . import base_types

class ISO8583PINEntryCapabilityCode(base_types._BaseDataType_String):

	_pattern = r"[0-9]{2,2}"

