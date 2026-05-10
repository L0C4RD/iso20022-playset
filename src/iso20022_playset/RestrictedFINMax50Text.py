from . import base_types

class RestrictedFINMax50Text(base_types._BaseDataType_String):

	_max = 50
	_min = 1
	_pattern = r"([^/]+/)+([^/]+)|([^/]*)"

