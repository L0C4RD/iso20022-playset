from . import base_types

class UPICIdentifier(base_types._BaseDataType_String):

	_pattern = r"[0-9]{8,17}"

