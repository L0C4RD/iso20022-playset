from . import base_types

class KeyUsage1Code(base_types._BaseDataType_String):

	_values = {
		"ENCR",
		"DCPT",
		"DENC",
		"DDEC",
		"TRNI",
		"TRNX",
		"MACG",
		"MACV",
		"SIGG",
		"SUGV",
		"PINE",
		"PIND",
		"PINV",
		"KEYG",
		"KEYI",
		"KEYX",
		"KEYD",
	}

