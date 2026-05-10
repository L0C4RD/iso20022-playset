from . import base_types

class AuthenticationResult1Code(base_types._BaseDataType_String):

	_values = {
		"DENY",
		"MRCH",
		"CARD",
		"AUTH",
		"CRPT",
		"UCRP",
	}

