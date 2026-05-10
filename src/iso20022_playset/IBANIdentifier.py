from . import base_types

class IBANIdentifier(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}"

