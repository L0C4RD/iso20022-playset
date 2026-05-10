from . import base_types

class RestrictedFINMax35Text(base_types._BaseDataType_String):

	_max = 35
	_min = 1
	_pattern = r"([^/]+/)+([^/]+)|([^/]*)"

