from . import base_types

class Status10Code(base_types._BaseDataType_String):

	_values = {
		"COMP",
		"QUED",
		"REJT",
		"PART",
	}

