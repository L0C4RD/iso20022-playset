from . import base_types

class RestrictedFINMax210Text(base_types._BaseDataType_String):

	_max = 210
	_min = 1

