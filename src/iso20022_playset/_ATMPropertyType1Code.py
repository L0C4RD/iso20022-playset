from . import base_types

class ATMPropertyType1Code(base_types._BaseDataType_String):

	_values = {
		"STRG",
		"NMBR",
		"BOOL",
		"JSON",
		"CSVF",
	}

