import base_types

class RestrictedFINXMax24Text(base_types._BaseDataType_String):

	_max = 24
	_min = 1
	_pattern = r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)"

