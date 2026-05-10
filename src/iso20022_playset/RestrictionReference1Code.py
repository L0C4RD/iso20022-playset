from . import base_types

class RestrictionReference1Code(base_types._BaseDataType_String):

	_max = 4
	_min = 1
	_values = {
		"ADDC",
		"ADDS",
		"REMC",
		"REMS",
	}

