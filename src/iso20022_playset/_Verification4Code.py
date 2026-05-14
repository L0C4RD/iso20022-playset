from . import base_types

class Verification4Code(base_types._BaseDataType_String):

	_values = {
		"FAIL",
		"FUTA",
		"MISS",
		"NOSP",
		"NOVF",
		"PART",
		"SUCC",
		"ERRR",
	}

