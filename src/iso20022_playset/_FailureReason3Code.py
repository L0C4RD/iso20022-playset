from . import base_types

class FailureReason3Code(base_types._BaseDataType_String):

	_values = {
		"CDCL",
		"CUCL",
		"MALF",
		"FDCL",
		"NDCL",
		"PART",
		"SFRD",
		"TIMO",
		"LATE",
		"UCMP",
		"USND",
		"SECU",
	}

