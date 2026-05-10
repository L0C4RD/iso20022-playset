from . import base_types

class ProcessedStatus7Code(base_types._BaseDataType_String):

	_values = {
		"RECE",
		"SENT",
		"SNAV",
		"WARN",
		"PACK",
		"PEND",
	}

