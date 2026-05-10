import base_types

class RestrictedFINExact2Text(base_types._BaseDataType_String):

	_length = 2
	_pattern = r"XX|TS"

