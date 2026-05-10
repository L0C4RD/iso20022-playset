from . import base_types

class RestrictedFINXMax350Text(base_types._BaseDataType_String):

	_max = 350
	_min = 1
	_pattern = r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}"

