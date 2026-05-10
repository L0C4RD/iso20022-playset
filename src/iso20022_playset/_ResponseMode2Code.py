from . import base_types

class ResponseMode2Code(base_types._BaseDataType_String):

	_values = {
		"SEND",
		"IMMD",
		"NREQ",
		"PEND",
	}

