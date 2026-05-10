from . import base_types

class Frequency13Code(base_types._BaseDataType_String):

	_max = 4
	_min = 1
	_values = {
		"DAIL",
		"WEEK",
		"MNTH",
		"YEAR",
		"ADHO",
		"EXPI",
		"MIAN",
		"QURT",
	}

