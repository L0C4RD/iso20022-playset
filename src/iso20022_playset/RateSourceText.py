import base_types

class RateSourceText(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z]{3}[0-9]{1,2}"

