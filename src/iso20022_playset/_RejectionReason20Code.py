from . import base_types

class RejectionReason20Code(base_types._BaseDataType_String):

	_values = {
		"FAIL",
		"CASA",
		"CORR",
		"STAN",
		"NOHO",
	}

