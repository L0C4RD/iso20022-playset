import base_types

class RestrictedFINXMax8Text(base_types._BaseDataType_String):

	_max = 8
	_min = 1
	_pattern = r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,8}"

