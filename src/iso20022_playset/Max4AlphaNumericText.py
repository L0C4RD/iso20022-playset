from . import base_types

class Max4AlphaNumericText(base_types._BaseDataType_String):

	_max = 4
	_min = 1
	_pattern = r"[a-zA-Z0-9]{1,4}"

