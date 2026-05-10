from . import base_types

class ATMCommandReason1Code(base_types._BaseDataType_String):

	_values = {
		"DIAG",
		"MONI",
		"SECU",
		"SYNC",
		"UPDT",
	}

