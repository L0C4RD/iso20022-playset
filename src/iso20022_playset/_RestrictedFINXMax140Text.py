from . import base_types

class RestrictedFINXMax140Text(base_types._BaseDataType_String):

	_max = 140
	_min = 1
	_pattern = r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}"

