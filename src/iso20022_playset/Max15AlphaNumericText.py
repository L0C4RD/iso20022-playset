import base_types

class Max15AlphaNumericText(base_types._BaseDataType_String):

	_max = 15
	_min = 1
	_pattern = r"[a-zA-Z0-9]{1,15}"

