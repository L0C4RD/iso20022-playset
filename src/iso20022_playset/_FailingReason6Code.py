from . import base_types

class FailingReason6Code(base_types._BaseDataType_String):

	_values = {
		"BLOC",
		"PART",
		"LINK",
		"LACK",
		"CYCL",
		"SBLO",
		"OTHR",
		"LATE",
		"CERT",
		"PRSY",
		"INBC",
	}

