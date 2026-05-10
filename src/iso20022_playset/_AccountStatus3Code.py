from . import base_types

class AccountStatus3Code(base_types._BaseDataType_String):

	_values = {
		"ENAB",
		"DISA",
		"DELE",
		"FORM",
	}

