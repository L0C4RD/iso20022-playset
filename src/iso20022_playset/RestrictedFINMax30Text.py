from . import base_types

class RestrictedFINMax30Text(base_types._BaseDataType_String):

	_max = 30
	_min = 1
	_pattern = r"([^/]+/)+([^/]+)|([^/]*)"

