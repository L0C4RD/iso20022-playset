from . import base_types

class IssuanceType1Code(base_types._BaseDataType_String):

	_length = 4
	_values = {
		"CRQL",
		"CRQC",
		"ISSU",
		"ISCO",
		"ISAD",
	}

