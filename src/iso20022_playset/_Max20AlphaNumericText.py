from . import base_types

class Max20AlphaNumericText(base_types._BaseDataType_String):

	_max = 20
	_min = 1
	_pattern = r"[a-zA-Z0-9]{1,20}"

