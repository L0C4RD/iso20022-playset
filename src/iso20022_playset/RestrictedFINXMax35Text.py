from . import base_types

class RestrictedFINXMax35Text(base_types._BaseDataType_String):

	_max = 35
	_min = 1
	_pattern = r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}"

