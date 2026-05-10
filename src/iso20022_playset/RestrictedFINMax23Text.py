import base_types

class RestrictedFINMax23Text(base_types._BaseDataType_String):

	_max = 23
	_min = 1
	_pattern = r"([^/]+/)+([^/]+)|([^/]*)"

