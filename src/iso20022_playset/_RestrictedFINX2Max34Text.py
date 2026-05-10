from . import base_types

class RestrictedFINX2Max34Text(base_types._BaseDataType_String):

	_max = 34
	_min = 1
	_pattern = r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,34}"

