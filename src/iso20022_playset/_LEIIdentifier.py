from . import base_types

class LEIIdentifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z0-9]{18,18}[0-9]{2,2}"

