import base_types

class RestrictedFINXMax30Text(base_types._BaseDataType_String):

	_max = 30
	_min = 1
	_pattern = r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)"

