import base_types

class CountryCode(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{2,2}"

