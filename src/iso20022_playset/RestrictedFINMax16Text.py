import base_types

class RestrictedFINMax16Text(base_types._BaseDataType_String):

	_max = 16
	_min = 1
	_pattern = r"([^/]+/)+([^/]+)|([^/]*)"

