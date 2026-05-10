from . import base_types

class BBANIdentifier(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z0-9]{1,30}"

