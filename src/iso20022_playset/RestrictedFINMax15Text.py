from . import base_types

class RestrictedFINMax15Text(base_types._BaseDataType_String):

	_max = 15
	_min = 1

